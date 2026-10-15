# cs_sdk_python.api_client.PayloadAndArtifactsApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_payload**](PayloadAndArtifactsApi.md#download_payload) | **GET** /api/v1/payloads/{fileName} | Retrieve payload
[**generate_stageless_payload**](PayloadAndArtifactsApi.md#generate_stageless_payload) | **POST** /api/v1/payloads/generate/stageless | Create Stageless Payload
[**generate_stager_payload**](PayloadAndArtifactsApi.md#generate_stager_payload) | **POST** /api/v1/payloads/generate/stager | Create Stager Payload
[**get_payload_store_metadata**](PayloadAndArtifactsApi.md#get_payload_store_metadata) | **GET** /api/v1/artifacts/payload/{name}/metadata | Get Payload Store Metadata
[**list_artifacts**](PayloadAndArtifactsApi.md#list_artifacts) | **GET** /api/v1/artifacts | List Artifacts
[**upload_payload_store_item**](PayloadAndArtifactsApi.md#upload_payload_store_item) | **POST** /api/v1/artifacts/payload | Upload Payload Store Item


# **download_payload**
> bytearray download_payload(file_name)

Retrieve payload

Retrieve a previously generated payload stored server-side.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.download_payload(
            file_name='file_name_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Name of the payload to download | 

### Return type

**bytearray**

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

# **generate_stageless_payload**
> object generate_stageless_payload(request_model)

Create Stageless Payload

Generate a Stageless Payload from a Cobalt Strike Listener and save it to the payload store.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.generate_stageless_payload(
            request_model=cs_sdk_python.api_client.PayloadDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**PayloadDto**](PayloadDto.md)|  | 

### Return type

**object**

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

# **generate_stager_payload**
> object generate_stager_payload(request_model)

Create Stager Payload

Generate a Stager Payload from a Cobalt Strike Listener and save it to the payload store.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.generate_stager_payload(
            request_model=cs_sdk_python.api_client.PayloadStagerDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**PayloadStagerDto**](PayloadStagerDto.md)|  | 

### Return type

**object**

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

# **get_payload_store_metadata**
> PayloadStoreMetadataDto get_payload_store_metadata(name)

Get Payload Store Metadata

Retrieve payload store item metadata by payload store name.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.get_payload_store_metadata(
            name='name_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Payload store item name | 

### Return type

[**PayloadStoreMetadataDto**](PayloadStoreMetadataDto.md)

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

# **list_artifacts**
> List[ArtifactDto] list_artifacts()

List Artifacts

Retrieve a listing of all server side artifacts/files and their references. Various commands that expect a filename can ingest an artifact (e.g. executeBOF).

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.list_artifacts()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ArtifactDto]**](ArtifactDto.md)

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

# **upload_payload_store_item**
> PayloadStoreUploadResponseDto upload_payload_store_item(request_model)

Upload Payload Store Item

Upload Base64-encoded payload bytes into Payload Store.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import PayloadAndArtifactsApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = PayloadAndArtifactsApi(client)
        response = await api.upload_payload_store_item(
            request_model=cs_sdk_python.api_client.PayloadStoreUploadDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**PayloadStoreUploadDto**](PayloadStoreUploadDto.md)|  | 

### Return type

[**PayloadStoreUploadResponseDto**](PayloadStoreUploadResponseDto.md)

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

