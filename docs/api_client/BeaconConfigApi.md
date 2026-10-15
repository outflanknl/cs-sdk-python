# cs_sdk_python.api_client.BeaconConfigApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_host_callback_information**](BeaconConfigApi.md#add_host_callback_information) | **POST** /api/v1/beacons/{bid}/state/c2/host | Add Host to Beacon Callback hosts list
[**add_spoofed_arguments**](BeaconConfigApi.md#add_spoofed_arguments) | **POST** /api/v1/beacons/{bid}/state/spoofedArguments | Add Command Line Argument Spoofing 
[**disable_beacon_gate**](BeaconConfigApi.md#disable_beacon_gate) | **POST** /api/v1/beacons/{bid}/state/beaconGate/disable | Disable Beacon Gate
[**disable_block_dlls**](BeaconConfigApi.md#disable_block_dlls) | **POST** /api/v1/beacons/{bid}/state/blockdlls/disable | Disable Block Dlls
[**disable_failover_notification**](BeaconConfigApi.md#disable_failover_notification) | **POST** /api/v1/beacons/{bid}/state/c2/failoverNotification/disable | Disable Failover Notification
[**enable_beacon_gate**](BeaconConfigApi.md#enable_beacon_gate) | **POST** /api/v1/beacons/{bid}/state/beaconGate/enable | Enable Beacon Gate
[**enable_block_dlls**](BeaconConfigApi.md#enable_block_dlls) | **POST** /api/v1/beacons/{bid}/state/blockdlls/enable | Enable Block Dlls
[**enable_failover_notification**](BeaconConfigApi.md#enable_failover_notification) | **POST** /api/v1/beacons/{bid}/state/c2/failoverNotification/enable | Enable Failover Notification
[**execute_beacon_info**](BeaconConfigApi.md#execute_beacon_info) | **POST** /api/v1/beacons/{bid}/execute/beaconInfo | Get Beacon Info
[**get_current_failover_notification_setting**](BeaconConfigApi.md#get_current_failover_notification_setting) | **GET** /api/v1/beacons/{bid}/state/c2/failoverNotification | Get Failover Notification config
[**get_host_callback_information**](BeaconConfigApi.md#get_host_callback_information) | **GET** /api/v1/beacons/{bid}/state/c2/host | Get Beacon Callback Information
[**get_syscall_method**](BeaconConfigApi.md#get_syscall_method) | **GET** /api/v1/beacons/{bid}/state/syscallMethod | Get Syscall Method
[**hold_host_callback**](BeaconConfigApi.md#hold_host_callback) | **POST** /api/v1/beacons/{bid}/state/c2/host/hold | Hold Host
[**list_host_profiles**](BeaconConfigApi.md#list_host_profiles) | **GET** /api/v1/beacons/{bid}/state/c2/host/profiles | List Host Profiles
[**list_spoofed_arguments**](BeaconConfigApi.md#list_spoofed_arguments) | **GET** /api/v1/beacons/{bid}/state/spoofedArguments | List Argue / Command Line Argument Spoofing 
[**release_host_profile**](BeaconConfigApi.md#release_host_profile) | **POST** /api/v1/beacons/{bid}/state/c2/host/release | Release Host
[**remove_host_callback**](BeaconConfigApi.md#remove_host_callback) | **DELETE** /api/v1/beacons/{bid}/state/c2/host | Delete Host
[**remove_spoofed_arguments**](BeaconConfigApi.md#remove_spoofed_arguments) | **DELETE** /api/v1/beacons/{bid}/state/spoofedArguments | Remove Argument Spoofing Configuration
[**reset_callback_host**](BeaconConfigApi.md#reset_callback_host) | **POST** /api/v1/beacons/{bid}/state/c2/host/reset | Reset Hosts Stats
[**set_dns_mode**](BeaconConfigApi.md#set_dns_mode) | **POST** /api/v1/beacons/{bid}/state/dnsMode | Set DNS Beacon Mode
[**set_ppid**](BeaconConfigApi.md#set_ppid) | **POST** /api/v1/beacons/{bid}/state/ppid | Set Initial Beacon PID
[**set_sleep_time**](BeaconConfigApi.md#set_sleep_time) | **POST** /api/v1/beacons/{bid}/state/sleepTime | Set Sleep
[**set_spawn_to**](BeaconConfigApi.md#set_spawn_to) | **POST** /api/v1/beacons/{bid}/state/spawnto | Set executable that is used when spawning
[**set_syscall_method**](BeaconConfigApi.md#set_syscall_method) | **POST** /api/v1/beacons/{bid}/state/syscallMethod | Set Syscall Method
[**unset_ppid**](BeaconConfigApi.md#unset_ppid) | **DELETE** /api/v1/beacons/{bid}/state/ppid | Reset the specified parent PID
[**unset_spawn_to**](BeaconConfigApi.md#unset_spawn_to) | **DELETE** /api/v1/beacons/{bid}/state/spawnto | Reset the executable that is used when spawning to default
[**update_host_callback_info**](BeaconConfigApi.md#update_host_callback_info) | **PUT** /api/v1/beacons/{bid}/state/c2/host | Update Host in Beacon Callback hosts list


# **add_host_callback_information**
> AsyncCommandResponse add_host_callback_information(bid, request_model)

Add Host to Beacon Callback hosts list

Add one or more hosts/uris to the Beacons callback host list.

Related CS Console Command: beacon_config

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.add_host_callback_information(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackAddDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackAddDto**](HostCallbackAddDto.md)|  | 

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

# **add_spoofed_arguments**
> AsyncCommandResponse add_spoofed_arguments(bid, request_model)

Add Command Line Argument Spoofing 

Add Command Line Argument Spoofing entry.

Related CS Console Command: argue add

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.add_spoofed_arguments(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpoofedArgumentsAddDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SpoofedArgumentsAddDto**](SpoofedArgumentsAddDto.md)|  | 

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

# **disable_beacon_gate**
> AsyncCommandResponse disable_beacon_gate(bid)

Disable Beacon Gate

Disable the Beacon Gate functionality at runtime.

Related CS Console Command: beacon_gate disable

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.disable_beacon_gate(
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

# **disable_block_dlls**
> AsyncCommandResponse disable_block_dlls(bid)

Disable Block Dlls

Disable use of the 'BlockDLL feature'. With BlockDLL, a Windows binary signature policy is used that blocks non-Microsoft DLLs from loading into the child process.
This feature requires Windows 10/Windows Server 2012 or later.

Related CS Console Command: blockdlls stop

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.disable_block_dlls(
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

# **disable_failover_notification**
> AsyncCommandResponse disable_failover_notification(bid)

Disable Failover Notification

Disable notifications from a Beacon [HTTP|DNS] when host rotation occurs from failover events.

Related CS Console Command: beacon_config failover_notification

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.disable_failover_notification(
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

# **enable_beacon_gate**
> AsyncCommandResponse enable_beacon_gate(bid)

Enable Beacon Gate

Enable the Beacon Gate functionality as specified in the profile at runtime.

Related CS Console Command: beacon_gate enable

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.enable_beacon_gate(
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

# **enable_block_dlls**
> AsyncCommandResponse enable_block_dlls(bid)

Enable Block Dlls

Enable use of the BlockDLL feature. With BlockDLL, a Windows binary signature policy is used that blocks non-Microsoft DLLs from loading into the child process.
This feature requires Windows 10/Windows Server 2012 or later.

Related CS Console Command: blockdlls start

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.enable_block_dlls(
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

# **enable_failover_notification**
> AsyncCommandResponse enable_failover_notification(bid)

Enable Failover Notification

Enable notifications from a Beacon [HTTP|DNS] when host rotation occurs from failover events.

Related CS Console Command: beacon_config failover_notification

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.enable_failover_notification(
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

# **execute_beacon_info**
> AsyncCommandResponse execute_beacon_info(bid)

Get Beacon Info

Prints detailed information about the Beacon's runtime state such as its base address, allocated memory regions, allocated section details, heap records and sleep mask information.
Useful for inspecting the current memory layout of Beacon.

Related CS Console Command: beacon_info

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.execute_beacon_info(
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

# **get_current_failover_notification_setting**
> AsyncCommandResponse get_current_failover_notification_setting(bid)

Get Failover Notification config

Get the current failover notification setting from a Beacon [HTTP|DNS].

Related CS Console Command: beacon_config failover_notification

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.get_current_failover_notification_setting(
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

# **get_host_callback_information**
> AsyncCommandResponse get_host_callback_information(bid)

Get Beacon Callback Information

Retrieve host callback information from a Beacon.

Related CS Console Command: beacon_config

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.get_host_callback_information(
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

# **get_syscall_method**
> AsyncCommandResponse get_syscall_method(bid)

Get Syscall Method

Query the current syscall method.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.get_syscall_method(
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

# **hold_host_callback**
> AsyncCommandResponse hold_host_callback(bid, request_model)

Hold Host

Hold one or more hosts in the callback host list [Random and Round-Robin rotation only].

Related CS Console Command: beacon_config hold

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.hold_host_callback(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackHoldDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackHoldDto**](HostCallbackHoldDto.md)|  | 

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

# **list_host_profiles**
> AsyncCommandResponse list_host_profiles(bid)

List Host Profiles

List the host profiles defined in the Beacon from Malleable C2 definition.

Related CS Console Command: beacon_config profiles

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.list_host_profiles(
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

# **list_spoofed_arguments**
> AsyncCommandResponse list_spoofed_arguments(bid)

List Argue / Command Line Argument Spoofing 

List argument spoofing configuration.

Related CS Console Command: argue list

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.list_spoofed_arguments(
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

# **release_host_profile**
> AsyncCommandResponse release_host_profile(bid, request_model)

Release Host

Release a host in the callback host list [Random and Round-Robin rotation only]. Multiple hosts can be used by way of a comma-separated list.

Related CS Console Command: beacon_config release

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.release_host_profile(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackReleaseDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackReleaseDto**](HostCallbackReleaseDto.md)|  | 

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

# **remove_host_callback**
> AsyncCommandResponse remove_host_callback(bid, request_model)

Delete Host

Remove a host from the host list.

Related CS Console Command: beacon_config

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.remove_host_callback(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackRemoveDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackRemoveDto**](HostCallbackRemoveDto.md)|  | 

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

# **remove_spoofed_arguments**
> AsyncCommandResponse remove_spoofed_arguments(bid, request_model)

Remove Argument Spoofing Configuration

Remove Command Line Argument Spoofing entry.

Related CS Console Command: argue remove

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.remove_spoofed_arguments(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpoofedArgumentsRemoveDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SpoofedArgumentsRemoveDto**](SpoofedArgumentsRemoveDto.md)|  | 

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

# **reset_callback_host**
> AsyncCommandResponse reset_callback_host(bid, request_model)

Reset Hosts Stats

Reset the status and/or statistics for callback hosts.

Related CS Console Command: beacon_config reset

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.reset_callback_host(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackResetDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackResetDto**](HostCallbackResetDto.md)|  | 

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

# **set_dns_mode**
> AsyncCommandResponse set_dns_mode(bid, request_model)

Set DNS Beacon Mode

Sets Beacon's mode to exchange data with the end-user. 
 - Mode dns is the DNS A record data channel. 
 - Mode dns6 is the DNS AAAA record channel. 
 - Mode dns-txt is the DNS TXT record data channel. 

The default is the DNS TXT record data channel.
This only has an effect on a DNS Beacon.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.set_dns_mode(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DnsModeDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**DnsModeDto**](DnsModeDto.md)|  | 

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

# **set_ppid**
> AsyncCommandResponse set_ppid(bid, request_model)

Set Initial Beacon PID

Use specified PID as parent for processes Beacon launches.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.set_ppid(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PpidDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PpidDto**](PpidDto.md)|  | 

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

# **set_sleep_time**
> AsyncCommandResponse set_sleep_time(bid, request_model)

Set Sleep

Change the communication interval for Beacon calls home.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.set_sleep_time(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SleepDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SleepDto**](SleepDto.md)|  | 

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

# **set_spawn_to**
> AsyncCommandResponse set_spawn_to(bid, request_model)

Set executable that is used when spawning

Sets the executable Beacon spawns x86 and x64 shellcode into.
You must specify a full-path. Environment variables are OK (e.g., %windir%\sysnative\rundll32.exe).
Do not reference %windir%\system32\ directly. This path is different depending on whether or not Beacon is x86 or x64. Use %windir%\sysnative\ and %windir%\syswow64\ instead.
Beacon will map %windir%\syswow64\ to system32 when WOW64 is not present.

Related CS Console Command: spawnto

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.set_spawn_to(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpawnToDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SpawnToDto**](SpawnToDto.md)|  | 

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

# **set_syscall_method**
> AsyncCommandResponse set_syscall_method(bid, request_model)

Set Syscall Method

Change the syscall method at runtime.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.set_syscall_method(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SyscallMethodDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SyscallMethodDto**](SyscallMethodDto.md)|  | 

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

# **unset_ppid**
> AsyncCommandResponse unset_ppid(bid)

Reset the specified parent PID

Reset the specified parent PID.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.unset_ppid(
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

# **unset_spawn_to**
> AsyncCommandResponse unset_spawn_to(bid)

Reset the executable that is used when spawning to default

Resets the executable Beacon spawns x86 and x64 shellcode into to the value defined in the Malleable profile.

Related CS Console Command: spawnto

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.unset_spawn_to(
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

# **update_host_callback_info**
> AsyncCommandResponse update_host_callback_info(bid, request_model)

Update Host in Beacon Callback hosts list

Change the host/uri of one or more existing hosts/uris in the host list.

Related CS Console Command: beacon_config

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import BeaconConfigApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = BeaconConfigApi(client)
        response = await api.update_host_callback_info(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HostCallbackUpdateDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HostCallbackUpdateDto**](HostCallbackUpdateDto.md)|  | 

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

