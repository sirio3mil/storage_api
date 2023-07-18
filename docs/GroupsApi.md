# swagger_client.GroupsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups**](GroupsApi.md#groups) | **GET** /api/v2.1/groups | TODO
[**groups_attributes**](GroupsApi.md#groups_attributes) | **GET** /api/v2.1/groups/{groupId}/attributes | TODO
[**groups_branding_logo_remove**](GroupsApi.md#groups_branding_logo_remove) | **DELETE** /api/v2.1/groups/{groupId}/branding/logo | TODO
[**groups_common_edit**](GroupsApi.md#groups_common_edit) | **PUT** /api/v2.1/groups/{groupId}/common | TODO
[**groups_content_groups_branding_logo**](GroupsApi.md#groups_content_groups_branding_logo) | **GET** /content/api/v2.1/groups/{groupId}/branding/logo | Get the group&#x27;s branding logo
[**groups_content_groups_branding_logo_update**](GroupsApi.md#groups_content_groups_branding_logo_update) | **POST** /content/api/v2.1/groups/{groupId}/branding/logo | Update the group&#x27;s branding logo.
[**groups_details**](GroupsApi.md#groups_details) | **GET** /api/v2.1/groups/{groupId} | TODO
[**groups_users_add**](GroupsApi.md#groups_users_add) | **POST** /api/v2.1/groups/{groupId}/users | TODO
[**groups_users_edit**](GroupsApi.md#groups_users_edit) | **PUT** /api/v2.1/groups/{groupId}/users/{groupUserId} | TODO
[**groups_users_remove**](GroupsApi.md#groups_users_remove) | **DELETE** /api/v2.1/groups/{groupId}/users/{groupUserId} | TODO

# **groups**
> Groups groups()

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_response = api_instance.groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Groups**](Groups.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_attributes**
> object groups_attributes(group_id)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.groups_attributes(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_branding_logo_remove**
> groups_branding_logo_remove(group_id)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.groups_branding_logo_remove(group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_branding_logo_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_common_edit**
> groups_common_edit(group_id, body=body)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.GroupCommonUpdate() # GroupCommonUpdate | TODO (optional)

try:
    # TODO
    api_instance.groups_common_edit(group_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_common_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 
 **body** | [**GroupCommonUpdate**](GroupCommonUpdate.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_content_groups_branding_logo**
> str groups_content_groups_branding_logo(group_id)

Get the group's branding logo

Response image can be a JPEG, PNG or GIF.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 

try:
    # Get the group's branding logo
    api_response = api_instance.groups_content_groups_branding_logo(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_content_groups_branding_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_content_groups_branding_logo_update**
> FilesFile groups_content_groups_branding_logo_update(group_id, body=body)

Update the group's branding logo.

The uploaded image must be smaller than 8 MB and will be automatically resized.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = 'group_id_example' # str | 
body = swagger_client.Object() # Object | New branding logo file (optional)

try:
    # Update the group's branding logo.
    api_response = api_instance.groups_content_groups_branding_logo_update(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_content_groups_branding_logo_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | **Object**| New branding logo file | [optional] 

### Return type

[**FilesFile**](FilesFile.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_details**
> Group groups_details(group_id)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.groups_details(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_users_add**
> GroupUser groups_users_add(group_id, body=body)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.GroupUserCreate() # GroupUserCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.groups_users_add(group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_users_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 
 **body** | [**GroupUserCreate**](GroupUserCreate.md)| TODO | [optional] 

### Return type

[**GroupUser**](GroupUser.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_users_edit**
> groups_users_edit(group_id, group_user_id, body=body)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
group_user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.GroupUserEdit() # GroupUserEdit | TODO (optional)

try:
    # TODO
    api_instance.groups_users_edit(group_id, group_user_id, body=body)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_users_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 
 **group_user_id** | [**str**](.md)|  | 
 **body** | [**GroupUserEdit**](GroupUserEdit.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_users_remove**
> groups_users_remove(group_id, group_user_id)

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
group_user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.groups_users_remove(group_id, group_user_id)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_users_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**str**](.md)|  | 
 **group_user_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

