# TaskDetailDtoResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**type** | **str** | Discriminator; fixed to &#39;jobs&#39;. | `[default to 'jobs']`
**jobs** | **List[JobInfoDto]** |  | 
**process_list** | **List[ProcessDto]** |  | 
**output** | **str** |  | 
**tokens** | **List[TokenWithPidDto]** |  | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


