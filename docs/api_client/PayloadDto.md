# PayloadDto

Options for generating a stageless Payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listener_name** | **str** | The listener name | 
**use_listener_guard_rails** | **bool** | A flag to use the listener&#39;s guard rails (true) or the guard rails defined here (false) | 
**guard_rails** | [**GuardRailsDto**](GuardRailsDto.md) | The guard rails settings to use for the payload. The useListenerGuardRails must be set to &#39;false&#39; | [optional] 
**architecture** | **str** | The architecture of the payload (x86|x64) | 
**exit_function** | **str** | The method/behavior that Beacon uses when the exit command is executed. Use Process to to terminate the whole process or Thread to terminate the current thread.  | 
**system_call_method** | **str** | The system call method that Beacon uses when executing supported functions. | 
**http_library** | **str** | The Microsoft library (WinINet or WinHTTP) to use for HTTP(S) beacons. | [optional] 
**dns_comm_mode** | **str** | The DNS comm mode (dns or dns-over-https) to use for DNS beacons. | [optional] 
**output** | **str** | The output format to use when the payload is saved. | 
**payload_file_name** | **str** | The name the payload file will be saved to in the artifacts/generated location.  A name will automatically be generated when it is not set. | [optional] 
**sleep_mask_cna** | **str** | The sleep mask override script to use when generating the payload. | [optional] 
**udrl_cna** | **str** | The udrl override script to use when generating the payload. | [optional] 
**options** | **Dict[str, str]** | A user defined options map to pass to the hooks when generating the payload. | [optional] 
**malleable_override** | **str** | Malleable Override specified as a file resource (@files/filename.mpo). See associated &#39;files&#39; argument. | [optional] 
**hidden** | **bool** | A flag to hide the generated artifact in Payload Store | 
**files** | **Dict[str, str]** | Map of fileKey -&gt; base64 content. Required when the malleableOverride field starts with &#39;@files/&#39;. | [optional] 

[[Back to Model list]](README.md#documentation-for-models) [[Back to API list]](README.md#documentation-for-api-endpoints) [[Back to API reference]](README.md)


