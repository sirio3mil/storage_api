# swagger_client.UserProfilePictureApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_profile_picture_content_profile_picture**](UserProfilePictureApi.md#user_profile_picture_content_profile_picture) | **GET** /content/api/v2.1/user/profile-picture | Get user&#x27;s profile picture
[**user_profile_picture_content_profile_picture_update**](UserProfilePictureApi.md#user_profile_picture_content_profile_picture_update) | **POST** /content/api/v2.1/user/profile-picture/update | Update user&#x27;s profile picture.

# **user_profile_picture_content_profile_picture**
> str user_profile_picture_content_profile_picture(nodefault=nodefault)

Get user's profile picture

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
api_instance = swagger_client.UserProfilePictureApi(swagger_client.ApiClient(configuration))
nodefault = true # bool | Controls whether the response contains the default profile picture or 404 not found in case the user does not have a custom profile picture set. (optional)

try:
    # Get user's profile picture
    api_response = api_instance.user_profile_picture_content_profile_picture(nodefault=nodefault)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfilePictureApi->user_profile_picture_content_profile_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodefault** | **bool**| Controls whether the response contains the default profile picture or 404 not found in case the user does not have a custom profile picture set. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_profile_picture_content_profile_picture_update**
> FilesFile user_profile_picture_content_profile_picture_update(body=body)

Update user's profile picture.

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
api_instance = swagger_client.UserProfilePictureApi(swagger_client.ApiClient(configuration))
body = swagger_client.Object() # Object | New profile picture file (optional)

try:
    # Update user's profile picture.
    api_response = api_instance.user_profile_picture_content_profile_picture_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfilePictureApi->user_profile_picture_content_profile_picture_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| New profile picture file | [optional] 

### Return type

[**FilesFile**](FilesFile.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

