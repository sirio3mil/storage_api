# swagger_client.UserBookmarksApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmarks**](UserBookmarksApi.md#bookmarks) | **GET** /api/v2.1/user/bookmarks | TODO
[**bookmarks_create**](UserBookmarksApi.md#bookmarks_create) | **POST** /api/v2.1/user/bookmarks | TODO
[**bookmarks_edit**](UserBookmarksApi.md#bookmarks_edit) | **PUT** /api/v2.1/user/bookmarks | TODO
[**bookmarks_remove**](UserBookmarksApi.md#bookmarks_remove) | **DELETE** /api/v2.1/user/bookmarks | TODO

# **bookmarks**
> Bookmarks bookmarks()

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
api_instance = swagger_client.UserBookmarksApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_response = api_instance.bookmarks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBookmarksApi->bookmarks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Bookmarks**](Bookmarks.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_create**
> bookmarks_create(body=body)

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
api_instance = swagger_client.UserBookmarksApi(swagger_client.ApiClient(configuration))
body = swagger_client.Bookmark() # Bookmark | TODO (optional)

try:
    # TODO
    api_instance.bookmarks_create(body=body)
except ApiException as e:
    print("Exception when calling UserBookmarksApi->bookmarks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bookmark**](Bookmark.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_edit**
> Bookmarks bookmarks_edit(body=body)

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
api_instance = swagger_client.UserBookmarksApi(swagger_client.ApiClient(configuration))
body = swagger_client.Bookmarks() # Bookmarks | TODO (optional)

try:
    # TODO
    api_response = api_instance.bookmarks_edit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserBookmarksApi->bookmarks_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bookmarks**](Bookmarks.md)| TODO | [optional] 

### Return type

[**Bookmarks**](Bookmarks.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bookmarks_remove**
> bookmarks_remove(mount_id, path)

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
api_instance = swagger_client.UserBookmarksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_instance.bookmarks_remove(mount_id, path)
except ApiException as e:
    print("Exception when calling UserBookmarksApi->bookmarks_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

