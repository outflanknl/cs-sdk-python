# PortScanInjectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pid** | **int** |  | 
**arch** | **str** |  | 
**targets** | **List[str]** | List of hosts to scan. You may also specify IPv4 address ranges (e.g., 192.168.1.128-192.168.2.240, 192.168.1.0/24) | 
**ports** | **List[str]** | List of ports to scan. You may specify port ranges as well (e.g., 1-65536 | 
**method** | **str** | Dictate how the port scanning tool will determine if a host is alive | 
**max_connections** | **int** | limits how many connections the port scan tool will attempt at any one time | 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


