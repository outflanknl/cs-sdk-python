# cs_sdk_python.api_client.CredsAndTokensApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credential**](CredsAndTokensApi.md#add_credential) | **POST** /api/v1/data/credentials | Add Credential
[**delete_credential**](CredsAndTokensApi.md#delete_credential) | **DELETE** /api/v1/data/credentials/{id} | Delete Credential
[**elevate_beacon**](CredsAndTokensApi.md#elevate_beacon) | **POST** /api/v1/beacons/{bid}/elevate/beacon | Run a Beacon elevated (elevate)
[**execute_kerberos_ticket_purge**](CredsAndTokensApi.md#execute_kerberos_ticket_purge) | **POST** /api/v1/beacons/{bid}/execute/kerberos/ticket/purge | Purge Kerberos Ticket
[**execute_kerberos_ticket_use**](CredsAndTokensApi.md#execute_kerberos_ticket_use) | **POST** /api/v1/beacons/{bid}/execute/kerberos/ticket/use | Use Kerberos Ticket
[**execute_make_token_logon_name**](CredsAndTokensApi.md#execute_make_token_logon_name) | **POST** /api/v1/beacons/{bid}/execute/makeToken/logonName | Make Token with Logon Name
[**execute_make_token_upn**](CredsAndTokensApi.md#execute_make_token_upn) | **POST** /api/v1/beacons/{bid}/execute/makeToken/upn | Make Token with UPN
[**execute_rev2_self**](CredsAndTokensApi.md#execute_rev2_self) | **POST** /api/v1/beacons/{bid}/execute/rev2self | Revert Token
[**execute_steal_token**](CredsAndTokensApi.md#execute_steal_token) | **POST** /api/v1/beacons/{bid}/execute/stealToken | Steal Token
[**execute_token_store_remove_all_tokens**](CredsAndTokensApi.md#execute_token_store_remove_all_tokens) | **POST** /api/v1/beacons/{bid}/execute/tokenStore/removeAll | Delete All Tokens
[**execute_token_store_remove_token**](CredsAndTokensApi.md#execute_token_store_remove_token) | **POST** /api/v1/beacons/{bid}/execute/tokenStore/remove | Delete Token
[**execute_token_store_steal_and_use_token**](CredsAndTokensApi.md#execute_token_store_steal_and_use_token) | **POST** /api/v1/beacons/{bid}/execute/tokenStore/stealAndUse | Steal and Use Token
[**execute_token_store_steal_token**](CredsAndTokensApi.md#execute_token_store_steal_token) | **POST** /api/v1/beacons/{bid}/execute/tokenStore/steal | Steal and Store Token
[**execute_token_store_use_token**](CredsAndTokensApi.md#execute_token_store_use_token) | **POST** /api/v1/beacons/{bid}/execute/tokenStore/use | Use Token
[**get_credential**](CredsAndTokensApi.md#get_credential) | **GET** /api/v1/data/credentials/{id} | Get Credential
[**inject_chrome_dump**](CredsAndTokensApi.md#inject_chrome_dump) | **POST** /api/v1/beacons/{bid}/inject/chromedump | Chromedump (Inject)
[**inject_dc_sync**](CredsAndTokensApi.md#inject_dc_sync) | **POST** /api/v1/beacons/{bid}/inject/dcsync | DCSYNC (Inject)
[**inject_hash_dump**](CredsAndTokensApi.md#inject_hash_dump) | **POST** /api/v1/beacons/{bid}/inject/hashdump | HashDump (Inject)
[**inject_logon_passwords**](CredsAndTokensApi.md#inject_logon_passwords) | **POST** /api/v1/beacons/{bid}/inject/logonPasswords | Dump Credentials (Inject)
[**inject_mimikatz**](CredsAndTokensApi.md#inject_mimikatz) | **POST** /api/v1/beacons/{bid}/inject/mimikatz | Mimikatz (Inject)
[**inject_post_ex_dll**](CredsAndTokensApi.md#inject_post_ex_dll) | **POST** /api/v1/beacons/{bid}/inject/postExDll | Inject PostEx Dll (Inject)
[**list_credentials**](CredsAndTokensApi.md#list_credentials) | **GET** /api/v1/data/credentials | List Credentials
[**list_elevate_beacon_methods**](CredsAndTokensApi.md#list_elevate_beacon_methods) | **GET** /api/v1/beacons/{bid}/elevate/beacon | List Privesc methods
[**list_token_store**](CredsAndTokensApi.md#list_token_store) | **POST** /api/v1/beacons/{bid}/state/tokenStore | List Tokens
[**spawn_chrome_dump**](CredsAndTokensApi.md#spawn_chrome_dump) | **POST** /api/v1/beacons/{bid}/spawn/chromedump | Chromedump (Spawn)
[**spawn_dc_sync**](CredsAndTokensApi.md#spawn_dc_sync) | **POST** /api/v1/beacons/{bid}/spawn/dcsync | DCSYNC (Spawn)
[**spawn_hash_dump**](CredsAndTokensApi.md#spawn_hash_dump) | **POST** /api/v1/beacons/{bid}/spawn/hashdump | HashDump (Spawn)
[**spawn_logon_passwords**](CredsAndTokensApi.md#spawn_logon_passwords) | **POST** /api/v1/beacons/{bid}/spawn/logonPasswords | Dump Credentials (Spawn)
[**spawn_mimikatz**](CredsAndTokensApi.md#spawn_mimikatz) | **POST** /api/v1/beacons/{bid}/spawn/mimikatz | Mimikatz (Spawn)
[**spawn_post_ex_dll**](CredsAndTokensApi.md#spawn_post_ex_dll) | **POST** /api/v1/beacons/{bid}/spawn/postExDll | Execute PostEx DLL (Spawn)
[**spawn_run_command_no_output**](CredsAndTokensApi.md#spawn_run_command_no_output) | **POST** /api/v1/beacons/{bid}/spawn/command/runNoOutput | Run without output (Spawn)


# **add_credential**
> add_credential(request_model)

Add Credential

Add a credential into the credentials data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        await api.add_credential(
            request_model=cs_sdk_python.api_client.CredentialDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **request_model** | [**CredentialDto**](CredentialDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuthentication](README.md#BearerAuthentication)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to Model list]](README.md#documentation-for-models) [[Back to API reference]](README.md)

# **delete_credential**
> delete_credential(id)

Delete Credential

Delete a credential from the credentials data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        await api.delete_credential(
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

# **elevate_beacon**
> AsyncCommandResponse elevate_beacon(bid, request_model)

Run a Beacon elevated (elevate)

Attempt to create an elevated Beacon session with the specified privilege elevation technique. Depending on technique, proceses could be spawned or injected.

Related CS Console Command: elevate

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.elevate_beacon(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ElevateDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ElevateDto**](ElevateDto.md)|  | 

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

# **execute_kerberos_ticket_purge**
> AsyncCommandResponse execute_kerberos_ticket_purge(bid)

Purge Kerberos Ticket

Purges Kerberos tickets from this session.

Related CS Console Command: kerberos_ticket_purge

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_kerberos_ticket_purge(
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

# **execute_kerberos_ticket_use**
> AsyncCommandResponse execute_kerberos_ticket_use(bid, request_model)

Use Kerberos Ticket

Applies a Kerberos ticket (.kirbi) to this session.

Related CS Console Command: kerberos_ticket_use

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_kerberos_ticket_use(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.KerberosTicketUseDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**KerberosTicketUseDto**](KerberosTicketUseDto.md)|  | 

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

# **execute_make_token_logon_name**
> AsyncCommandResponse execute_make_token_logon_name(bid, request_model)

Make Token with Logon Name

Ask Beacon to create a token from the specified credentials using domain, user and password.

Related CS Console Command: make_token

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_make_token_logon_name(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MakeTokenLogonNameDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**MakeTokenLogonNameDto**](MakeTokenLogonNameDto.md)|  | 

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

# **execute_make_token_upn**
> AsyncCommandResponse execute_make_token_upn(bid, request_model)

Make Token with UPN

Ask Beacon to create a token from the specified credentials using UPN syntax.

Related CS Console Command: make_token

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_make_token_upn(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MakeTokenUpnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**MakeTokenUpnDto**](MakeTokenUpnDto.md)|  | 

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

# **execute_rev2_self**
> AsyncCommandResponse execute_rev2_self(bid)

Revert Token

Request a Beacon to drop any tokens and revert to the original access token.

Related CS Console Command: rev2self

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_rev2_self(
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

# **execute_steal_token**
> AsyncCommandResponse execute_steal_token(bid, request_model)

Steal Token

Request a Beacon to steal a token from a process.

Related CS Console Command: steal_token

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_steal_token(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.StealTokenDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**StealTokenDto**](StealTokenDto.md)|  | 

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

# **execute_token_store_remove_all_tokens**
> AsyncCommandResponse execute_token_store_remove_all_tokens(bid)

Delete All Tokens

"Request a Beacon to remove all tokens from the store.

Related CS Console Command: token-store remove-all"

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_token_store_remove_all_tokens(
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

# **execute_token_store_remove_token**
> AsyncCommandResponse execute_token_store_remove_token(bid, request_model)

Delete Token

Request a Beacon to remove specific access tokens from the store.

Related CS Console Command: token-store remove

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_token_store_remove_token(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.TokenStoreRemoveDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**TokenStoreRemoveDto**](TokenStoreRemoveDto.md)|  | 

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

# **execute_token_store_steal_and_use_token**
> AsyncCommandResponse execute_token_store_steal_and_use_token(bid, request_model)

Steal and Use Token

Request a Beacon to steal a token, store it and immediately apply it to the Beacon.

Related CS Console Command: token-store steal-and-use

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_token_store_steal_and_use_token(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.TokenStoreStealAndUseDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**TokenStoreStealAndUseDto**](TokenStoreStealAndUseDto.md)|  | 

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

# **execute_token_store_steal_token**
> AsyncCommandResponse execute_token_store_steal_token(bid, request_model)

Steal and Store Token

Request a Beacon to steal a token and store it in the token store.

Related CS Console Command: token-store steal

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_token_store_steal_token(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.TokenStoreStealTokensDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**TokenStoreStealTokensDto**](TokenStoreStealTokensDto.md)|  | 

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

# **execute_token_store_use_token**
> AsyncCommandResponse execute_token_store_use_token(bid, request_model)

Use Token

Request a Beacon to use a token from the token store.

Related CS Console Command: token-store use

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.execute_token_store_use_token(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.TokenStoreUseDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**TokenStoreUseDto**](TokenStoreUseDto.md)|  | 

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

# **get_credential**
> CredentialDto get_credential(id)

Get Credential

Get the information of the specified credential from the credentials data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.get_credential(
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

[**CredentialDto**](CredentialDto.md)

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

# **inject_chrome_dump**
> AsyncCommandResponse inject_chrome_dump(bid, request_model)

Chromedump (Inject)

Inject into the specified process to recover credential material from Google Chrome. This command will use Mimikatz to recover the credential material and should be run under a user context.

Related CS Console Command: chromedump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_chrome_dump(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ChromeDumpInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ChromeDumpInjectDto**](ChromeDumpInjectDto.md)|  | 

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

# **inject_dc_sync**
> AsyncCommandResponse inject_dc_sync(bid, request_model)

DCSYNC (Inject)

Inject into the specified process to extract the NTLM password hash for domain users from the domain controller using mimikatz' DCSYNC. Specify a user to get their hash only.
This command requires a domain administrator trust relationship.

Related CS Console Command: dcsync

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_dc_sync(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DcSyncInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**DcSyncInjectDto**](DcSyncInjectDto.md)|  | 

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

# **inject_hash_dump**
> AsyncCommandResponse inject_hash_dump(bid, request_model)

HashDump (Inject)

Inject the hashdump DLL into the specified process. The hashdump DLL will dump password hashes (Warning: Injects into LSASS).
This action requires administrator privileges.

Related CS Console Command: hashdump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_hash_dump(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.HashDumpInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**HashDumpInjectDto**](HashDumpInjectDto.md)|  | 

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

# **inject_logon_passwords**
> AsyncCommandResponse inject_logon_passwords(bid, request_model)

Dump Credentials (Inject)

Inject into the specified process to dump plaintext credentials and NTLM hashes. This action uses mimikatz and requires administrator privileges.

Related CS Console Command: logonpasswords

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_logon_passwords(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.LogonPasswordsInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**LogonPasswordsInjectDto**](LogonPasswordsInjectDto.md)|  | 

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

# **inject_mimikatz**
> AsyncCommandResponse inject_mimikatz(bid, request_model)

Mimikatz (Inject)

Inject into the specified process to run a mimikatz command. 
Use ! to make mimikatz elevate to SYSTEM before it runs your command. Some commands require this.
Use @ to make mimikatz impersonate Beacon's thread token before it runs your command. This is helpful for mimikatz commands that interact with remote systems (e.g., lsadump::dcsync)
Use ; to separate multiple mimikatz commands.  The maximum length of the commands is 511 characters.
Command Example:   crypto::capi ; crypto::certificates /systemstore:local_machine /store:my /export.

Related CS Console Command: mimikatz

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_mimikatz(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MimikatzInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**MimikatzInjectDto**](MimikatzInjectDto.md)|  | 

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

# **inject_post_ex_dll**
> AsyncCommandResponse inject_post_ex_dll(bid, request_model)

Inject PostEx Dll (Inject)

Inject the provided postex DLL into the specified process.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.inject_post_ex_dll(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ExecuteDllInjectDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ExecuteDllInjectDto**](ExecuteDllInjectDto.md)|  | 

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

# **list_credentials**
> List[CredentialDto] list_credentials()

List Credentials

List all credentials in the credentials data model.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.list_credentials()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CredentialDto]**](CredentialDto.md)

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

# **list_elevate_beacon_methods**
> List[LocalExploitInfoDto] list_elevate_beacon_methods(bid)

List Privesc methods

List available local privilege elevation techniques specific for running a Beacon.

Related CS Console Command: elevate

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.list_elevate_beacon_methods(
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

[**List[LocalExploitInfoDto]**](LocalExploitInfoDto.md)

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

# **list_token_store**
> AsyncCommandResponse list_token_store(bid)

List Tokens

List the tokens currently available in the token store for the specified Beacon.

Related CS Console Command: token-store show

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.list_token_store(
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

# **spawn_chrome_dump**
> AsyncCommandResponse spawn_chrome_dump(bid)

Chromedump (Spawn)

Spawn a temporary process to recover credential material from Google Chrome. This command will use Mimikatz to recover the credential material and should be run under a user context.

Related CS Console Command: chromedump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_chrome_dump(
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

# **spawn_dc_sync**
> AsyncCommandResponse spawn_dc_sync(bid, request_model)

DCSYNC (Spawn)

Spawn a temporary process to extract the NTLM password hash for domain users from the domain controller using mimikatz's DCSYNC. Specify a user to get their hash only.
This command requires a domain administrator trust relationship.

Related CS Console Command: dcsync

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_dc_sync(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.DcSyncSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**DcSyncSpawnDto**](DcSyncSpawnDto.md)|  | 

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

# **spawn_hash_dump**
> AsyncCommandResponse spawn_hash_dump(bid)

HashDump (Spawn)

Spawn a temporary process and inject an hashdump DLL into it. The hashdump DLL will dump password hashes (Warning: Injects into LSASS).
This action requires administrator privileges.

Related CS Console Command: hashdump

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_hash_dump(
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

# **spawn_logon_passwords**
> AsyncCommandResponse spawn_logon_passwords(bid)

Dump Credentials (Spawn)

Spawn a temporary process to dump plaintext credentials and NTLM hashes. This action uses mimikatz and requires administrator privileges.

Related CS Console Command: logonpasswords

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_logon_passwords(
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

# **spawn_mimikatz**
> AsyncCommandResponse spawn_mimikatz(bid, request_model)

Mimikatz (Spawn)

Spawn a temporary process to run a mimikatz command. 
Use ! to make mimikatz elevate to SYSTEM before it runs your command. Some commands require this.
Use @ to make mimikatz impersonate Beacon's thread token before it runs your command. This is helpful for mimikatz commands that interact with remote systems (e.g., lsadump::dcsync)
Use ; to separate multiple mimikatz commands.  The maximum length of the commands is 511 characters.
Command Example:   crypto::capi ; crypto::certificates /systemstore:local_machine /store:my /export.

Related CS Console Command: mimikatz

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_mimikatz(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.MimikatzSpawnDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**MimikatzSpawnDto**](MimikatzSpawnDto.md)|  | 

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

# **spawn_post_ex_dll**
> AsyncCommandResponse spawn_post_ex_dll(bid, request_model)

Execute PostEx DLL (Spawn)

Spawn a temporary process and inject the postex DLL into it.

Related CS Console Command: spawn

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_post_ex_dll(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ExecuteDllDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**|  | 
 **request_model** | [**ExecuteDllDto**](ExecuteDllDto.md)|  | 

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

# **spawn_run_command_no_output**
> AsyncCommandResponse spawn_run_command_no_output(bid, request_model)

Run without output (Spawn)

Execute the program (without a shell). Does not block or return output.

Related CS Console Command: execute

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import CredsAndTokensApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = CredsAndTokensApi(client)
        response = await api.spawn_run_command_no_output(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.ExecuteDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**ExecuteDto**](ExecuteDto.md)|  | 

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

