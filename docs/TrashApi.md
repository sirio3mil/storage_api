# swagger_client.TrashApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trash**](TrashApi.md#trash) | **GET** /api/v2.1/trash | Get deleted files
[**trash_empty**](TrashApi.md#trash_empty) | **DELETE** /api/v2.1/trash | Empty trash
[**trash_undelete**](TrashApi.md#trash_undelete) | **POST** /api/v2.1/trash/undelete | Undelete files from trash

# **trash**
> Trash trash(cursor=cursor, page_size=page_size, sort_field=sort_field, sort_dir=sort_dir)

Get deleted files

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
api_instance = swagger_client.TrashApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | Page cursor (optional)
page_size = 1000 # int | Max number of items per page (optional) (default to 1000)
sort_field = 'name' # str | Sort field name (optional) (default to name)
sort_dir = 'asc' # str | Sort direction (default: asc) (optional) (default to asc)

try:
    # Get deleted files
    api_response = api_instance.trash(cursor=cursor, page_size=page_size, sort_field=sort_field, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashApi->trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Page cursor | [optional] 
 **page_size** | **int**| Max number of items per page | [optional] [default to 1000]
 **sort_field** | **str**| Sort field name | [optional] [default to name]
 **sort_dir** | **str**| Sort direction (default: asc) | [optional] [default to asc]

### Return type

[**Trash**](Trash.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trash_empty**
> Job trash_empty()

Empty trash

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
api_instance = swagger_client.TrashApi(swagger_client.ApiClient(configuration))

try:
    # Empty trash
    api_response = api_instance.trash_empty()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashApi->trash_empty: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trash_undelete**
> Job trash_undelete(body=body)

Undelete files from trash

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
api_instance = swagger_client.TrashApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobUndelete() # JobUndelete | Specific files can be undeleted by providing their mount ID and paths. If the files list is empty, all files will be undeleted. (optional)

try:
    # Undelete files from trash
    api_response = api_instance.trash_undelete(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrashApi->trash_undelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobUndelete**](JobUndelete.md)| Specific files can be undeleted by providing their mount ID and paths. If the files list is empty, all files will be undeleted. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

