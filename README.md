# cs-sdk-python

Async Python SDK for the Cobalt Strike REST API, generated from
`cobalt-strike-openapi.js` (API version `1.0.0-BETA`). Requires Python 3.13+.

Uses **OpenAPI Generator 7.14.0**, the Python **asyncio** library, and Pydantic v2.
Clients and models live under `cs_sdk_python.api_client`.

## Install

From this checkout:

```bash
uv sync
```

In another project, install from this directory with `pip install /path/to/cs-sdk-python`
or `uv add /path/to/cs-sdk-python`.

## Usage

```python
import asyncio
import os

from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconInfoApi, SecurityApi
from cs_sdk_python.api_client.models import LoginRequest


async def main() -> None:
    config = Configuration(host="https://localhost:50443")
    # For a private CA, set config.ssl_ca_cert to the trusted CA PEM path.
    async with ApiClient(config) as client:
        auth = await SecurityApi(client).authenticate_user(
            request_model=LoginRequest(
                username=os.environ["CS_USERNAME"],
                password=os.environ["CS_PASSWORD"],
            )
        )
        config.access_token = auth.access_token
        for beacon in await BeaconInfoApi(client).list_beacons():
            print(beacon.bid, beacon.computer, beacon.user)


asyncio.run(main())
```

For an existing token, set `config.access_token` directly. The host is the server
origin; endpoint paths already include `/api`. Use the async context manager to
close connections. TLS verification is enabled by default.

See the [generated API and model reference](docs/api_client/README.md).
Methods accept `_request_timeout` and provide `_with_http_info` and
`_without_preload_content` variants. The latter returns an `aiohttp.ClientResponse`
for streaming or binary responses; read and release it when finished.

The source spec describes screenshot and download bodies as an untyped
`StreamingResponseBody`. Use `CaptureApi.get_screenshot_without_preload_content`
and `FileAndRegistryApi.get_download_without_preload_content` for these binary
endpoints, rather than their default JSON-decoding variants.

## Regenerate

Requires Java, Node.js/npm, and uv. Generator and dependency versions are locked
in `openapitools.json`, `package-lock.json`, and `uv.lock`.

```bash
uv sync --group dev
npm ci
uv run python -m cs_sdk_python.scripts.generate
```

To refresh from the original JavaScript file:

```bash
uv run python -m cs_sdk_python.scripts.generate --spec ../cobalt-strike-openapi.js
```

The script extracts JSON without executing JavaScript, validates the spec, and
regenerates `src/cs_sdk_python/api_client/` and `docs/api_client/`. The checked-in
`openapi.json` preserves the source document, so future generation does not require
a sibling checkout. Request bodies use the `request_model` parameter. Make changes
to the generator configuration, templates, or script rather than editing generated
files.

Generation also adds explicit discriminator mappings derived from the source's
fixed `type` enums, so polymorphic arguments and task outputs deserialize using
their wire values. These adaptations are only applied to the generator input.

## Check and build

```bash
uv run ruff check .
uv run ruff format --check .
uv build
```
