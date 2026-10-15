# UserDefinedC2ListenerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the listener | 
**color** | **str** | Set the color that is used in the Cobalt Strike UI for the listener. | 
**error** | **str** | Error message indicating why the listener service failed | [optional] [readonly] 
**template** | **str** | Beacon templated used for the listener. | [optional] 
**port** | **int** | Port (Bind) | 
**local_host_only** | **bool** | Bind to localhost only | 
**debug_only** | **bool** | Debug only | 
**udc2_bof** | **str** | The file or artifact reference for a User Defined C2 BOF or BOF-PE | 
**files** | **Dict[str, str]** | Map of fileKey -&gt; base64 content. Required when the udc2Bof fields starts with &#39;@files/&#39;. | [optional] 
**guard_rails** | [**GuardRailsDto**](GuardRailsDto.md) | The guard rails settings to use for the listener | [optional] 
**payload** | **str** | Payload type | [optional] [readonly] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


