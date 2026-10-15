# cs_sdk_python.api_client.FileAndRegistryApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_file_download**](FileAndRegistryApi.md#cancel_file_download) | **POST** /api/v1/beacons/{bid}/execute/cancelFileDownload | Cancel Download
[**delete_download**](FileAndRegistryApi.md#delete_download) | **DELETE** /api/v1/data/downloads/{id} | Delete Download
[**execute_cd**](FileAndRegistryApi.md#execute_cd) | **POST** /api/v1/beacons/{bid}/execute/cd | Change Current Directory
[**execute_cp**](FileAndRegistryApi.md#execute_cp) | **POST** /api/v1/beacons/{bid}/execute/cp | Copy File
[**execute_download**](FileAndRegistryApi.md#execute_download) | **POST** /api/v1/beacons/{bid}/execute/download | Download File
[**execute_drives**](FileAndRegistryApi.md#execute_drives) | **POST** /api/v1/beacons/{bid}/execute/drives | List Drives
[**execute_ls**](FileAndRegistryApi.md#execute_ls) | **POST** /api/v1/beacons/{bid}/execute/ls | List Directory contents
[**execute_mkdir**](FileAndRegistryApi.md#execute_mkdir) | **POST** /api/v1/beacons/{bid}/execute/mkdir | Create Directory
[**execute_move**](FileAndRegistryApi.md#execute_move) | **POST** /api/v1/beacons/{bid}/execute/mv | Move File
[**execute_pwd**](FileAndRegistryApi.md#execute_pwd) | **POST** /api/v1/beacons/{bid}/execute/pwd | Get Current Directory
[**execute_reg_query**](FileAndRegistryApi.md#execute_reg_query) | **POST** /api/v1/beacons/{bid}/execute/reg/query | Get Registry Key
[**execute_reg_query_value**](FileAndRegistryApi.md#execute_reg_query_value) | **POST** /api/v1/beacons/{bid}/execute/reg/queryv | Get Registry SubKey
[**execute_rm**](FileAndRegistryApi.md#execute_rm) | **POST** /api/v1/beacons/{bid}/execute/rm | Remove File or Folder
[**execute_timestomp**](FileAndRegistryApi.md#execute_timestomp) | **POST** /api/v1/beacons/{bid}/execute/timestomp | Timestomp
[**execute_upload**](FileAndRegistryApi.md#execute_upload) | **POST** /api/v1/beacons/{bid}/execute/upload | Upload File
[**get_download**](FileAndRegistryApi.md#get_download) | **GET** /api/v1/data/downloads/{id} | Get Download
[**list_active_downloads**](FileAndRegistryApi.md#list_active_downloads) | **GET** /api/v1/beacons/{bid}/activeDownloads | List Active Downloads
[**list_downloads**](FileAndRegistryApi.md#list_downloads) | **GET** /api/v1/data/downloads | List Downloads


# **cancel_file_download**
> AsyncCommandResponse cancel_file_download(bid, request_model)

Cancel Download

Cancels a download that is currently in progress.

Related CS Console Command: cancel

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.cancel_file_download(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.FileDownloadCancelDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**FileDownloadCancelDto**](FileDownloadCancelDto.md)|  | 

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

# **delete_download**
> delete_download(id)

Delete Download

Delete a Download from the Downloads data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        await api.delete_download(
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

# **execute_cd**
> AsyncCommandResponse execute_cd(bid, request_model)

Change Current Directory

Change the working directory of this Beacon.

Related CS Console Command: cd

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_cd(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.CdDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**CdDto**](CdDto.md)|  | 

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

# **execute_cp**
> AsyncCommandResponse execute_cp(bid, request_model)

Copy File

Copy source file to the specified destination.

Related CS Console Command: cp

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_cp(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.CpDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**CpDto**](CpDto.md)|  | 

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

# **execute_download**
> AsyncCommandResponse execute_download(bid, request_model)

Download File

Download a file to the team server.

Related CS Console Command: download

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_download(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DownloadDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**DownloadDto**](DownloadDto.md)|  | 

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

# **execute_drives**
> AsyncCommandResponse execute_drives(bid)

List Drives

Lists drivers on current system.

Related CS Console Command: drives

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_drives(
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

# **execute_ls**
> AsyncCommandResponse execute_ls(bid, request_model)

List Directory contents

Lists files in a folder.

Related CS Console Command: ls

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_ls(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.LsDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**LsDto**](LsDto.md)|  | 

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

# **execute_mkdir**
> AsyncCommandResponse execute_mkdir(bid, request_model)

Create Directory

Create a directory, if it does not already exist.

Related CS Console Command: mkdir

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_mkdir(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MkdirDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**MkdirDto**](MkdirDto.md)|  | 

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

# **execute_move**
> AsyncCommandResponse execute_move(bid, request_model)

Move File

Move source file to the specified destination.

Related CS Console Command: mv

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_move(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MoveDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**MoveDto**](MoveDto.md)|  | 

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

# **execute_pwd**
> AsyncCommandResponse execute_pwd(bid)

Get Current Directory

Displays the current working directory of this Beacon.

Related CS Console Command: pwd

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_pwd(
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

# **execute_reg_query**
> AsyncCommandResponse execute_reg_query(bid, request_model)

Get Registry Key

Query a key within the registry. Lists all subkeys and values.

Related CS Console Command: reg query

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_reg_query(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RegQueryDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RegQueryDto**](RegQueryDto.md)|  | 

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

# **execute_reg_query_value**
> AsyncCommandResponse execute_reg_query_value(bid, request_model)

Get Registry SubKey

Query a subkey within the registry. Lists only the subkey and its value.

Related CS Console Command: reg queryv

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_reg_query_value(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RegQueryValueDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**RegQueryValueDto**](RegQueryValueDto.md)|  | 

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

# **execute_rm**
> AsyncCommandResponse execute_rm(bid, request_model)

Remove File or Folder

Remove a file or folder via the Beacon.

Related CS Console Command: rm

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_rm(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.RmDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**RmDto**](RmDto.md)|  | 

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

# **execute_timestomp**
> AsyncCommandResponse execute_timestomp(bid, request_model)

Timestomp

Update the Modified, Access, and Created times of source file to match those of destination file.

Related CS Console Command: timestomp

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_timestomp(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.TimeStompDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**TimeStompDto**](TimeStompDto.md)|  | 

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

# **execute_upload**
> AsyncCommandResponse execute_upload(bid, request_model)

Upload File

Upload a file to a host via the Beacon.

Related CS Console Command: upload

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.execute_upload(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.UploadDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**UploadDto**](UploadDto.md)|  | 

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

# **get_download**
> object get_download(id)

Get Download

Get the specified download from the team servers Downloads data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.get_download(
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

# **list_active_downloads**
> List[DownloadProgressDto] list_active_downloads(bid)

List Active Downloads

Lists file downloads currently in progress for a given Beacon.

Related CS Console Command: downloads

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.list_active_downloads(
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

[**List[DownloadProgressDto]**](DownloadProgressDto.md)

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

# **list_downloads**
> List[DownloadDto] list_downloads()

List Downloads

Lists all downloaded files from the Downloads data model.

Related CS Aggressor function: downloads()

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import FileAndRegistryApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = FileAndRegistryApi(client)
        response = await api.list_downloads()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DownloadDto]**](DownloadDto.md)

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

