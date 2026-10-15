# cs_sdk_python.api_client

Async REST API client for Cobalt Strike API (API 1.0.0-BETA), generated with
OpenAPI Generator 7.14.0 and the Python asyncio library.

See the [SDK README](../../README.md) for installation, authentication, and a
complete example. Python 3.13+ is required.

## Documentation for API Endpoints

All URIs are relative to *https://localhost:50443*.

- [BeaconConfigApi](BeaconConfigApi.md)
- [BeaconInfoApi](BeaconInfoApi.md)
- [CaptureApi](CaptureApi.md)
- [ConsoleCommandApi](ConsoleCommandApi.md)
- [CredsAndTokensApi](CredsAndTokensApi.md)
- [FileAndRegistryApi](FileAndRegistryApi.md)
- [JobsAndTasksApi](JobsAndTasksApi.md)
- [ListenersApi](ListenersApi.md)
- [NetworkReconApi](NetworkReconApi.md)
- [PayloadAndArtifactsApi](PayloadAndArtifactsApi.md)
- [PivotingApi](PivotingApi.md)
- [ProcessAndExecutionApi](ProcessAndExecutionApi.md)
- [SecurityApi](SecurityApi.md)
- [ServerConfigApi](ServerConfigApi.md)
- [TunnelingApi](TunnelingApi.md)

## Documentation for Models

Request and response models are linked from the endpoint reference pages above.

## Authentication

<a id="BearerAuthentication"></a>

### BearerAuthentication

Set `Configuration.access_token` to a JWT returned by
[`SecurityApi.authenticate_user`](SecurityApi.md#authenticate_user).
The login endpoint does not require an existing token. Tokens are not refreshed
automatically; request a new token when needed.

```python
from cs_sdk_python.api_client import Configuration

config = Configuration(host="https://localhost:50443")
config.access_token = "your-access-token"
```

The host is the server origin, without an `/api` suffix. TLS certificate
verification is enabled by default; set `config.ssl_ca_cert` for a private CA.
