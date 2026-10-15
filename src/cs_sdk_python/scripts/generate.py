"""Regenerate the asyncio client with the OpenAPI Generator."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

ROOT = Path(__file__).resolve().parents[3]


def load_spec(path: Path) -> dict[str, Any]:
    """Read JSON or the supplied `var spec = {...};` wrapper without executing JS."""
    text = path.read_text(encoding="utf-8-sig").strip()
    if re.match(r"^(?:var|let|const)\s+spec\s*=", text):
        text = re.sub(r"^(?:var|let|const)\s+spec\s*=\s*", "", text, count=1)
        text = text.removesuffix(";").rstrip()
    spec = json.loads(text)
    if not isinstance(spec, dict) or not str(spec.get("openapi", "")).startswith("3."):
        raise ValueError("Expected an OpenAPI 3 document")
    if not isinstance(spec.get("paths"), dict) or not spec["paths"]:
        raise ValueError("OpenAPI document must contain paths")
    return spec


def prepare_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """Adapt generator input without changing the checked-in source document."""
    spec = json.loads(json.dumps(spec))
    for path_item in spec["paths"].values():
        for method, operation in path_item.items():
            if (
                method in {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
                and "requestBody" in operation
            ):
                operation["x-codegen-request-body-name"] = "request_model"
    # The source uses singleton enums for wire discriminator values but omits
    # mappings. Generator 7.14 otherwise uses class names (e.g. TextOutputDto)
    # instead of the API's values (e.g. text), breaking from_dict deserialization.
    schemas = spec.get("components", {}).get("schemas", {})
    for name, schema in schemas.items():
        parts = schema.get("allOf", [])
        properties = dict(schema.get("properties", {}))
        for part in parts:
            properties.update(part.get("properties", {}))
        for part in parts:
            parent = schemas.get(part.get("$ref", "").removeprefix("#/components/schemas/"), {})
            discriminator = parent.get("discriminator")
            if discriminator:
                values = properties.get(discriminator["propertyName"], {}).get("enum", [])
                if len(values) == 1:
                    discriminator.setdefault("mapping", {}).setdefault(
                        values[0], f"#/components/schemas/{name}"
                    )
    return spec


def run(*command: str) -> None:
    print("Running: " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def generate(source: Path) -> None:
    spec = load_spec(source)
    cli = ROOT / "node_modules" / ".bin" / "openapi-generator-cli"
    if not cli.is_file():
        run("npm", "ci")

    # Stage and validate the complete output before replacing generated files.
    with TemporaryDirectory(prefix="cs-sdk-generate-") as temporary:
        staging = Path(temporary)
        generator_input = staging / "openapi.generator.json"
        generator_input.write_text(json.dumps(prepare_spec(spec), indent=2) + "\n")
        run(str(cli), "validate", "-i", str(generator_input))
        run(
            str(cli),
            "generate",
            "-i",
            str(generator_input),
            "-g",
            "python",
            "-o",
            str(staging),
            "-c",
            str(ROOT / "openapi-generator-config.yml"),
            "--global-property",
            "apiTests=false,modelTests=false",
        )
        generated = staging / "cs_sdk_python" / "api_client"
        if not (generated / "api_client.py").is_file():
            raise RuntimeError("Generator did not produce an API client")
        run("uv", "run", "ruff", "format", "--isolated", "--line-length", "100", str(generated))
        for source_dir, destination in (
            (generated, ROOT / "src" / "cs_sdk_python" / "api_client"),
            (staging / "docs", ROOT / "docs" / "api_client"),
        ):
            if destination.exists():
                shutil.rmtree(destination)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_dir, destination)
        (ROOT / "openapi.json").write_text(json.dumps(spec, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--spec",
        type=Path,
        default=ROOT / "openapi.json",
        help="JSON or JavaScript-wrapped OpenAPI source (default: checked-in openapi.json)",
    )
    args = parser.parse_args()
    generate(args.spec.resolve())


if __name__ == "__main__":
    main()
