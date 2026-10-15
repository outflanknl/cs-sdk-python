# cs_sdk_python.api_client.ServerConfigApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_root**](ServerConfigApi.md#api_root) | **GET** /api/v1 | Entry point to the API
[**get_c2_profile**](ServerConfigApi.md#get_c2_profile) | **GET** /api/v1/config/profile | Get Malleable Profile
[**get_kill_date**](ServerConfigApi.md#get_kill_date) | **GET** /api/v1/config/killdate | Get the Beacon kill date configured on the team server
[**get_system_information**](ServerConfigApi.md#get_system_information) | **GET** /api/v1/config/systeminformation | Get System Information
[**get_teamserver_ip**](ServerConfigApi.md#get_teamserver_ip) | **GET** /api/v1/config/teamserverIp | Get team server IP
[**reset_data**](ServerConfigApi.md#reset_data) | **DELETE** /api/v1/config/resetData | Reset Data Model


# **api_root**
> str api_root()

Entry point to the API

Entry point to the API

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.api_root()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **get_c2_profile**
> str get_c2_profile()

Get Malleable Profile

Retrieve the Malleable C2 profile.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.get_c2_profile()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **get_kill_date**
> str get_kill_date()

Get the Beacon kill date configured on the team server

Get the Beacon kill date configured on the team server.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.get_kill_date()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **get_system_information**
> str get_system_information()

Get System Information

Get information about your Cobalt Strike configuration. This information can help in troubleshooting or support requests.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.get_system_information()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **get_teamserver_ip**
> str get_teamserver_ip()

Get team server IP

Retrieve the IP address associated with the team server.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.get_teamserver_ip()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **reset_data**
> str reset_data()

Reset Data Model

Reset Cobalt Strike's data model. Use with care as all the inventory will be reset (Listeners, Credentials, Keys, Downloads, etc.).

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ServerConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ServerConfigApi(client)
        response = await api.reset_data()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

