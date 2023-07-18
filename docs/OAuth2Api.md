# swagger_client.OAuth2Api

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_device_code**](OAuth2Api.md#oauth2_device_code) | **POST** /oauth2/devicecode | OAuth 2.0 Device Code Endpoint
[**oauth2_token**](OAuth2Api.md#oauth2_token) | **POST** /oauth2/token | OAuth 2.0 Token Endpoint

# **oauth2_device_code**
> oauth2_device_code()

OAuth 2.0 Device Code Endpoint

OAuth 2.0 endpoint for obtaining device code.

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
api_instance = swagger_client.OAuth2Api(swagger_client.ApiClient(configuration))

try:
    # OAuth 2.0 Device Code Endpoint
    api_instance.oauth2_device_code()
except ApiException as e:
    print("Exception when calling OAuth2Api->oauth2_device_code: %s\n" % e)
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

# **oauth2_token**
> oauth2_token()

OAuth 2.0 Token Endpoint

This endpoint should not be used called manually. An OAuth 2 library should be used for calls to this endpoint.

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
api_instance = swagger_client.OAuth2Api(swagger_client.ApiClient(configuration))

try:
    # OAuth 2.0 Token Endpoint
    api_instance.oauth2_token()
except ApiException as e:
    print("Exception when calling OAuth2Api->oauth2_token: %s\n" % e)
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

