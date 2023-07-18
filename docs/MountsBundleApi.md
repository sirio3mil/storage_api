# swagger_client.MountsBundleApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle**](MountsBundleApi.md#bundle) | **GET** /api/v2.1/mounts/{mountId}/bundle | TODO

# **bundle**
> Bundle bundle(mount_id, path)

TODO

TODO

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: appPassword
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.MountsBundleApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.bundle(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsBundleApi->bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

