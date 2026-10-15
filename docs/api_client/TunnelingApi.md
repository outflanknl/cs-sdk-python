# cs_sdk_python.api_client.TunnelingApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_browser_pivot_stop**](TunnelingApi.md#execute_browser_pivot_stop) | **POST** /api/v1/beacons/{bid}/execute/browserpivotStop | Stop Browser Pivot
[**execute_remote_port_forward_start_on_teamserver**](TunnelingApi.md#execute_remote_port_forward_start_on_teamserver) | **POST** /api/v1/beacons/{bid}/execute/rportfwdStart/onTeamserver | Start Remote Port Forwarding
[**execute_remote_port_forward_stop_on_teamserver**](TunnelingApi.md#execute_remote_port_forward_stop_on_teamserver) | **POST** /api/v1/beacons/{bid}/execute/rportfwdStop/onTeamserver | Stop Reverse Port Forwarding
[**execute_socks4_start**](TunnelingApi.md#execute_socks4_start) | **POST** /api/v1/beacons/{bid}/execute/socks4Start | Start SOCKS4a Server
[**execute_socks5_start**](TunnelingApi.md#execute_socks5_start) | **POST** /api/v1/beacons/{bid}/execute/socks5Start | Start SOCKS5 Server
[**execute_socks_stop_all**](TunnelingApi.md#execute_socks_stop_all) | **POST** /api/v1/beacons/{bid}/execute/socksStop/all | Stop All SOCKS Servers
[**execute_socks_stop_by_port**](TunnelingApi.md#execute_socks_stop_by_port) | **POST** /api/v1/beacons/{bid}/execute/socksStop/{port} | Stop SOCKS Server
[**inject_browser_pivot_start**](TunnelingApi.md#inject_browser_pivot_start) | **POST** /api/v1/beacons/{bid}/inject/browserpivotStart | Start Browser Pivot (Inject)


# **execute_browser_pivot_stop**
> AsyncCommandResponse execute_browser_pivot_stop(bid)

Stop Browser Pivot

Tear down the browser pivoting sessions associated with this Beacon.

Related CS Console Command: browserpivot

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_browser_pivot_stop(
            bid='bid_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

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

# **execute_remote_port_forward_start_on_teamserver**
> AsyncCommandResponse execute_remote_port_forward_start_on_teamserver(bid, request_model)

Start Remote Port Forwarding

Binds the specified port on the target host. When a connection comes in, Cobalt Strike will make a connection to the forwarded host/port and use Beacon to relay traffic between the two connections.

Related CS Console Command: rportfwd

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_remote_port_forward_start_on_teamserver(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RportForwardBindDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RportForwardBindDto**](RportForwardBindDto.md)|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **execute_remote_port_forward_stop_on_teamserver**
> AsyncCommandResponse execute_remote_port_forward_stop_on_teamserver(bid, request_model)

Stop Reverse Port Forwarding

Stop remote port forward on the specific port.

Related CS Console Command: rportfwd stop

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_remote_port_forward_stop_on_teamserver(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RportFwdStopDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RportFwdStopDto**](RportFwdStopDto.md)|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **execute_socks4_start**
> AsyncCommandResponse execute_socks4_start(bid, request_model)

Start SOCKS4a Server

Starts a SOCKS4a server on the specified port.

Related CS Console Command: socks [port] socks4

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_socks4_start(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.Socks4StartDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**Socks4StartDto**](Socks4StartDto.md)|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **execute_socks5_start**
> AsyncCommandResponse execute_socks5_start(bid, request_model)

Start SOCKS5 Server

Starts a SOCKS5 server on the specified port.

Related CS Console Command: socks [port] socks5

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_socks5_start(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.Socks5StartDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**Socks5StartDto**](Socks5StartDto.md)|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **execute_socks_stop_all**
> AsyncCommandResponse execute_socks_stop_all(bid)

Stop All SOCKS Servers

Stop the SOCKS servers and terminate existing connections.

Related CS Console Command: socks stop

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_socks_stop_all(
            bid='bid_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

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

# **execute_socks_stop_by_port**
> AsyncCommandResponse execute_socks_stop_by_port(bid, port)

Stop SOCKS Server

Stop the specific SOCKS server and terminate existing connections.

Related CS Console Command: socks stop

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.execute_socks_stop_by_port(
            bid='bid_example',
            port=56,
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **port** | **int**|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

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

# **inject_browser_pivot_start**
> AsyncCommandResponse inject_browser_pivot_start(bid, request_model)

Start Browser Pivot (Inject)

Start a Browser Pivot into the specified process. To hijack authenticated web sessions, make sure the process is an Internet Explorer tab. These processes have iexplore.exe as their parent process.

Related CS Console Command: browserpivot

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import TunnelingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = TunnelingApi(client)
        response = await api.inject_browser_pivot_start(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.BrowserPivotSetupDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**BrowserPivotSetupDto**](BrowserPivotSetupDto.md)|  | 

### Return type

[**AsyncCommandResponse**](AsyncCommandResponse.md)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

