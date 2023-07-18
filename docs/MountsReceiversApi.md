# swagger_client.MountsReceiversApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receivers**](MountsReceiversApi.md#receivers) | **GET** /api/v2.1/mounts/{mountId}/receivers | TODO
[**receivers_create**](MountsReceiversApi.md#receivers_create) | **POST** /api/v2.1/mounts/{mountId}/receivers | TODO
[**receivers_delete**](MountsReceiversApi.md#receivers_delete) | **DELETE** /api/v2.1/mounts/{mountId}/receivers/{receiverId} | TODO
[**receivers_details**](MountsReceiversApi.md#receivers_details) | **GET** /api/v2.1/mounts/{mountId}/receivers/{receiverId} | TODO
[**receivers_remove_password**](MountsReceiversApi.md#receivers_remove_password) | **DELETE** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/password | TODO
[**receivers_reset_password**](MountsReceiversApi.md#receivers_reset_password) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/password/reset | TODO
[**receivers_set_alert**](MountsReceiversApi.md#receivers_set_alert) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/alert | TODO
[**receivers_set_message**](MountsReceiversApi.md#receivers_set_message) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/message | TODO
[**receivers_set_password**](MountsReceiversApi.md#receivers_set_password) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/password/set | TODO
[**receivers_set_url_hash**](MountsReceiversApi.md#receivers_set_url_hash) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/urlHash | TODO
[**receivers_set_validity**](MountsReceiversApi.md#receivers_set_validity) | **PUT** /api/v2.1/mounts/{mountId}/receivers/{receiverId}/validity | TODO

# **receivers**
> Receivers receivers(mount_id)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_response = api_instance.receivers(mount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

[**Receivers**](Receivers.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_create**
> Receiver receivers_create(mount_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
body = swagger_client.ReceiverCreate() # ReceiverCreate | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_create(mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **body** | [**ReceiverCreate**](ReceiverCreate.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_delete**
> receivers_delete(mount_id, receiver_id)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_instance.receivers_delete(mount_id, receiver_id)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_details**
> Receiver receivers_details(mount_id, receiver_id)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.receivers_details(mount_id, receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_remove_password**
> Receiver receivers_remove_password(mount_id, receiver_id)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.receivers_remove_password(mount_id, receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_remove_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_reset_password**
> Receiver receivers_reset_password(mount_id, receiver_id)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # TODO
    api_response = api_instance.receivers_reset_password(mount_id, receiver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_set_alert**
> Receiver receivers_set_alert(mount_id, receiver_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.ReceiverSetAlert() # ReceiverSetAlert | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_set_alert(mount_id, receiver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_set_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 
 **body** | [**ReceiverSetAlert**](ReceiverSetAlert.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_set_message**
> Receiver receivers_set_message(mount_id, receiver_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.ReceiverMessage() # ReceiverMessage | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_set_message(mount_id, receiver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_set_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 
 **body** | [**ReceiverMessage**](ReceiverMessage.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_set_password**
> Receiver receivers_set_password(mount_id, receiver_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.ReceiverSetPassword() # ReceiverSetPassword | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_set_password(mount_id, receiver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 
 **body** | [**ReceiverSetPassword**](ReceiverSetPassword.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_set_url_hash**
> Receiver receivers_set_url_hash(mount_id, receiver_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.ReceiverSetHash() # ReceiverSetHash | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_set_url_hash(mount_id, receiver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_set_url_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 
 **body** | [**ReceiverSetHash**](ReceiverSetHash.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receivers_set_validity**
> Receiver receivers_set_validity(mount_id, receiver_id, body=body)

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
api_instance = swagger_client.MountsReceiversApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
receiver_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.ReceiverValidity() # ReceiverValidity | TODO (optional)

try:
    # TODO
    api_response = api_instance.receivers_set_validity(mount_id, receiver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsReceiversApi->receivers_set_validity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **receiver_id** | [**str**](.md)|  | 
 **body** | [**ReceiverValidity**](ReceiverValidity.md)| TODO | [optional] 

### Return type

[**Receiver**](Receiver.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

