# swagger_client.SearchApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /api/v2.1/search | Search files and folders

# **search**
> SearchResult search(query=query, offset=offset, limit=limit, sort_field=sort_field, sort_dir=sort_dir, mount_id=mount_id, path=path, content_type=content_type, file_type=file_type, tag=tag)

Search files and folders

Search returns search results in the `hits` list. Mounts are normalized and present on the root level to minimize the response size.

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Search query term (optional)
offset = 789 # int | Pagination offset (default: 0) (optional)
limit = 789 # int | Max number of search results (default: 256, max: 1000) (optional)
sort_field = 'sort_field_example' # str | Sort field name (optional)
sort_dir = 'sort_dir_example' # str | Sort direction (default: asc) (optional)
mount_id = 'mount_id_example' # str | Filter by mount ID (optional)
path = 'path_example' # str | Filter by path (`mountId` is required if `path` is specified) (optional)
content_type = 'content_type_example' # str | Filter by content type / mime type (optional)
file_type = 'file_type_example' # str | Filter by file type (optional)
tag = ['tag_example'] # list[str] | Filter by tag value (key=value pairs) (optional)

try:
    # Search files and folders
    api_response = api_instance.search(query=query, offset=offset, limit=limit, sort_field=sort_field, sort_dir=sort_dir, mount_id=mount_id, path=path, content_type=content_type, file_type=file_type, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query term | [optional] 
 **offset** | **int**| Pagination offset (default: 0) | [optional] 
 **limit** | **int**| Max number of search results (default: 256, max: 1000) | [optional] 
 **sort_field** | **str**| Sort field name | [optional] 
 **sort_dir** | **str**| Sort direction (default: asc) | [optional] 
 **mount_id** | **str**| Filter by mount ID | [optional] 
 **path** | **str**| Filter by path (&#x60;mountId&#x60; is required if &#x60;path&#x60; is specified) | [optional] 
 **content_type** | **str**| Filter by content type / mime type | [optional] 
 **file_type** | **str**| Filter by file type | [optional] 
 **tag** | [**list[str]**](str.md)| Filter by tag value (key&#x3D;value pairs) | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

