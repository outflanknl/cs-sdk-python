# HttpListenerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the listener | 
**color** | **str** | Set the color that is used in the Cobalt Strike UI for the listener. | 
**error** | **str** | Error message indicating why the listener service failed | [optional] [readonly] 
**template** | **str** | Beacon templated used for the listener. | [optional] 
**hosts** | **List[str]** | HTTP Hosts | 
**host** | **str** | HTTP Host (Stager) | 
**http_port** | **int** | HTTP Port (C2) | [optional] 
**http_bind_port** | **int** | HTTP Port (Bind) | [optional] 
**http_host_header** | **str** | HTTP Host Header | [optional] 
**host_rotation_strategy** | **str** | Host Rotation Strategy | [optional] 
**max_retry_strategy** | **str** | Max Retry Strategy specified using the following format: exit-[max_attempts]-[increase_attempts]-[duration][m,h,d] or none | [optional] 
**profile** | **str** | Profile variant name | [optional] 
**ignore_proxy_settings** | **bool** | Set to true to use a direct connection. Set to false to use the http proxy settings. | 
**http_proxy** | [**ProxyDto**](ProxyDto.md) | Override the default behavior to use the Internet Explorer proxy configuration for the current process/user context by configuring the proxy settings. | [optional] 
**guard_rails** | [**GuardRailsDto**](GuardRailsDto.md) | The guard rails settings to use for the listener | [optional] 
**payload** | **str** | Payload type | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


