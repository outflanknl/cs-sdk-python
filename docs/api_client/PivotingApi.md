# cs_sdk_python.api_client.PivotingApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_link_smb**](PivotingApi.md#execute_link_smb) | **POST** /api/v1/beacons/{bid}/execute/link/smb | Connect to SMB Beacon
[**execute_link_tcp**](PivotingApi.md#execute_link_tcp) | **POST** /api/v1/beacons/{bid}/execute/link/tcp | Connect to TCP Beacon
[**execute_unlink**](PivotingApi.md#execute_unlink) | **POST** /api/v1/beacons/{bid}/execute/unlink | Disconnect Pivot Beacon
[**inject_ssh**](PivotingApi.md#inject_ssh) | **POST** /api/v1/beacons/{bid}/inject/ssh | Connect via SSH using User/Password (Inject)
[**inject_ssh_key**](PivotingApi.md#inject_ssh_key) | **POST** /api/v1/beacons/{bid}/inject/sshKey | Connect via SSH using Key (Inject)
[**spawn_ssh**](PivotingApi.md#spawn_ssh) | **POST** /api/v1/beacons/{bid}/spawn/ssh | Connect via SSH using User/Password (Spawn)
[**spawn_ssh_key**](PivotingApi.md#spawn_ssh_key) | **POST** /api/v1/beacons/{bid}/spawn/sshKey | Connect via SSH using Key (Spawn)


# **execute_link_smb**
> AsyncCommandResponse execute_link_smb(bid, request_model)

Connect to SMB Beacon

Connect to an SMB Beacon and re-establish control of it.

Related CS Console Command: link

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.execute_link_smb(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.LinkDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**LinkDto**](LinkDto.md)|  | 

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

# **execute_link_tcp**
> AsyncCommandResponse execute_link_tcp(bid, request_model)

Connect to TCP Beacon

Connect to a TCP Beacon and re-establish control of it.

Related CS Console Command: connect

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.execute_link_tcp(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ConnectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**ConnectDto**](ConnectDto.md)|  | 

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

# **execute_unlink**
> AsyncCommandResponse execute_unlink(bid, request_model)

Disconnect Pivot Beacon

Disconnect from a named pipe or TCP Beacon.

Related CS Console Command: unlink

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.execute_unlink(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.UnlinkDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**UnlinkDto**](UnlinkDto.md)|  | 

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

# **inject_ssh**
> AsyncCommandResponse inject_ssh(bid, request_model)

Connect via SSH using User/Password (Inject)

Inject into the specified process to run an SSH client and attempt to login to the specified target.

Related CS Console Command: ssh-key

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.inject_ssh(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SshInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SshInjectDto**](SshInjectDto.md)|  | 

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

# **inject_ssh_key**
> AsyncCommandResponse inject_ssh_key(bid, request_model)

Connect via SSH using Key (Inject)

Inject into the specified process to run an SSH client and attempt to login to the specified target using an SSH key. The key file needs to be in the PEM format.  If the file is not in the PEM format then make a copy of the file and convert the copy with the following command: /usr/bin/ssh-keygen -f [/path/to/copy] -e -m pem -p.

Related CS Console Command: ssh-key

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.inject_ssh_key(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SshKeyInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SshKeyInjectDto**](SshKeyInjectDto.md)|  | 

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

# **spawn_ssh**
> AsyncCommandResponse spawn_ssh(bid, request_model)

Connect via SSH using User/Password (Spawn)

Spawn a temporary process to run an SSH client and attempt to login to the specified target.

Related CS Console Command: ssh-key

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.spawn_ssh(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SshSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SshSpawnDto**](SshSpawnDto.md)|  | 

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

# **spawn_ssh_key**
> AsyncCommandResponse spawn_ssh_key(bid, request_model)

Connect via SSH using Key (Spawn)

Spawn a temporary process to run an SSH client and attempt to login to the specified target using an SSH key. The key file needs to be in the PEM format.  If the file is not in the PEM format then make a copy of the file and convert the copy with the following command: /usr/bin/ssh-keygen -f [/path/to/copy] -e -m pem -p.

Related CS Console Command: ssh-key

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PivotingApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PivotingApi(client)
        response = await api.spawn_ssh_key(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SshKeySpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SshKeySpawnDto**](SshKeySpawnDto.md)|  | 

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

