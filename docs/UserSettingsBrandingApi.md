# swagger_client.UserSettingsBrandingApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branding_content_branding_logo**](UserSettingsBrandingApi.md#branding_content_branding_logo) | **GET** /content/api/v2.1/user/settings/branding/logo | Get the current user&#x27;s branding logo
[**branding_content_branding_logo_update**](UserSettingsBrandingApi.md#branding_content_branding_logo_update) | **POST** /content/api/v2.1/user/settings/branding/logo | Update the current user&#x27;s branding logo.
[**branding_logo_remove**](UserSettingsBrandingApi.md#branding_logo_remove) | **DELETE** /api/v2.1/user/settings/branding/logo | Remove the current user&#x27;s branding logo.

# **branding_content_branding_logo**
> str branding_content_branding_logo()

Get the current user's branding logo

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
api_instance = swagger_client.UserSettingsBrandingApi(swagger_client.ApiClient(configuration))

try:
    # Get the current user's branding logo
    api_response = api_instance.branding_content_branding_logo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsBrandingApi->branding_content_branding_logo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branding_content_branding_logo_update**
> FilesFile branding_content_branding_logo_update(body=body)

Update the current user's branding logo.

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
api_instance = swagger_client.UserSettingsBrandingApi(swagger_client.ApiClient(configuration))
body = swagger_client.Object() # Object | New branding logo file (optional)

try:
    # Update the current user's branding logo.
    api_response = api_instance.branding_content_branding_logo_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsBrandingApi->branding_content_branding_logo_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| New branding logo file | [optional] 

### Return type

[**FilesFile**](FilesFile.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branding_logo_remove**
> branding_logo_remove()

Remove the current user's branding logo.

Remove the current user's branding logo.

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
api_instance = swagger_client.UserSettingsBrandingApi(swagger_client.ApiClient(configuration))

try:
    # Remove the current user's branding logo.
    api_instance.branding_logo_remove()
except ApiException as e:
    print("Exception when calling UserSettingsBrandingApi->branding_logo_remove: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

