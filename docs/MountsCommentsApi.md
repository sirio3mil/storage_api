# swagger_client.MountsCommentsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments**](MountsCommentsApi.md#comments) | **GET** /api/v2.1/mounts/{mountId}/comments | TODO
[**comments_delete**](MountsCommentsApi.md#comments_delete) | **DELETE** /api/v2.1/mounts/{mountId}/comments/{commentId} | TODO
[**comments_details**](MountsCommentsApi.md#comments_details) | **GET** /api/v2.1/mounts/{mountId}/comments/{commentId} | TODO
[**comments_new**](MountsCommentsApi.md#comments_new) | **POST** /api/v2.1/mounts/{mountId}/comments | TODO
[**comments_range**](MountsCommentsApi.md#comments_range) | **GET** /api/v2.1/mounts/{mountId}/comments/range | TODO

# **comments**
> Comments comments(mount_id)

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
api_instance = swagger_client.MountsCommentsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_response = api_instance.comments(mount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsCommentsApi->comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

[**Comments**](Comments.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_delete**
> comments_delete(mount_id, comment_id)

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
api_instance = swagger_client.MountsCommentsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
comment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.comments_delete(mount_id, comment_id)
except ApiException as e:
    print("Exception when calling MountsCommentsApi->comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **comment_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_details**
> Comment comments_details(mount_id, comment_id)

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
api_instance = swagger_client.MountsCommentsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
comment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.comments_details(mount_id, comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsCommentsApi->comments_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **comment_id** | [**str**](.md)|  | 

### Return type

[**Comment**](Comment.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_new**
> Comment comments_new(mount_id, body=body)

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
api_instance = swagger_client.MountsCommentsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.CommentCreate() # CommentCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.comments_new(mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsCommentsApi->comments_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**CommentCreate**](CommentCreate.md)| TODO | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_range**
> Comments comments_range(mount_id, _from, limit)

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
api_instance = swagger_client.MountsCommentsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
_from = 56 # int | 
limit = 56 # int | 

try:
    # TODO
    api_response = api_instance.comments_range(mount_id, _from, limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsCommentsApi->comments_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **_from** | **int**|  | 
 **limit** | **int**|  | 

### Return type

[**Comments**](Comments.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

