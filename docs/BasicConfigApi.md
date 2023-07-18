# swagger_client.BasicConfigApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basic_config**](BasicConfigApi.md#basic_config) | **GET** /api/v2.1/basicconfig | Basic application configuration

# **basic_config**
> BasicConfig basic_config()

Basic application configuration

Get basic application configuration.

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
api_instance = swagger_client.BasicConfigApi(swagger_client.ApiClient(configuration))

try:
    # Basic application configuration
    api_response = api_instance.basic_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasicConfigApi->basic_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BasicConfig**](BasicConfig.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

