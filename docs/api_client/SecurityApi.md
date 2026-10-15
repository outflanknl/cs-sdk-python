# cs_sdk_python.api_client.SecurityApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](SecurityApi.md#authenticate_user) | **POST** /api/auth/login | Generate a token to access the Rest API Server


# **authenticate_user**
> AuthDto authenticate_user(request_model)

Generate a token to access the Rest API Server

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import SecurityApi


async def main():
    config = Configuration(host="https://localhost:50443")
    async with ApiClient(config) as client:
        api = SecurityApi(client)
        response = await api.authenticate_user(
            request_model=cs_sdk_python.api_client.LoginRequest(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**AuthDto**](AuthDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

