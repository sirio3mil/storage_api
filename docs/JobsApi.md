# swagger_client.JobsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs**](JobsApi.md#jobs) | **GET** /api/v2.1/jobs | TODO
[**jobs_details**](JobsApi.md#jobs_details) | **GET** /api/v2.1/jobs/{jobId} | TODO
[**jobs_files_copy**](JobsApi.md#jobs_files_copy) | **POST** /api/v2.1/jobs/files/copy | TODO
[**jobs_files_import_link**](JobsApi.md#jobs_files_import_link) | **POST** /api/v2.1/jobs/files/importlink | TODO
[**jobs_files_move**](JobsApi.md#jobs_files_move) | **POST** /api/v2.1/jobs/files/move | TODO
[**jobs_files_remove**](JobsApi.md#jobs_files_remove) | **POST** /api/v2.1/jobs/files/remove | TODO
[**jobs_files_restore_snapshot**](JobsApi.md#jobs_files_restore_snapshot) | **POST** /api/v2.1/jobs/files/restoresnapshot | TODO
[**jobs_remove**](JobsApi.md#jobs_remove) | **DELETE** /api/v2.1/jobs/{jobId} | TODO
[**jobs_remove_completed**](JobsApi.md#jobs_remove_completed) | **DELETE** /api/v2.1/jobs/completed | TODO

# **jobs**
> Jobs jobs()

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_response = api_instance.jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Jobs**](Jobs.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_details**
> Job jobs_details(job_id)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
job_id = 789 # int | 

try:
    # TODO
    api_response = api_instance.jobs_details(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_files_copy**
> Job jobs_files_copy(body=body)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobCopy() # JobCopy | TODO (optional)

try:
    # TODO
    api_response = api_instance.jobs_files_copy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_files_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCopy**](JobCopy.md)| TODO | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_files_import_link**
> Job jobs_files_import_link(body=body)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobCopy() # JobCopy | TODO (optional)

try:
    # TODO
    api_response = api_instance.jobs_files_import_link(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_files_import_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCopy**](JobCopy.md)| TODO | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_files_move**
> Job jobs_files_move(body=body)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobCopy() # JobCopy | TODO (optional)

try:
    # TODO
    api_response = api_instance.jobs_files_move(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_files_move: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCopy**](JobCopy.md)| TODO | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_files_remove**
> Job jobs_files_remove(body=body)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobRemove() # JobRemove | TODO (optional)

try:
    # TODO
    api_response = api_instance.jobs_files_remove(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_files_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobRemove**](JobRemove.md)| TODO | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_files_restore_snapshot**
> Job jobs_files_restore_snapshot(body=body)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
body = swagger_client.JobCopy() # JobCopy | TODO (optional)

try:
    # TODO
    api_response = api_instance.jobs_files_restore_snapshot(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_files_restore_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCopy**](JobCopy.md)| TODO | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_remove**
> jobs_remove(job_id)

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))
job_id = 789 # int | 

try:
    # TODO
    api_instance.jobs_remove(job_id)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_remove_completed**
> jobs_remove_completed()

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
api_instance = swagger_client.JobsApi(swagger_client.ApiClient(configuration))

try:
    # TODO
    api_instance.jobs_remove_completed()
except ApiException as e:
    print("Exception when calling JobsApi->jobs_remove_completed: %s\n" % e)
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

