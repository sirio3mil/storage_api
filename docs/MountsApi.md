# swagger_client.MountsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mounts**](MountsApi.md#mounts) | **GET** /api/v2.1/mounts | List of places and shared folders.
[**mounts_delete**](MountsApi.md#mounts_delete) | **DELETE** /api/v2.1/mounts/{mountId} | TODO
[**mounts_details**](MountsApi.md#mounts_details) | **GET** /api/v2.1/mounts/{mountId} | TODO
[**mounts_edit**](MountsApi.md#mounts_edit) | **PUT** /api/v2.1/mounts/{mountId} | TODO
[**mounts_groups_add**](MountsApi.md#mounts_groups_add) | **PUT** /api/v2.1/mounts/{mountId}/groups/{mountGroupId} | TODO
[**mounts_groups_remove**](MountsApi.md#mounts_groups_remove) | **DELETE** /api/v2.1/mounts/{mountId}/groups/{mountGroupId} | TODO
[**mounts_reauth**](MountsApi.md#mounts_reauth) | **GET** /api/v2.1/mounts/{mountId}/reauth | TODO
[**mounts_submounts_create**](MountsApi.md#mounts_submounts_create) | **POST** /api/v2.1/mounts/{mountId}/submounts | TODO
[**mounts_users_add**](MountsApi.md#mounts_users_add) | **POST** /api/v2.1/mounts/{mountId}/users | TODO
[**mounts_users_edit**](MountsApi.md#mounts_users_edit) | **PUT** /api/v2.1/mounts/{mountId}/users/{mountUserId} | TODO
[**mounts_users_remove**](MountsApi.md#mounts_users_remove) | **DELETE** /api/v2.1/mounts/{mountId}/users/{mountUserId} | TODO

# **mounts**
> Mounts mounts()

List of places and shared folders.

Deprecated. Use Places or Shared.

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))

try:
    # List of places and shared folders.
    api_response = api_instance.mounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsApi->mounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Mounts**](Mounts.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_delete**
> mounts_delete(mount_id)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_instance.mounts_delete(mount_id)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_details**
> Mount mounts_details(mount_id)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_response = api_instance.mounts_details(mount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

[**Mount**](Mount.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_edit**
> mounts_edit(mount_id, body=body)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.MountEdit() # MountEdit | TODO (optional)

try:
    # TODO
    api_instance.mounts_edit(mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**MountEdit**](MountEdit.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_groups_add**
> mounts_groups_add(mount_id, mount_group_id, body=body)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
mount_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.MountGroupCreate() # MountGroupCreate | TODO (optional)

try:
    # TODO
    api_instance.mounts_groups_add(mount_id, mount_group_id, body=body)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_groups_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **mount_group_id** | [**str**](.md)|  | 
 **body** | [**MountGroupCreate**](MountGroupCreate.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_groups_remove**
> mounts_groups_remove(mount_id, mount_group_id)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
mount_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.mounts_groups_remove(mount_id, mount_group_id)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_groups_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **mount_group_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_reauth**
> mounts_reauth(mount_id)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_instance.mounts_reauth(mount_id)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_reauth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_submounts_create**
> Mount mounts_submounts_create(mount_id, body=body)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.MountCreate() # MountCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.mounts_submounts_create(mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_submounts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**MountCreate**](MountCreate.md)| TODO | [optional] 

### Return type

[**Mount**](Mount.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_users_add**
> MountUser mounts_users_add(mount_id, body=body)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.MountUserCreate() # MountUserCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.mounts_users_add(mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_users_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**MountUserCreate**](MountUserCreate.md)| TODO | [optional] 

### Return type

[**MountUser**](MountUser.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_users_edit**
> mounts_users_edit(mount_id, mount_user_id, body=body)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
mount_user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.MountUserEdit() # MountUserEdit | TODO (optional)

try:
    # TODO
    api_instance.mounts_users_edit(mount_id, mount_user_id, body=body)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_users_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **mount_user_id** | [**str**](.md)|  | 
 **body** | [**MountUserEdit**](MountUserEdit.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mounts_users_remove**
> mounts_users_remove(mount_id, mount_user_id)

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
mount_user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.mounts_users_remove(mount_id, mount_user_id)
except ApiException as e:
    print("Exception when calling MountsApi->mounts_users_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **mount_user_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

