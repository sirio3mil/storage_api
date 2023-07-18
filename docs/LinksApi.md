# swagger_client.LinksApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**links_all**](LinksApi.md#links_all) | **GET** /api/v2.1/links | TODO

# **links_all**
> LinksBundle links_all()

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
api_instance = swagger_client.LinksApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_response = api_instance.links_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->links_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LinksBundle**](LinksBundle.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

