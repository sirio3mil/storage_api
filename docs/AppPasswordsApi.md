# swagger_client.AppPasswordsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_passwords_generate**](AppPasswordsApi.md#app_passwords_generate) | **PUT** /api/v2.1/user/apw | TODO
[**app_passwords_list**](AppPasswordsApi.md#app_passwords_list) | **GET** /api/v2.1/user/apw | TODO
[**app_passwords_revoke**](AppPasswordsApi.md#app_passwords_revoke) | **DELETE** /api/v2.1/user/apw/{apwId} | TODO

# **app_passwords_generate**
> AppPassword app_passwords_generate(body=body)

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
api_instance = swagger_client.AppPasswordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AppPasswordGenerate() # AppPasswordGenerate | TODO (optional)

try:
    # TODO
    api_response = api_instance.app_passwords_generate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppPasswordsApi->app_passwords_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppPasswordGenerate**](AppPasswordGenerate.md)| TODO | [optional] 

### Return type

[**AppPassword**](AppPassword.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_passwords_list**
> AppPasswords app_passwords_list()

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
api_instance = swagger_client.AppPasswordsApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_response = api_instance.app_passwords_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppPasswordsApi->app_passwords_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppPasswords**](AppPasswords.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_passwords_revoke**
> app_passwords_revoke(apw_id)

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
api_instance = swagger_client.AppPasswordsApi(swagger_client.ApiClient(configuration))
apw_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.app_passwords_revoke(apw_id)
except ApiException as e:
    print("Exception when calling AppPasswordsApi->app_passwords_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apw_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

