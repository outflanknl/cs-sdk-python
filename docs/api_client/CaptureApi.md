# cs_sdk_python.api_client.CaptureApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_keystrokes**](CaptureApi.md#delete_keystrokes) | **DELETE** /api/v1/data/keystrokes/{id} | Delete Keystrokes
[**delete_screenshot**](CaptureApi.md#delete_screenshot) | **DELETE** /api/v1/data/screenshots/{id} | Delete Screenshot
[**execute_clipboard**](CaptureApi.md#execute_clipboard) | **POST** /api/v1/beacons/{bid}/execute/clipboard | Get Clipboard content
[**get_key_strokes_by_bid**](CaptureApi.md#get_key_strokes_by_bid) | **GET** /api/v1/beacons/{bid}/keystrokes | List Beacon Keystrokes
[**get_screenshot**](CaptureApi.md#get_screenshot) | **GET** /api/v1/data/screenshots/{id} | Get Screenshot
[**inject_keylogger**](CaptureApi.md#inject_keylogger) | **POST** /api/v1/beacons/{bid}/inject/keylogger | Start Keylogger (Inject)
[**inject_print_screen**](CaptureApi.md#inject_print_screen) | **POST** /api/v1/beacons/{bid}/inject/printscreen | Print Screen (Inject)
[**inject_screenshot**](CaptureApi.md#inject_screenshot) | **POST** /api/v1/beacons/{bid}/inject/screenshot | Take Screenshot (Inject)
[**inject_screenwatch**](CaptureApi.md#inject_screenwatch) | **POST** /api/v1/beacons/{bid}/inject/screenwatch | Start Screenwatch (Inject)
[**list_key_strokes**](CaptureApi.md#list_key_strokes) | **GET** /api/v1/data/keystrokes | List Keystrokes
[**list_screenshots**](CaptureApi.md#list_screenshots) | **GET** /api/v1/data/screenshots | List Screenshots
[**spawn_keylogger**](CaptureApi.md#spawn_keylogger) | **POST** /api/v1/beacons/{bid}/spawn/keylogger | Start Keylogger (Spawn)
[**spawn_print_screen**](CaptureApi.md#spawn_print_screen) | **POST** /api/v1/beacons/{bid}/spawn/printscreen | Print Screen (Spawn)
[**spawn_screenshot**](CaptureApi.md#spawn_screenshot) | **POST** /api/v1/beacons/{bid}/spawn/screenshot | Take Screenshot (Spawn)
[**spawn_screenwatch**](CaptureApi.md#spawn_screenwatch) | **POST** /api/v1/beacons/{bid}/spawn/screenwatch | Start Screenwatch (Spawn)


# **delete_keystrokes**
> delete_keystrokes(id)

Delete Keystrokes

Delete a specified Keystroke.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        await api.delete_keystrokes(
            id='id_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_screenshot**
> delete_screenshot(id)

Delete Screenshot

Delete the specified Screenshot from Cobalt Strike's data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        await api.delete_screenshot(
            id='id_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **execute_clipboard**
> AsyncCommandResponse execute_clipboard(bid)

Get Clipboard content

Get text from the clipboard contents.

Related CS Console Command: clipboard

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.execute_clipboard(
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

# **get_key_strokes_by_bid**
> List[KeystrokeDto] get_key_strokes_by_bid(bid)

List Beacon Keystrokes

List all keystrokes for a specified Beacon.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.get_key_strokes_by_bid(
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

[**List[KeystrokeDto]**](KeystrokeDto.md)

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

# **get_screenshot**
> object get_screenshot(id)

Get Screenshot

Retrieve a specified Screenshot from Cobalt Strike's data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.get_screenshot(
            id='id_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **inject_keylogger**
> AsyncCommandResponse inject_keylogger(bid, request_model)

Start Keylogger (Inject)

Keystroke logger to capture the keys pressed. The keylogger DLL is injected in the specified process.

The Keylogger is implemented as a job and can be stopped using the jobkill command or the /execute/jobStop route.

Related CS Console Command: keylogger

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.inject_keylogger(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.KeyLoggerInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**KeyLoggerInjectDto**](KeyLoggerInjectDto.md)|  | 

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

# **inject_print_screen**
> AsyncCommandResponse inject_print_screen(bid, request_model)

Print Screen (Inject)

A DLL is injected in the specified process, sends a PrintScr keypress and grab the screenshot from the clipboard. Will clear the clipboard contents after its done.

Related CS Console Command: printscreen

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.inject_print_screen(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.PrintScreenInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**PrintScreenInjectDto**](PrintScreenInjectDto.md)|  | 

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

# **inject_screenshot**
> AsyncCommandResponse inject_screenshot(bid, request_model)

Take Screenshot (Inject)

Takes a picture of the visible desktop and exit. The Screenshot DLL is injected in the specified process.

Related CS Console Command: screenshot

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.inject_screenshot(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ScreenshotInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ScreenshotInjectDto**](ScreenshotInjectDto.md)|  | 

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

# **inject_screenwatch**
> AsyncCommandResponse inject_screenwatch(bid, request_model)

Start Screenwatch (Inject)

Screenwatch sends a screenshot of the user's desktop (one per Beacon check-in) until terminated. If the user is idle, the screen watch DLL will take a new screenshot every three minutes. The Screenshot DLL is injected in the specified process.

Screenwatch is implemented as a job and can be stopped using the jobkill command or the /execute/jobStop route.

Related CS Console Command: screenwatch

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.inject_screenwatch(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ScreenwatchInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ScreenwatchInjectDto**](ScreenwatchInjectDto.md)|  | 

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

# **list_key_strokes**
> List[KeystrokeDto] list_key_strokes()

List Keystrokes

List all keystrokes in the inventory.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.list_key_strokes()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[KeystrokeDto]**](KeystrokeDto.md)

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

# **list_screenshots**
> List[ScreenshotDto] list_screenshots()

List Screenshots

Returns a list of screenshots from Cobalt Strike's data model.

Related CS Aggressor function: screenshots()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.list_screenshots()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ScreenshotDto]**](ScreenshotDto.md)

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

# **spawn_keylogger**
> AsyncCommandResponse spawn_keylogger(bid)

Start Keylogger (Spawn)

Keystroke logger to capture the keys pressed. A new process is spawned and the keylogger DLL is injected into it.

The Keylogger is implemented as a job and can be stopped using the jobkill command or the /execute/jobStop route.

Related CS Console Command: keylogger

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.spawn_keylogger(
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

# **spawn_print_screen**
> AsyncCommandResponse spawn_print_screen(bid)

Print Screen (Spawn)

A DLL is injected a newly spawned process, sends a PrintScr keypress and grab the screenshot from the clipboard. Will clear the clipboard contents after its done.

Related CS Console Command: printscreen

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.spawn_print_screen(
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

# **spawn_screenshot**
> AsyncCommandResponse spawn_screenshot(bid)

Take Screenshot (Spawn)

Takes a picture of the visible desktop and exit. A new process is spawned and the screenshot DLL  is injected into it.

Related CS Console Command: screenshot

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.spawn_screenshot(
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

# **spawn_screenwatch**
> AsyncCommandResponse spawn_screenwatch(bid)

Start Screenwatch (Spawn)

Screenwatch sends a screenshot of the user's desktop (one per Beacon check-in) until terminated. If the user is idle, the screen watch DLL will take a new screenshot every three minutes. A new process is spawned and the Screenshot DLL is injected into it.

Screenwatch is implemented as a job and can be stopped using the jobkill command or the /execute/jobStop route.

Related CS Console Command: screenwatch

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CaptureApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CaptureApi(client)
        response = await api.spawn_screenwatch(
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

