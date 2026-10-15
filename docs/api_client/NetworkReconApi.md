# cs_sdk_python.api_client.NetworkReconApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_net_domain**](NetworkReconApi.md#execute_net_domain) | **POST** /api/v1/beacons/{bid}/execute/net/domain | Get Domain
[**inject_net_computers**](NetworkReconApi.md#inject_net_computers) | **POST** /api/v1/beacons/{bid}/inject/net/computers | List Specified Groups (Inject)
[**inject_net_dc_list**](NetworkReconApi.md#inject_net_dc_list) | **POST** /api/v1/beacons/{bid}/inject/net/dclist | List Domain Controllers (Inject)
[**inject_net_domain_controllers**](NetworkReconApi.md#inject_net_domain_controllers) | **POST** /api/v1/beacons/{bid}/inject/net/domainControllers | List Domain Controllers Hosts (Inject)
[**inject_net_domain_trusts**](NetworkReconApi.md#inject_net_domain_trusts) | **POST** /api/v1/beacons/{bid}/inject/net/domainTrusts | List Domain Trusts (Inject)
[**inject_net_group**](NetworkReconApi.md#inject_net_group) | **POST** /api/v1/beacons/{bid}/inject/net/group | List Domain Groups (Inject)
[**inject_net_local_group**](NetworkReconApi.md#inject_net_local_group) | **POST** /api/v1/beacons/{bid}/inject/net/localGroup | List Local Groups (Inject)
[**inject_net_logons**](NetworkReconApi.md#inject_net_logons) | **POST** /api/v1/beacons/{bid}/inject/net/logons | List Logged in Users (Inject)
[**inject_net_sessions**](NetworkReconApi.md#inject_net_sessions) | **POST** /api/v1/beacons/{bid}/inject/net/sessions | List Sessions (Inject)
[**inject_net_share**](NetworkReconApi.md#inject_net_share) | **POST** /api/v1/beacons/{bid}/inject/net/share | List Shares (Inject)
[**inject_net_time**](NetworkReconApi.md#inject_net_time) | **POST** /api/v1/beacons/{bid}/inject/net/time | Get System Time (Inject)
[**inject_net_user**](NetworkReconApi.md#inject_net_user) | **POST** /api/v1/beacons/{bid}/inject/net/user | List Users (Inject)
[**inject_net_user_detail**](NetworkReconApi.md#inject_net_user_detail) | **POST** /api/v1/beacons/{bid}/inject/net/user/detail | Get User (Inject)
[**inject_net_view**](NetworkReconApi.md#inject_net_view) | **POST** /api/v1/beacons/{bid}/inject/net/view | List Domain Hosts (Inject)
[**inject_port_scan**](NetworkReconApi.md#inject_port_scan) | **POST** /api/v1/beacons/{bid}/inject/portscan | Port Scan (Inject)
[**spawn_net_computers**](NetworkReconApi.md#spawn_net_computers) | **POST** /api/v1/beacons/{bid}/spawn/net/computers | List Specified Groups (Spawn)
[**spawn_net_dc_list**](NetworkReconApi.md#spawn_net_dc_list) | **POST** /api/v1/beacons/{bid}/spawn/net/dclist | List Domain Controllers (Spawn)
[**spawn_net_domain_controllers**](NetworkReconApi.md#spawn_net_domain_controllers) | **POST** /api/v1/beacons/{bid}/spawn/net/domainControllers | List Domain Controllers Hosts (Spawn)
[**spawn_net_domain_trusts**](NetworkReconApi.md#spawn_net_domain_trusts) | **POST** /api/v1/beacons/{bid}/spawn/net/domainTrusts | List Domain Trusts (Spawn)
[**spawn_net_group**](NetworkReconApi.md#spawn_net_group) | **POST** /api/v1/beacons/{bid}/spawn/net/group | List Domain Groups (Spawn)
[**spawn_net_local_group**](NetworkReconApi.md#spawn_net_local_group) | **POST** /api/v1/beacons/{bid}/spawn/net/localGroup | List Local Groups (Spawn)
[**spawn_net_logons**](NetworkReconApi.md#spawn_net_logons) | **POST** /api/v1/beacons/{bid}/spawn/net/logons | List Logged in Users (Spawn)
[**spawn_net_sessions**](NetworkReconApi.md#spawn_net_sessions) | **POST** /api/v1/beacons/{bid}/spawn/net/sessions | List Sessions (Spawn)
[**spawn_net_share**](NetworkReconApi.md#spawn_net_share) | **POST** /api/v1/beacons/{bid}/spawn/net/share | List Shares (Spawn)
[**spawn_net_time**](NetworkReconApi.md#spawn_net_time) | **POST** /api/v1/beacons/{bid}/spawn/net/time | Get System Time (Spawn)
[**spawn_net_user**](NetworkReconApi.md#spawn_net_user) | **POST** /api/v1/beacons/{bid}/spawn/net/user | List Users (Spawn)
[**spawn_net_user_detail**](NetworkReconApi.md#spawn_net_user_detail) | **POST** /api/v1/beacons/{bid}/spawn/net/user/detail | Get User (Spawn)
[**spawn_net_view**](NetworkReconApi.md#spawn_net_view) | **POST** /api/v1/beacons/{bid}/spawn/net/view | List Domain Hosts (Spawn)
[**spawn_port_scan**](NetworkReconApi.md#spawn_port_scan) | **POST** /api/v1/beacons/{bid}/spawn/portscan | Port Scan (Spawn)


# **execute_net_domain**
> AsyncCommandResponse execute_net_domain(bid)

Get Domain

Get active directory domain for current system.

Related CS Console Command: net domain

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.execute_net_domain(
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

# **inject_net_computers**
> AsyncCommandResponse inject_net_computers(bid, request_model)

List Specified Groups (Inject)

Inject the network and host enumeration DLL into the specified process to list hosts from the Domain Computers and Domain Controllers groups on the specified domain.

Related CS Console Command: net computers

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_computers(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetComputersInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetComputersInjectDto**](NetComputersInjectDto.md)|  | 

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

# **inject_net_dc_list**
> AsyncCommandResponse inject_net_dc_list(bid, request_model)

List Domain Controllers (Inject)

Inject the network and host enumeration DLL into the specified process to list domain controllers for the specified domain.

Related CS Console Command: net dclist

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_dc_list(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDcListInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDcListInjectDto**](NetDcListInjectDto.md)|  | 

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

# **inject_net_domain_controllers**
> AsyncCommandResponse inject_net_domain_controllers(bid, request_model)

List Domain Controllers Hosts (Inject)

Inject the network and host enumeration DLL into the specified process to list hosts from the Domain Controllers group on the specified domain.

Related CS Console Command: net domain_controllers

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_domain_controllers(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDomainControllersInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDomainControllersInjectDto**](NetDomainControllersInjectDto.md)|  | 

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

# **inject_net_domain_trusts**
> AsyncCommandResponse inject_net_domain_trusts(bid, request_model)

List Domain Trusts (Inject)

Inject the network and host enumeration DLL into the specified process to list domain trusts for the specified domain.

Related CS Console Command: net domain_trusts

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_domain_trusts(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDomainTrustsInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDomainTrustsInjectDto**](NetDomainTrustsInjectDto.md)|  | 

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

# **inject_net_group**
> AsyncCommandResponse inject_net_group(bid, request_model)

List Domain Groups (Inject)

Inject the network and host enumeration DLL into the specified process to enumerate groups on a domain controller.

Related CS Console Command: net group

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_group(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetGroupInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetGroupInjectDto**](NetGroupInjectDto.md)|  | 

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

# **inject_net_local_group**
> AsyncCommandResponse inject_net_local_group(bid, request_model)

List Local Groups (Inject)

Inject the network and host enumeration DLL into the specified process to enumerate local groups on a specific system.

Related CS Console Command: net localgroup

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_local_group(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetLocalGroupInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetLocalGroupInjectDto**](NetLocalGroupInjectDto.md)|  | 

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

# **inject_net_logons**
> AsyncCommandResponse inject_net_logons(bid, request_model)

List Logged in Users (Inject)

Inject the network and host enumeration DLL into the specified process to list users logged onto a target.

Related CS Console Command: net logons

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_logons(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetLogonsInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetLogonsInjectDto**](NetLogonsInjectDto.md)|  | 

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

# **inject_net_sessions**
> AsyncCommandResponse inject_net_sessions(bid, request_model)

List Sessions (Inject)

Inject the network and host enumeration DLL into the specified process to list sessions on a target.

Related CS Console Command: net sessions

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_sessions(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetSessionsInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetSessionsInjectDto**](NetSessionsInjectDto.md)|  | 

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

# **inject_net_share**
> AsyncCommandResponse inject_net_share(bid, request_model)

List Shares (Inject)

Inject the network and host enumeration DLL into the specified process to list shares on a target.

Related CS Console Command: net share

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_share(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetShareInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetShareInjectDto**](NetShareInjectDto.md)|  | 

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

# **inject_net_time**
> AsyncCommandResponse inject_net_time(bid, request_model)

Get System Time (Inject)

Inject the network and host enumeration DLL into the specified process to  show time for a target.

Related CS Console Command: net time

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_time(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetTimeInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetTimeInjectDto**](NetTimeInjectDto.md)|  | 

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

# **inject_net_user**
> AsyncCommandResponse inject_net_user(bid, request_model)

List Users (Inject)

Inject the network and host enumeration dll into the specified process to list users on a system.

Related CS Console Command: net user

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_user(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetUserInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetUserInjectDto**](NetUserInjectDto.md)|  | 

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

# **inject_net_user_detail**
> AsyncCommandResponse inject_net_user_detail(bid, request_model)

Get User (Inject)

Inject the network and host enumeration DLL into the specified process to get information about a user.

Related CS Console Command: net user

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_user_detail(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetUserDetailInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetUserDetailInjectDto**](NetUserDetailInjectDto.md)|  | 

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

# **inject_net_view**
> AsyncCommandResponse inject_net_view(bid, request_model)

List Domain Hosts (Inject)

Inject the network and host enumeration DLL into the specified process to list hosts on a domain.

Related CS Console Command: net view

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_net_view(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetViewInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetViewInjectDto**](NetViewInjectDto.md)|  | 

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

# **inject_port_scan**
> AsyncCommandResponse inject_port_scan(bid, request_model)

Port Scan (Inject)

Inject a portscan DLL into the specified process to run a portscan against the specified hosts.

Related CS Console Command: portscan

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.inject_port_scan(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PortScanInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PortScanInjectDto**](PortScanInjectDto.md)|  | 

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

# **spawn_net_computers**
> AsyncCommandResponse spawn_net_computers(bid, request_model)

List Specified Groups (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list hosts from the Domain Computers and Domain Controllers groups on the specified domain.

Related CS Console Command: net computers

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_computers(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetComputersDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetComputersDto**](NetComputersDto.md)|  | 

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

# **spawn_net_dc_list**
> AsyncCommandResponse spawn_net_dc_list(bid, request_model)

List Domain Controllers (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list domain controllers for the specified domain.

Related CS Console Command: net dclist

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_dc_list(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDcListDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDcListDto**](NetDcListDto.md)|  | 

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

# **spawn_net_domain_controllers**
> AsyncCommandResponse spawn_net_domain_controllers(bid, request_model)

List Domain Controllers Hosts (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list hosts from the Domain Controllers group on the specified domain.

Related CS Console Command: net domain_controllers

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_domain_controllers(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDomainControllersDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDomainControllersDto**](NetDomainControllersDto.md)|  | 

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

# **spawn_net_domain_trusts**
> AsyncCommandResponse spawn_net_domain_trusts(bid, request_model)

List Domain Trusts (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list domain trusts for the specified domain.

Related CS Console Command: net domain_trusts

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_domain_trusts(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetDomainTrustsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetDomainTrustsDto**](NetDomainTrustsDto.md)|  | 

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

# **spawn_net_group**
> AsyncCommandResponse spawn_net_group(bid, request_model)

List Domain Groups (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to enumerate groups on a domain controller.

Related CS Console Command: net group

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_group(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetGroupDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetGroupDto**](NetGroupDto.md)|  | 

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

# **spawn_net_local_group**
> AsyncCommandResponse spawn_net_local_group(bid, request_model)

List Local Groups (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to enumerate local groups on a specific system.

Related CS Console Command: net localgroup

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_local_group(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetLocalGroupDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetLocalGroupDto**](NetLocalGroupDto.md)|  | 

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

# **spawn_net_logons**
> AsyncCommandResponse spawn_net_logons(bid, request_model)

List Logged in Users (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list users logged onto a target.

Related CS Console Command: net logons

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_logons(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetLogonsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetLogonsDto**](NetLogonsDto.md)|  | 

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

# **spawn_net_sessions**
> AsyncCommandResponse spawn_net_sessions(bid, request_model)

List Sessions (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list sessions on a target.

Related CS Console Command: net sessions

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_sessions(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetSessionsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetSessionsDto**](NetSessionsDto.md)|  | 

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

# **spawn_net_share**
> AsyncCommandResponse spawn_net_share(bid, request_model)

List Shares (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list shares on a target.

Related CS Console Command: net share

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_share(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetShareDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetShareDto**](NetShareDto.md)|  | 

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

# **spawn_net_time**
> AsyncCommandResponse spawn_net_time(bid, request_model)

Get System Time (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to show time for a target.

Related CS Console Command: net time

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_time(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetTimeDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetTimeDto**](NetTimeDto.md)|  | 

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

# **spawn_net_user**
> AsyncCommandResponse spawn_net_user(bid, request_model)

List Users (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list users on a system.

Related CS Console Command: net user

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_user(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetUserDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetUserDto**](NetUserDto.md)|  | 

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

# **spawn_net_user_detail**
> AsyncCommandResponse spawn_net_user_detail(bid, request_model)

Get User (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to get information about a user.

Related CS Console Command: net user

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_user_detail(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetUserDetailDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetUserDetailDto**](NetUserDetailDto.md)|  | 

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

# **spawn_net_view**
> AsyncCommandResponse spawn_net_view(bid, request_model)

List Domain Hosts (Spawn)

Spawn a temporary process and inject the network and host enumeration DLL into it to list hosts on a domain.

Related CS Console Command: net view

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_net_view(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.NetViewDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**NetViewDto**](NetViewDto.md)|  | 

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

# **spawn_port_scan**
> AsyncCommandResponse spawn_port_scan(bid, request_model)

Port Scan (Spawn)

Spawn a temporary process, inject a portscan DLL into it and to run a portscan against the specified hosts. [targets] is a comma separated list of hosts to scan.

Related CS Console Command: portscan

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import NetworkReconApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = NetworkReconApi(client)
        response = await api.spawn_port_scan(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PortScanSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PortScanSpawnDto**](PortScanSpawnDto.md)|  | 

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

