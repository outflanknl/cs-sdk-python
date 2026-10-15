# cs_sdk_python.api_client.ConsoleCommandApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_console_command**](ConsoleCommandApi.md#execute_console_command) | **POST** /api/v1/beacons/{bid}/consoleCommand | Run Command
[**get_command_help**](ConsoleCommandApi.md#get_command_help) | **GET** /api/v1/beacons/{bid}/help/{command} | Command Help
[**list_command_help**](ConsoleCommandApi.md#list_command_help) | **GET** /api/v1/beacons/{bid}/help | Help


# **execute_console_command**
> AsyncCommandResponse execute_console_command(bid, request_model)

Run Command

Execute a console command on a Beacon. 

Can be used: 
 - to run commands and syntax as if on the normal console;
 - to call server side aliases.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ConsoleCommandApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ConsoleCommandApi(client)
        response = await api.execute_console_command(
            bid='bid_example',
            request_model={"command":"ps"},
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**CommandDto**](CommandDto.md)| Command to execute | 

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

# **get_command_help**
> CommandHelpInfoDto get_command_help(bid, command)

Command Help

Get the help of a specific command that is available as a consoleCommand.

Related CS Console Command: help

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ConsoleCommandApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ConsoleCommandApi(client)
        response = await api.get_command_help(
            bid='bid_example',
            command='command_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **command** | **str**| Command name | 

### Return type

[**CommandHelpInfoDto**](CommandHelpInfoDto.md)

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

# **list_command_help**
> List[CommandHelpInfoDto] list_command_help(bid)

Help

List help for all commands available on the consoleCommand route (including possible server side aliases).

Related CS Console Command: help

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ConsoleCommandApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ConsoleCommandApi(client)
        response = await api.list_command_help(
            bid='bid_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 

### Return type

[**List[CommandHelpInfoDto]**](CommandHelpInfoDto.md)

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

