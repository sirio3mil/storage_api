# swagger_client.MountsLinksApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**links**](MountsLinksApi.md#links) | **GET** /api/v2.1/mounts/{mountId}/links | TODO
[**links_counter**](MountsLinksApi.md#links_counter) | **GET** /api/v2.1/mounts/{mountId}/links/{linkId}/counter | TODO
[**links_create**](MountsLinksApi.md#links_create) | **POST** /api/v2.1/mounts/{mountId}/links | TODO
[**links_delete**](MountsLinksApi.md#links_delete) | **DELETE** /api/v2.1/mounts/{mountId}/links/{linkId} | TODO
[**links_details**](MountsLinksApi.md#links_details) | **GET** /api/v2.1/mounts/{mountId}/links/{linkId} | TODO
[**links_remove_password**](MountsLinksApi.md#links_remove_password) | **DELETE** /api/v2.1/mounts/{mountId}/links/{linkId}/password | TODO
[**links_reset_password**](MountsLinksApi.md#links_reset_password) | **PUT** /api/v2.1/mounts/{mountId}/links/{linkId}/password/reset | TODO
[**links_set_message**](MountsLinksApi.md#links_set_message) | **PUT** /api/v2.1/mounts/{mountId}/links/{linkId}/message | TODO
[**links_set_password**](MountsLinksApi.md#links_set_password) | **PUT** /api/v2.1/mounts/{mountId}/links/{linkId}/password/set | TODO
[**links_set_url_hash**](MountsLinksApi.md#links_set_url_hash) | **PUT** /api/v2.1/mounts/{mountId}/links/{linkId}/urlHash | TODO
[**links_set_validity**](MountsLinksApi.md#links_set_validity) | **PUT** /api/v2.1/mounts/{mountId}/links/{linkId}/validity | TODO

# **links**
> Links links(mount_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_response = api_instance.links(mount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

[**Links**](Links.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_counter**
> LinkCounter links_counter(mount_id, link_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.links_counter(mount_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 

### Return type

[**LinkCounter**](LinkCounter.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_create**
> Link links_create(mount_id, body=body)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.LinkCreate() # LinkCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.links_create(mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**LinkCreate**](LinkCreate.md)| TODO | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_delete**
> links_delete(mount_id, link_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.links_delete(mount_id, link_id)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_details**
> Link links_details(mount_id, link_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.links_details(mount_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_remove_password**
> Link links_remove_password(mount_id, link_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.links_remove_password(mount_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_remove_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_reset_password**
> Link links_reset_password(mount_id, link_id)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.links_reset_password(mount_id, link_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_set_message**
> Link links_set_message(mount_id, link_id, body=body)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.LinkMessage() # LinkMessage | TODO (optional)

try:
    # TODO
    api_response = api_instance.links_set_message(mount_id, link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_set_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 
 **body** | [**LinkMessage**](LinkMessage.md)| TODO | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_set_password**
> Link links_set_password(mount_id, link_id, body=body)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.LinkSetPassword() # LinkSetPassword | TODO (optional)

try:
    # TODO
    api_response = api_instance.links_set_password(mount_id, link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 
 **body** | [**LinkSetPassword**](LinkSetPassword.md)| TODO | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_set_url_hash**
> Link links_set_url_hash(mount_id, link_id, body=body)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.LinkSetHash() # LinkSetHash | TODO (optional)

try:
    # TODO
    api_response = api_instance.links_set_url_hash(mount_id, link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_set_url_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 
 **body** | [**LinkSetHash**](LinkSetHash.md)| TODO | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **links_set_validity**
> Link links_set_validity(mount_id, link_id, body=body)

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
api_instance = swagger_client.MountsLinksApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
link_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.LinkValidity() # LinkValidity | TODO (optional)

try:
    # TODO
    api_response = api_instance.links_set_validity(mount_id, link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsLinksApi->links_set_validity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **link_id** | [**str**](.md)|  | 
 **body** | [**LinkValidity**](LinkValidity.md)| TODO | [optional] 

### Return type

[**Link**](Link.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

