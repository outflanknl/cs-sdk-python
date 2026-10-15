# SmbListenerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the listener | 
**color** | **str** | Set the color that is used in the Cobalt Strike UI for the listener. | 
**error** | **str** | Error message indicating why the listener service failed | [optional] [readonly] 
**template** | **str** | Beacon templated used for the listener. | [optional] 
**pipename** | **str** | Pipename (C2): | 
**guard_rails** | [**GuardRailsDto**](GuardRailsDto.md) | The guard rails settings to use for the listener | [optional] 
**payload** | **str** | Payload type | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


