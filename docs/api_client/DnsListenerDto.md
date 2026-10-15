# DnsListenerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the listener | 
**color** | **str** | Set the color that is used in the Cobalt Strike UI for the listener. | 
**error** | **str** | Error message indicating why the listener service failed | [optional] [readonly] 
**template** | **str** | Beacon templated used for the listener. | [optional] 
**hosts** | **List[str]** | DNS Hosts | 
**host** | **str** | DNS Host (Stager) | 
**dns_bind_port** | **int** | DNS Port (Bind) | [optional] 
**host_rotation_strategy** | **str** | Host Rotation Strategy | [optional] 
**max_retry_strategy** | **str** | Max Retry Strategy specified using the following format: exit-[max_attempts]-[increase_attempts]-[duration][m,h,d] or none | [optional] 
**profile** | **str** | Profile variant name | [optional] 
**dns_resolver** | **str** | DNS Resolver | [optional] 
**guard_rails** | [**GuardRailsDto**](GuardRailsDto.md) | The guard rails settings to use for the listener | [optional] 
**dns_port** | **int** | DNS Port | [optional] [readonly] 
**payload** | **str** | Payload type | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


