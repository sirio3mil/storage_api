# swagger_client.UsersProfilePicturesApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_profile_picture_content_profile_picture**](UsersProfilePicturesApi.md#users_profile_picture_content_profile_picture) | **GET** /content/api/v2.1/users/{userId}/profile-picture | Get a user&#x27;s profile picture

# **users_profile_picture_content_profile_picture**
> str users_profile_picture_content_profile_picture(user_id, nodefault=nodefault)

Get a user's profile picture

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
api_instance = swagger_client.UsersProfilePicturesApi(swagger_client.ApiClient(configuration))
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
nodefault = true # bool | Controls whether the response contains the default profile picture or 404 not found in case the user does not have a custom profile picture set. (optional)

try:
    # Get a user's profile picture
    api_response = api_instance.users_profile_picture_content_profile_picture(user_id, nodefault=nodefault)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersProfilePicturesApi->users_profile_picture_content_profile_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 
 **nodefault** | **bool**| Controls whether the response contains the default profile picture or 404 not found in case the user does not have a custom profile picture set. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

