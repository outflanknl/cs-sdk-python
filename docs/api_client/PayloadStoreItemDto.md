# PayloadStoreItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payload store item id | [optional] 
**name** | **str** | Payload store item name | [optional] 
**payload_type** | **int** | Payload type id | [optional] 
**payload_type_name** | **str** | Payload type name | [optional] 
**artifact_type** | **str** | Payload artifact type | [optional] 
**architecture** | **str** | Payload architecture | [optional] 
**listener_name** | **str** | Listener name associated with the payload | [optional] 
**file_size** | **int** | Payload file size in bytes | [optional] 
**shellcode_id** | **int** | Payload shellcode id | [optional] 
**timestamp** | **int** | Payload creation timestamp in milliseconds since epoch | [optional] 
**creator** | **str** | User that created the payload store item | [optional] 
**hidden** | **bool** | Whether this payload store item is hidden | [optional] 
**hashes** | [**HashesDto**](HashesDto.md) | Payload file hashes | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


