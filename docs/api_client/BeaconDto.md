# BeaconDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid** | **str** | Beacon id which associates tasks and metadata to a session. | 
**pbid** | **str** | Beacon id of the parent Beacon that it is communicating through. | [optional] 
**pid** | **int** | Process id that beacon is running under. | [optional] 
**process** | **str** | Process name that beacon is running under. | [optional] 
**user** | **str** | User name that beacon is running under. | [optional] 
**impersonated** | **str** | Impersonation information beacon is currently using. | [optional] 
**is_admin** | **bool** | A flag indicating the beacon is running as an administrator. | [optional] 
**computer** | **str** | Computer name where beacon is executing. | [optional] 
**host** | **str** | Host IP where beacon is executing. | [optional] 
**internal** | **str** | Internal IP where beacon is executing. | [optional] 
**external** | **str** | External IP where beacon is executing. | [optional] 
**os** | **str** | Hosts operating system. | [optional] 
**version** | **str** | Hosts operating system version. | [optional] 
**build** | **int** | Hosts operating system build number. | [optional] 
**charset** | **str** | Specifies the character encoding used to interpret or store text data. | [optional] 
**system_arch** | **str** | The CPU architecture of the host system as x86 or x64. | [optional] 
**beacon_arch** | **str** | The bitness of the process where beacon is running as x86 or x64. | [optional] 
**session** | **str** | The type of session beacon is running as beacon or ssh. | 
**listener** | **str** | The egress listener name beacon is communicating with. | [optional] 
**pivot_hint** | **str** | The pivot hints for pivot beacons only | [optional] 
**port** | **int** | The port number for ssh beacons only | [optional] 
**note** | **str** | The note associated with the beacon | [optional] 
**color** | **str** | The color associated with the beacon | [optional] 
**alive** | **bool** | A flag indicating beacon is still active | 
**link_state** | **str** | The status of a link for a pivot beacon. | [optional] 
**last_checkin_time** | **datetime** | The time stamp for the last check-in for the beacon | 
**last_checkin_ms** | **int** | The difference in time in milliseconds between the last check-in and now. | 
**last_checkin_formatted** | **str** | The difference using a formated time between the last check-in and now. | 
**sleep** | [**SleepDto**](SleepDto.md) |  | 
**supports_sleep** | **bool** | A flag indicating that beacon supports the sleep command | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


