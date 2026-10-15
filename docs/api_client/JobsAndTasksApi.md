# cs_sdk_python.api_client.JobsAndTasksApi

All URIs are relative to *https://localhost:50443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**error**](JobsAndTasksApi.md#error) | **POST** /api/v1/tasks/{taskId}/error | Log Error
[**execute_job_stop**](JobsAndTasksApi.md#execute_job_stop) | **POST** /api/v1/beacons/{bid}/execute/jobStop | Stop Job
[**get_task_by_id**](JobsAndTasksApi.md#get_task_by_id) | **GET** /api/v1/tasks/{taskId} | Get Task
[**list_jobs**](JobsAndTasksApi.md#list_jobs) | **POST** /api/v1/beacons/{bid}/state/jobs | List Active Jobs
[**list_task_summaries_by_bid**](JobsAndTasksApi.md#list_task_summaries_by_bid) | **GET** /api/v1/beacons/{bid}/tasks/summary | Get Beacon Tasks Summary
[**list_tasks**](JobsAndTasksApi.md#list_tasks) | **GET** /api/v1/tasks | List Tasks
[**list_tasks_by_bid**](JobsAndTasksApi.md#list_tasks_by_bid) | **GET** /api/v1/beacons/{bid}/tasks/detail | List Beacon Tasks
[**log**](JobsAndTasksApi.md#log) | **POST** /api/v1/tasks/{taskId}/log | Log Message


# **error**
> error(task_id, request_model)

Log Error

Publishes an error message to the Beacon/task transcript.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        await api.error(
            task_id='task_id_example',
            request_model=cs_sdk_python.api_client.PublishOutputDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task id | 
 **request_model** | [**PublishOutputDto**](PublishOutputDto.md)|  | 

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

# **execute_job_stop**
> AsyncCommandResponse execute_job_stop(bid, request_model)

Stop Job

Stop a specific job.

Related CS Console Command: jobkill

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.execute_job_stop(
            bid='bid_example',
            request_model=cs_sdk_python.api_client.JobKillDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon id | 
 **request_model** | [**JobKillDto**](JobKillDto.md)|  | 

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

# **get_task_by_id**
> TaskDetailDto get_task_by_id(task_id, format=format)

Get Task

Retrieve the detailed information for a specific task.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.get_task_by_id(
            task_id='task_id_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| ID of the task | 
 **format** | **str**| Select the output format | [optional] `[default to structured]`

### Return type

[**TaskDetailDto**](TaskDetailDto.md)

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

# **list_jobs**
> AsyncCommandResponse list_jobs(bid)

List Active Jobs

Lists jobs currently in progress.

Related CS Console Command: jobs

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.list_jobs(
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

# **list_task_summaries_by_bid**
> List[TaskSummaryDto] list_task_summaries_by_bid(bid)

Get Beacon Tasks Summary

Retrieve the summarized information / listing of all tasks for a specific Beacon.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.list_task_summaries_by_bid(
            bid='bid_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon ID | 

### Return type

[**List[TaskSummaryDto]**](TaskSummaryDto.md)

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

# **list_tasks**
> List[TaskSummaryDto] list_tasks()

List Tasks

Retrieve the summarized information / listing of all tasks.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.list_tasks()


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TaskSummaryDto]**](TaskSummaryDto.md)

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

# **list_tasks_by_bid**
> List[TaskDetailDto] list_tasks_by_bid(bid, format=format)

List Beacon Tasks

Retrieve the detailed information for Beacon's tasks.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        response = await api.list_tasks_by_bid(
            bid='bid_example',
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **bid** | **str**| Beacon ID | 
 **format** | **str**| Select the output format | [optional] `[default to structured]`

### Return type

[**List[TaskDetailDto]**](TaskDetailDto.md)

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

# **log**
> log(task_id, request_model)

Log Message

Publishes an output message to the Beacon/task transcript.

### Example

```python
import asyncio
import os

import cs_sdk_python.api_client
from cs_sdk_python.api_client import ApiClient, Configuration
from cs_sdk_python.api_client.api import JobsAndTasksApi


async def main():
    config = Configuration(host="https://localhost:50443")
    config.access_token = os.environ["CS_ACCESS_TOKEN"]
    async with ApiClient(config) as client:
        api = JobsAndTasksApi(client)
        await api.log(
            task_id='task_id_example',
            request_model=cs_sdk_python.api_client.PublishOutputDto(),
        )


asyncio.run(main())
```

Replace example values and populate the required model fields before running.


### Parameters


Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task id | 
 **request_model** | [**PublishOutputDto**](PublishOutputDto.md)|  | 

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

