# cs_sdk_python.api_client.ListenersApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dns_listener**](ListenersApi.md#add_dns_listener) | **POST** /api/v1/listeners/dns | Add DNS Listener
[**add_external_c2_listener**](ListenersApi.md#add_external_c2_listener) | **POST** /api/v1/listeners/externalC2 | Add External C2 Listener
[**add_foreign_http_listener**](ListenersApi.md#add_foreign_http_listener) | **POST** /api/v1/listeners/foreignHttp | Add Foreign HTTP Listener
[**add_foreign_https_listener**](ListenersApi.md#add_foreign_https_listener) | **POST** /api/v1/listeners/foreignHttps | Add Foreign HTTPS Listener
[**add_http_listener**](ListenersApi.md#add_http_listener) | **POST** /api/v1/listeners/http | Add HTTP Listener
[**add_https_listener**](ListenersApi.md#add_https_listener) | **POST** /api/v1/listeners/https | Add HTTPS Listener
[**add_smb_listener**](ListenersApi.md#add_smb_listener) | **POST** /api/v1/listeners/smb | Add SMB Listener
[**add_tcp_listener**](ListenersApi.md#add_tcp_listener) | **POST** /api/v1/listeners/tcp | Add TCP Listener
[**add_user_defined_c2_listener**](ListenersApi.md#add_user_defined_c2_listener) | **POST** /api/v1/listeners/userDefinedC2 | Add UDC2 Listener
[**delete_listener**](ListenersApi.md#delete_listener) | **DELETE** /api/v1/listeners/{name} | Delete Listener
[**get_listener_by_name**](ListenersApi.md#get_listener_by_name) | **GET** /api/v1/listeners/{name} | Get Listener
[**list_listeners**](ListenersApi.md#list_listeners) | **GET** /api/v1/listeners | List Listeners
[**update_dns_listener**](ListenersApi.md#update_dns_listener) | **PUT** /api/v1/listeners/dns/{name} | Update DNS Listener
[**update_external_c2_listener**](ListenersApi.md#update_external_c2_listener) | **PUT** /api/v1/listeners/externalC2/{name} | Update External C2 Listener
[**update_foreign_http_listener**](ListenersApi.md#update_foreign_http_listener) | **PUT** /api/v1/listeners/foreignHttp/{name} | Update Foreign HTTP Listener
[**update_foreign_https_listener**](ListenersApi.md#update_foreign_https_listener) | **PUT** /api/v1/listeners/foreignHttps/{name} | Update Foreign HTTPs Listener
[**update_http_listener**](ListenersApi.md#update_http_listener) | **PUT** /api/v1/listeners/http/{name} | Update HTTP Listener
[**update_https_listener**](ListenersApi.md#update_https_listener) | **PUT** /api/v1/listeners/https/{name} | Update HTTPS Listener
[**update_smb_listener**](ListenersApi.md#update_smb_listener) | **PUT** /api/v1/listeners/smb/{name} | Update SMB Listener
[**update_tcp_listener**](ListenersApi.md#update_tcp_listener) | **PUT** /api/v1/listeners/tcp/{name} | Update TCP Listener
[**update_user_defined_c2_listener**](ListenersApi.md#update_user_defined_c2_listener) | **PUT** /api/v1/listeners/userDefinedC2/{name} | Update UDC2 Listener


# **add_dns_listener**
> DnsListenerDto add_dns_listener(request_model)

Add DNS Listener

Add a new DNS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_dns_listener(
            request_model=cs_sdk_python.api_client.DnsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**DnsListenerDto**](DnsListenerDto.md)|  | 

### Return type

[**DnsListenerDto**](DnsListenerDto.md)

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

# **add_external_c2_listener**
> ExternalC2ListenerDto add_external_c2_listener(request_model)

Add External C2 Listener

Add a new External C2 listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_external_c2_listener(
            request_model=cs_sdk_python.api_client.ExternalC2ListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**ExternalC2ListenerDto**](ExternalC2ListenerDto.md)|  | 

### Return type

[**ExternalC2ListenerDto**](ExternalC2ListenerDto.md)

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

# **add_foreign_http_listener**
> ForeignHttpListenerDto add_foreign_http_listener(request_model)

Add Foreign HTTP Listener

Add a new Foreign HTTP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_foreign_http_listener(
            request_model=cs_sdk_python.api_client.ForeignHttpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**ForeignHttpListenerDto**](ForeignHttpListenerDto.md)|  | 

### Return type

[**ForeignHttpListenerDto**](ForeignHttpListenerDto.md)

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

# **add_foreign_https_listener**
> ForeignHttpsListenerDto add_foreign_https_listener(request_model)

Add Foreign HTTPS Listener

Add a new Foreign HTTPS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_foreign_https_listener(
            request_model=cs_sdk_python.api_client.ForeignHttpsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**ForeignHttpsListenerDto**](ForeignHttpsListenerDto.md)|  | 

### Return type

[**ForeignHttpsListenerDto**](ForeignHttpsListenerDto.md)

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

# **add_http_listener**
> HttpListenerDto add_http_listener(request_model)

Add HTTP Listener

Add a new HTTP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_http_listener(
            request_model=cs_sdk_python.api_client.HttpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**HttpListenerDto**](HttpListenerDto.md)|  | 

### Return type

[**HttpListenerDto**](HttpListenerDto.md)

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

# **add_https_listener**
> HttpsListenerDto add_https_listener(request_model)

Add HTTPS Listener

Add a new HTTPS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_https_listener(
            request_model=cs_sdk_python.api_client.HttpsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**HttpsListenerDto**](HttpsListenerDto.md)|  | 

### Return type

[**HttpsListenerDto**](HttpsListenerDto.md)

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

# **add_smb_listener**
> SmbListenerDto add_smb_listener(request_model)

Add SMB Listener

Add a new SMB listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_smb_listener(
            request_model=cs_sdk_python.api_client.SmbListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**SmbListenerDto**](SmbListenerDto.md)|  | 

### Return type

[**SmbListenerDto**](SmbListenerDto.md)

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

# **add_tcp_listener**
> TcpListenerDto add_tcp_listener(request_model)

Add TCP Listener

Add a new TCP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_tcp_listener(
            request_model=cs_sdk_python.api_client.TcpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**TcpListenerDto**](TcpListenerDto.md)|  | 

### Return type

[**TcpListenerDto**](TcpListenerDto.md)

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

# **add_user_defined_c2_listener**
> UserDefinedC2ListenerDto add_user_defined_c2_listener(request_model)

Add UDC2 Listener

Add a new User Defined C2 (UDC2) listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.add_user_defined_c2_listener(
            request_model=cs_sdk_python.api_client.UserDefinedC2ListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**UserDefinedC2ListenerDto**](UserDefinedC2ListenerDto.md)|  | 

### Return type

[**UserDefinedC2ListenerDto**](UserDefinedC2ListenerDto.md)

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

# **delete_listener**
> delete_listener(name)

Delete Listener

Delete a Listener.

Related CS Aggressor function: listener_delete()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        await api.delete_listener(
            name='name_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 

### Return type

void (empty response body)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **get_listener_by_name**
> object get_listener_by_name(name)

Get Listener

Get the information of a specific listener.

Related CS Aggressor function: listener_info()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.get_listener_by_name(
            name='name_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 

### Return type

**object**

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

# **list_listeners**
> List[ListenerBaseDto] list_listeners()

List Listeners

Lists all listeners.

Related CS Aggressor function: listeners_local()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.list_listeners()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ListenerBaseDto]**](ListenerBaseDto.md)

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

# **update_dns_listener**
> DnsListenerDto update_dns_listener(name, request_model)

Update DNS Listener

Modify the configuration of a DNS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_dns_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.DnsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**DnsListenerDto**](DnsListenerDto.md)|  | 

### Return type

[**DnsListenerDto**](DnsListenerDto.md)

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

# **update_external_c2_listener**
> ExternalC2ListenerDto update_external_c2_listener(name, request_model)

Update External C2 Listener

Modify the configuration of an External C2 listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_external_c2_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.ExternalC2ListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**ExternalC2ListenerDto**](ExternalC2ListenerDto.md)|  | 

### Return type

[**ExternalC2ListenerDto**](ExternalC2ListenerDto.md)

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

# **update_foreign_http_listener**
> ForeignHttpListenerDto update_foreign_http_listener(name, request_model)

Update Foreign HTTP Listener

Modify the configuration of a Foreign HTTP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_foreign_http_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.ForeignHttpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**ForeignHttpListenerDto**](ForeignHttpListenerDto.md)|  | 

### Return type

[**ForeignHttpListenerDto**](ForeignHttpListenerDto.md)

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

# **update_foreign_https_listener**
> ForeignHttpsListenerDto update_foreign_https_listener(name, request_model)

Update Foreign HTTPs Listener

Modify the configuration of a Foreign HTTPS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_foreign_https_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.ForeignHttpsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**ForeignHttpsListenerDto**](ForeignHttpsListenerDto.md)|  | 

### Return type

[**ForeignHttpsListenerDto**](ForeignHttpsListenerDto.md)

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

# **update_http_listener**
> HttpListenerDto update_http_listener(name, request_model)

Update HTTP Listener

Modify the configuration of an HTTP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_http_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.HttpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**HttpListenerDto**](HttpListenerDto.md)|  | 

### Return type

[**HttpListenerDto**](HttpListenerDto.md)

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

# **update_https_listener**
> HttpsListenerDto update_https_listener(name, request_model)

Update HTTPS Listener

Modify the configuration of an HTTPS listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_https_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.HttpsListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**HttpsListenerDto**](HttpsListenerDto.md)|  | 

### Return type

[**HttpsListenerDto**](HttpsListenerDto.md)

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

# **update_smb_listener**
> SmbListenerDto update_smb_listener(name, request_model)

Update SMB Listener

Modify the configuration of an SMB listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_smb_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.SmbListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**SmbListenerDto**](SmbListenerDto.md)|  | 

### Return type

[**SmbListenerDto**](SmbListenerDto.md)

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

# **update_tcp_listener**
> TcpListenerDto update_tcp_listener(name, request_model)

Update TCP Listener

Modify the configuration of a TCP listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_tcp_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.TcpListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**TcpListenerDto**](TcpListenerDto.md)|  | 

### Return type

[**TcpListenerDto**](TcpListenerDto.md)

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

# **update_user_defined_c2_listener**
> UserDefinedC2ListenerDto update_user_defined_c2_listener(name, request_model)

Update UDC2 Listener

Modify the configuration of a User Defined C2 (UDC2) listener.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ListenersApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ListenersApi(client)
        response = await api.update_user_defined_c2_listener(
            name='name_example',
            request_model=cs_sdk_python.api_client.UserDefinedC2ListenerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the listener | 
 **request_model** | [**UserDefinedC2ListenerDto**](UserDefinedC2ListenerDto.md)|  | 

### Return type

[**UserDefinedC2ListenerDto**](UserDefinedC2ListenerDto.md)

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

