# cs_sdk_python.api_client.ProcessAndExecutionApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevate_command**](ProcessAndExecutionApi.md#elevate_command) | **POST** /api/v1/beacons/{bid}/elevate/command | Run a Command elevated (runasadmin)
[**execute_beacon_interpreter_lint**](ProcessAndExecutionApi.md#execute_beacon_interpreter_lint) | **POST** /api/v1/beacons/{bid}/execute/interpreter/lint | Lint Beacon Interpreter Script
[**execute_beacon_interpreter_pack**](ProcessAndExecutionApi.md#execute_beacon_interpreter_pack) | **POST** /api/v1/beacons/{bid}/execute/interpreter/pack | Run Beacon Interpreter Script With Packed Arguments
[**execute_beacon_interpreter_packed**](ProcessAndExecutionApi.md#execute_beacon_interpreter_packed) | **POST** /api/v1/beacons/{bid}/execute/interpreter/packed | Run Beacon Interpreter Script (Packed Arguments)
[**execute_beacon_interpreter_string**](ProcessAndExecutionApi.md#execute_beacon_interpreter_string) | **POST** /api/v1/beacons/{bid}/execute/interpreter/string | Run Beacon Interpreter Script With Optional String Argument
[**execute_bof_packed_arg**](ProcessAndExecutionApi.md#execute_bof_packed_arg) | **POST** /api/v1/beacons/{bid}/execute/bof/packed | Run BOF with Packed Arguments
[**execute_bof_string_arg**](ProcessAndExecutionApi.md#execute_bof_string_arg) | **POST** /api/v1/beacons/{bid}/execute/bof/string | Run BOF
[**execute_bofpe_packed_arg**](ProcessAndExecutionApi.md#execute_bofpe_packed_arg) | **POST** /api/v1/beacons/{bid}/execute/bof-pe/packed | Run BOF-PE with Packed Arguments
[**execute_bofpe_string_arg**](ProcessAndExecutionApi.md#execute_bofpe_string_arg) | **POST** /api/v1/beacons/{bid}/execute/bof-pe/string | Run BOF-PE
[**execute_bofpeto_pack_args**](ProcessAndExecutionApi.md#execute_bofpeto_pack_args) | **POST** /api/v1/beacons/{bid}/execute/bof-pe/pack | Pack Arguments and Run BOF-PE
[**execute_bofto_pack_args**](ProcessAndExecutionApi.md#execute_bofto_pack_args) | **POST** /api/v1/beacons/{bid}/execute/bof/pack | Pack Arguments and Run BOF
[**execute_exit**](ProcessAndExecutionApi.md#execute_exit) | **POST** /api/v1/beacons/{bid}/execute/exit | Exit
[**execute_get_privs**](ProcessAndExecutionApi.md#execute_get_privs) | **POST** /api/v1/beacons/{bid}/execute/getPrivs | Enable all available privileges
[**execute_get_system**](ProcessAndExecutionApi.md#execute_get_system) | **POST** /api/v1/beacons/{bid}/execute/getSystem | Attempt to obtain System Privileges
[**execute_get_uid**](ProcessAndExecutionApi.md#execute_get_uid) | **POST** /api/v1/beacons/{bid}/execute/getUid | Get current User ID
[**execute_kill_process**](ProcessAndExecutionApi.md#execute_kill_process) | **POST** /api/v1/beacons/{bid}/execute/killProcess | Kill Process
[**execute_power_shell_import**](ProcessAndExecutionApi.md#execute_power_shell_import) | **POST** /api/v1/beacons/{bid}/execute/powershell/import | Import Powershell Script
[**execute_ps**](ProcessAndExecutionApi.md#execute_ps) | **POST** /api/v1/beacons/{bid}/execute/ps | List Process information
[**execute_set_env**](ProcessAndExecutionApi.md#execute_set_env) | **POST** /api/v1/beacons/{bid}/execute/setenv | Set Environment variable
[**inject_beacon**](ProcessAndExecutionApi.md#inject_beacon) | **POST** /api/v1/beacons/{bid}/inject/beacon | Execute Beacon Shellcode (Inject)
[**inject_dll**](ProcessAndExecutionApi.md#inject_dll) | **POST** /api/v1/beacons/{bid}/inject/dll | Load DLL via reflective DLL loading (Inject)
[**inject_load_dll**](ProcessAndExecutionApi.md#inject_load_dll) | **POST** /api/v1/beacons/{bid}/inject/loadDll | Load Library from disk (Inject)
[**inject_pth**](ProcessAndExecutionApi.md#inject_pth) | **POST** /api/v1/beacons/{bid}/inject/pth | Pass-the-Hash (Inject)
[**inject_shellcode**](ProcessAndExecutionApi.md#inject_shellcode) | **POST** /api/v1/beacons/{bid}/inject/shellcode | Execute Shellcode (Inject)
[**inject_unmanaged_power_shell**](ProcessAndExecutionApi.md#inject_unmanaged_power_shell) | **POST** /api/v1/beacons/{bid}/inject/powershell/unmanaged | Execute unmanaged Powershell  / psinject (Inject)
[**list_elevate_command_methods**](ProcessAndExecutionApi.md#list_elevate_command_methods) | **GET** /api/v1/beacons/{bid}/elevate/command | List Command Privilege Elevators
[**list_remote_execute_beacon_methods**](ProcessAndExecutionApi.md#list_remote_execute_beacon_methods) | **GET** /api/v1/beacons/{bid}/remoteExec/beacon | List Remote Beacon Execution methods
[**list_remote_execution_command_methods**](ProcessAndExecutionApi.md#list_remote_execution_command_methods) | **GET** /api/v1/beacons/{bid}/remoteExec/command | List Remote Command Execution methods
[**remote_execute_beacon**](ProcessAndExecutionApi.md#remote_execute_beacon) | **POST** /api/v1/beacons/{bid}/remoteExec/beacon | Remote Beacon Execution (jump)
[**remote_execute_command**](ProcessAndExecutionApi.md#remote_execute_command) | **POST** /api/v1/beacons/{bid}/remoteExec/command | Remote Command Execution (remote-exec)
[**spawn_beacon**](ProcessAndExecutionApi.md#spawn_beacon) | **POST** /api/v1/beacons/{bid}/spawn/beacon | Execute Beacon Shellcode (Spawn)
[**spawn_beacon_as_user**](ProcessAndExecutionApi.md#spawn_beacon_as_user) | **POST** /api/v1/beacons/{bid}/spawn/beacon/asUser | Execute Beacon Shellcode as User (Spawn)
[**spawn_beacon_under**](ProcessAndExecutionApi.md#spawn_beacon_under) | **POST** /api/v1/beacons/{bid}/spawn/beacon/under | Execute Beacon Shellcode under parentPID (Spawn)
[**spawn_dot_net_assembly**](ProcessAndExecutionApi.md#spawn_dot_net_assembly) | **POST** /api/v1/beacons/{bid}/spawn/dotnetAssembly | Execute .NET assembly  (Spawn)
[**spawn_power_shell**](ProcessAndExecutionApi.md#spawn_power_shell) | **POST** /api/v1/beacons/{bid}/spawn/powershell | Execute Managed Powershell (Spawn)
[**spawn_pth**](ProcessAndExecutionApi.md#spawn_pth) | **POST** /api/v1/beacons/{bid}/spawn/pth | Pass-the-Hash (Spawn)
[**spawn_run_command**](ProcessAndExecutionApi.md#spawn_run_command) | **POST** /api/v1/beacons/{bid}/spawn/command/run | Run (Spawn)
[**spawn_run_command_as**](ProcessAndExecutionApi.md#spawn_run_command_as) | **POST** /api/v1/beacons/{bid}/spawn/command/runAs | Run As (Spawn)
[**spawn_run_command_under**](ProcessAndExecutionApi.md#spawn_run_command_under) | **POST** /api/v1/beacons/{bid}/spawn/command/runUnder | Run under parentPID (Spawn)
[**spawn_shell_command**](ProcessAndExecutionApi.md#spawn_shell_command) | **POST** /api/v1/beacons/{bid}/spawn/command/shell | Run Shell Command (Spawn)
[**spawn_shellcode**](ProcessAndExecutionApi.md#spawn_shellcode) | **POST** /api/v1/beacons/{bid}/spawn/shellcode | Execute Shellcode (Spawn)
[**spawn_unmanaged_power_shell**](ProcessAndExecutionApi.md#spawn_unmanaged_power_shell) | **POST** /api/v1/beacons/{bid}/spawn/powershell/unmanaged | Execute unmanaged Powershell  / powerpick (Spawn)


# **elevate_command**
> AsyncCommandResponse elevate_command(bid, request_model)

Run a Command elevated (runasadmin)

Attempt to execute the command in an elevated context using the specified privilege elevation technique. Depending on technique, proceses could be spawned or injected.

Related CS Console Command: runasadmin

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.elevate_command(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RunAsAdminDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RunAsAdminDto**](RunAsAdminDto.md)|  | 

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

# **execute_beacon_interpreter_lint**
> AsyncCommandResponse execute_beacon_interpreter_lint(bid, request_model)

Lint Beacon Interpreter Script

Compile (lint) a C script in Beacon Interpreter without execution.

Related CS Console Command: beacon-interpreter-lint

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_beacon_interpreter_lint(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.BeaconInterpreterLintDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**BeaconInterpreterLintDto**](BeaconInterpreterLintDto.md)|  | 

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

# **execute_beacon_interpreter_pack**
> AsyncCommandResponse execute_beacon_interpreter_pack(bid, request_model)

Run Beacon Interpreter Script With Packed Arguments

Pack typed arguments and execute a C script in Beacon Interpreter.

Related CS Aggressor functions: bbeacon_interpreter

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_beacon_interpreter_pack(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.BeaconInterpreterPackDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**BeaconInterpreterPackDto**](BeaconInterpreterPackDto.md)|  | 

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

# **execute_beacon_interpreter_packed**
> AsyncCommandResponse execute_beacon_interpreter_packed(bid, request_model)

Run Beacon Interpreter Script (Packed Arguments)

Execute a C script in Beacon Interpreter using pre-packed Base64 arguments.

Related CS Aggressor function: bbeacon_interpreter

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_beacon_interpreter_packed(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.BeaconInterpreterPackedDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**BeaconInterpreterPackedDto**](BeaconInterpreterPackedDto.md)|  | 

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

# **execute_beacon_interpreter_string**
> AsyncCommandResponse execute_beacon_interpreter_string(bid, request_model)

Run Beacon Interpreter Script With Optional String Argument

Compile and execute a C script in Beacon Interpreter using a string argument.

Related CS Console Command: beacon-interpreter

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_beacon_interpreter_string(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.BeaconInterpreterStringDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**BeaconInterpreterStringDto**](BeaconInterpreterStringDto.md)|  | 

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

# **execute_bof_packed_arg**
> AsyncCommandResponse execute_bof_packed_arg(bid, request_model)

Run BOF with Packed Arguments

Execute a Beacon Object File (BOF) with the packed argument.

Related CS Aggressor function: binline_execute()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bof_packed_arg(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecutePackedDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecutePackedDto**](InlineExecutePackedDto.md)|  | 

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

# **execute_bof_string_arg**
> AsyncCommandResponse execute_bof_string_arg(bid, request_model)

Run BOF

Execute a Beacon Object File (BOF) with a String argument.

Related CS Console Command: inline-execute

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bof_string_arg(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecuteStringDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecuteStringDto**](InlineExecuteStringDto.md)|  | 

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

# **execute_bofpe_packed_arg**
> AsyncCommandResponse execute_bofpe_packed_arg(bid, request_model)

Run BOF-PE with Packed Arguments

Execute a BOF-PE with packed arguments.

Related CS Console Command: inline-execute-pe

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bofpe_packed_arg(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecutePePackedDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecutePePackedDto**](InlineExecutePePackedDto.md)|  | 

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

# **execute_bofpe_string_arg**
> AsyncCommandResponse execute_bofpe_string_arg(bid, request_model)

Run BOF-PE

Execute a BOF-PE with a String argument.

Related CS Console Command: inline-execute-pe

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bofpe_string_arg(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecutePeStringDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecutePeStringDto**](InlineExecutePeStringDto.md)|  | 

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

# **execute_bofpeto_pack_args**
> AsyncCommandResponse execute_bofpeto_pack_args(bid, request_model)

Pack Arguments and Run BOF-PE

Pack the provided arguments and execute a BOF-PE with the resulting packed argument.

Related CS Aggressor function: bof_pack() then beacon_inline_execute_pe()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bofpeto_pack_args(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecutePePackDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecutePePackDto**](InlineExecutePePackDto.md)|  | 

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

# **execute_bofto_pack_args**
> AsyncCommandResponse execute_bofto_pack_args(bid, request_model)

Pack Arguments and Run BOF

Pack the provided arguments and execute a Beacon Object File (BOF) with the resulting packed argument.

Related CS Aggressor function: bof_pack() then binline_execute()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_bofto_pack_args(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InlineExecutePackDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InlineExecutePackDto**](InlineExecutePackDto.md)|  | 

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

# **execute_exit**
> AsyncCommandResponse execute_exit(bid)

Exit

Terminate the Beacon session.

Related CS Console Command: exit

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_exit(
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

# **execute_get_privs**
> AsyncCommandResponse execute_get_privs(bid)

Enable all available privileges

Enable as many system privileges as possible on current token.

Related CS Console Command: getprivs

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_get_privs(
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

# **execute_get_system**
> AsyncCommandResponse execute_get_system(bid)

Attempt to obtain System Privileges

Elevate the session permissions from a local administrator to SYSTEM.

Related CS Console Command: getsystem

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_get_system(
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

# **execute_get_uid**
> AsyncCommandResponse execute_get_uid(bid)

Get current User ID

Get the User ID associated with the current token.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_get_uid(
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

# **execute_kill_process**
> AsyncCommandResponse execute_kill_process(bid, request_model)

Kill Process

Kills the specified process.

Related CS Console Command: kill

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_kill_process(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.KillDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**KillDto**](KillDto.md)|  | 

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

# **execute_power_shell_import**
> AsyncCommandResponse execute_power_shell_import(bid, request_model)

Import Powershell Script

Import a powershell script which is combined with future calls to the powershell command.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_power_shell_import(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PowerShellImportDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PowerShellImportDto**](PowerShellImportDto.md)|  | 

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

# **execute_ps**
> AsyncCommandResponse execute_ps(bid)

List Process information

List information about processes running on the system.\n\nRelated CS Console Command: ps

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_ps(
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

# **execute_set_env**
> AsyncCommandResponse execute_set_env(bid, request_model)

Set Environment variable

Set an environment variable.

Related CS Console Command: setenv

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.execute_set_env(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SetEnvDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**SetEnvDto**](SetEnvDto.md)|  | 

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

# **inject_beacon**
> AsyncCommandResponse inject_beacon(bid, request_model)

Execute Beacon Shellcode (Inject)

Open the process and inject shellcode to start a Beacon.

Related CS Console Command: inject

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_beacon(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.InjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**InjectDto**](InjectDto.md)|  | 

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

# **inject_dll**
> AsyncCommandResponse inject_dll(bid, request_model)

Load DLL via reflective DLL loading (Inject)

Open the process and injects a Reflective DLL.

Related CS Console Command: dllinject

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_dll(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DllInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**DllInjectDto**](DllInjectDto.md)|  | 

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

# **inject_load_dll**
> AsyncCommandResponse inject_load_dll(bid, request_model)

Load Library from disk (Inject)

Load DLL into specified remote process via LoadLibrary(). The DLL must exist on the target.

Related CS Console Command: dllload

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_load_dll(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DllLoadDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**DllLoadDto**](DllLoadDto.md)|  | 

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

# **inject_pth**
> AsyncCommandResponse inject_pth(bid, request_model)

Pass-the-Hash (Inject)

Inject into the specified process to generate AND impersonate a token. This command uses mimikatz to generate AND impersonate a token that uses the specified DOMAIN, user, and NTLM hash as single sign-on credentials. Beacon will pass this hash when you interact with network resources.

Related CS Console Command: pth

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_pth(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PthInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PthInjectDto**](PthInjectDto.md)|  | 

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

# **inject_shellcode**
> AsyncCommandResponse inject_shellcode(bid, request_model)

Execute Shellcode (Inject)

Open the process and inject shellcode into it.

Related CS Console Command: shinject

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_shellcode(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ShInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**ShInjectDto**](ShInjectDto.md)|  | 

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

# **inject_unmanaged_power_shell**
> AsyncCommandResponse inject_unmanaged_power_shell(bid, request_model)

Execute unmanaged Powershell  / psinject (Inject)

Inject Unmanaged Powershell into a specific process and execute the specified command.

Related CS Console Command: psinject

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.inject_unmanaged_power_shell(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PowerShellInject(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PowerShellInject**](PowerShellInject.md)|  | 

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

# **list_elevate_command_methods**
> List[ElevatorInfoDto] list_elevate_command_methods(bid)

List Command Privilege Elevators

List available local privilege elevation techniques specific for running a command.

Related CS Console Command: runasadmin

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.list_elevate_command_methods(
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

[**List[ElevatorInfoDto]**](ElevatorInfoDto.md)

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

# **list_remote_execute_beacon_methods**
> List[RemoteExploitInfoDto] list_remote_execute_beacon_methods(bid)

List Remote Beacon Execution methods

List available remote command execution methods for running Beacon remotely.

Related CS Console Command: jump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.list_remote_execute_beacon_methods(
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

[**List[RemoteExploitInfoDto]**](RemoteExploitInfoDto.md)

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

# **list_remote_execution_command_methods**
> List[RemoteExecInfoDto] list_remote_execution_command_methods(bid)

List Remote Command Execution methods

List available remote command execution methods for running a remote command.

Related CS Console Command: remote-exec

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.list_remote_execution_command_methods(
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

[**List[RemoteExecInfoDto]**](RemoteExecInfoDto.md)

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

# **remote_execute_beacon**
> AsyncCommandResponse remote_execute_beacon(bid, request_model)

Remote Beacon Execution (jump)

Execute a Beacon session on a remote target with the specified remote execution method. Could use spawn or inject depending on chosen method.

Related CS Console Command: jump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.remote_execute_beacon(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.JumpDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**JumpDto**](JumpDto.md)|  | 

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

# **remote_execute_command**
> AsyncCommandResponse remote_execute_command(bid, request_model)

Remote Command Execution (remote-exec)

Execute a command on a target via specific remote execution method.  Could use spawn or inject depending on chosen method.

Related CS Console Command: remote-exec

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.remote_execute_command(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RemoteExecDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RemoteExecDto**](RemoteExecDto.md)|  | 

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

# **spawn_beacon**
> AsyncCommandResponse spawn_beacon(bid, request_model)

Execute Beacon Shellcode (Spawn)

Spawn an x86 or x64 process and inject shellcode for the payload source.

Related CS Console Command: spawn

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_beacon(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**SpawnDto**](SpawnDto.md)|  | 

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

# **spawn_beacon_as_user**
> AsyncCommandResponse spawn_beacon_as_user(bid, request_model)

Execute Beacon Shellcode as User (Spawn)

Spawn a process as another user and Beacon inject shellcode for the payload source.

Related CS Console Command: spawnas

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_beacon_as_user(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpawnBeaconAsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**SpawnBeaconAsDto**](SpawnBeaconAsDto.md)|  | 

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

# **spawn_beacon_under**
> AsyncCommandResponse spawn_beacon_under(bid, request_model)

Execute Beacon Shellcode under parentPID (Spawn)

Attempt to spawn a session with the specified PID as its parent.

Related CS Console Command: spawnu

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_beacon_under(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.SpawnuDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**SpawnuDto**](SpawnuDto.md)|  | 

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

# **spawn_dot_net_assembly**
> AsyncCommandResponse spawn_dot_net_assembly(bid, request_model)

Execute .NET assembly  (Spawn)

Spawns a local .NET executable assembly as a Beacon post-exploitation job.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_dot_net_assembly(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ExecuteAssemblyDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ExecuteAssemblyDto**](ExecuteAssemblyDto.md)|  | 

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

# **spawn_power_shell**
> AsyncCommandResponse spawn_power_shell(bid, request_model)

Execute Managed Powershell (Spawn)

Execute the command using powershell.

Related CS Console Command: powershell

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_power_shell(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PowerShellDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**PowerShellDto**](PowerShellDto.md)|  | 

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

# **spawn_pth**
> AsyncCommandResponse spawn_pth(bid, request_model)

Pass-the-Hash (Spawn)

Spawn a temporary process to generate AND impersonate a token. This command uses mimikatz to generate AND impersonate a token that uses the specified DOMAIN, user, and NTLM hash as single sign-on credentials. Beacon will pass this hash when you interact with network resources.

Related CS Console Command: pth

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_pth(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PthSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PthSpawnDto**](PthSpawnDto.md)|  | 

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

# **spawn_run_command**
> AsyncCommandResponse spawn_run_command(bid, request_model)

Run (Spawn)

Execute the program. Returns output.

Related CS Console Command: run

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_run_command(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RunDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**RunDto**](RunDto.md)|  | 

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

# **spawn_run_command_as**
> AsyncCommandResponse spawn_run_command_as(bid, request_model)

Run As (Spawn)

Attempt to execute a program as another user.

Related CS Console Command: runas

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_run_command_as(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RunAsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**RunAsDto**](RunAsDto.md)|  | 

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

# **spawn_run_command_under**
> AsyncCommandResponse spawn_run_command_under(bid, request_model)

Run under parentPID (Spawn)

Attempt to execute a program with the specified PID as its parent.

Related CS Console Command: runu

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_run_command_under(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RunUDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**RunUDto**](RunUDto.md)|  | 

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

# **spawn_shell_command**
> AsyncCommandResponse spawn_shell_command(bid, request_model)

Run Shell Command (Spawn)

Execute the command using cmd.exe.

Related CS Console Command: shell

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_shell_command(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ShellDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**ShellDto**](ShellDto.md)|  | 

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

# **spawn_shellcode**
> AsyncCommandResponse spawn_shellcode(bid, request_model)

Execute Shellcode (Spawn)

Spawn a process and inject shellcode into it.

Related CS Console Command: shspawn

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_shellcode(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ShSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**ShSpawnDto**](ShSpawnDto.md)|  | 

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

# **spawn_unmanaged_power_shell**
> AsyncCommandResponse spawn_unmanaged_power_shell(bid, request_model)

Execute unmanaged Powershell  / powerpick (Spawn)

Execute the Powershell command using Unmanaged PowerShell. Unmanaged PowerShell is a way to run PowerShell scripts without powershell.exe. the code loads the .NET CLR, reflectively loads a .NET class through that CLR, and uses that .NET class to call APIs in the System.management.automation namespace to evaluate arbitrary PowerShell expressions.

Related CS Console Command: powerpick

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import ProcessAndExecutionApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = ProcessAndExecutionApi(client)
        response = await api.spawn_unmanaged_power_shell(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PowerPickDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PowerPickDto**](PowerPickDto.md)|  | 

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

