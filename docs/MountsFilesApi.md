# swagger_client.MountsFilesApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_change_version**](MountsFilesApi.md#files_change_version) | **POST** /api/v2.1/mounts/{mountId}/files/versions/change | Change file version
[**files_content_files_get**](MountsFilesApi.md#files_content_files_get) | **GET** /content/api/v2.1/mounts/{mountId}/files/get | Download a file
[**files_content_files_get_multi**](MountsFilesApi.md#files_content_files_get_multi) | **POST** /content/api/v2.1/files/get | Download multiple files in a ZIP archive
[**files_content_files_get_multi_name**](MountsFilesApi.md#files_content_files_get_multi_name) | **POST** /content/api/v2.1/files/get/{name} | Download multiple files in a ZIP archive
[**files_content_files_get_name**](MountsFilesApi.md#files_content_files_get_name) | **GET** /content/api/v2.1/mounts/{mountId}/files/get/{name} | Download a file
[**files_content_files_get_name_post**](MountsFilesApi.md#files_content_files_get_name_post) | **POST** /content/api/v2.1/mounts/{mountId}/files/get/{name} | Download a folder with filtered files
[**files_content_files_get_post**](MountsFilesApi.md#files_content_files_get_post) | **POST** /content/api/v2.1/mounts/{mountId}/files/get | Download a folder with filtered files
[**files_content_files_list_recursive**](MountsFilesApi.md#files_content_files_list_recursive) | **GET** /content/api/v2.1/mounts/{mountId}/files/listrecursive | Get a recursive stream of files and folders
[**files_content_files_put**](MountsFilesApi.md#files_content_files_put) | **POST** /content/api/v2.1/mounts/{mountId}/files/put | Upload a file
[**files_copy**](MountsFilesApi.md#files_copy) | **PUT** /api/v2.1/mounts/{mountId}/files/copy | TODO
[**files_create**](MountsFilesApi.md#files_create) | **PUT** /api/v2.1/mounts/{mountId}/files/create/{template} | TODO
[**files_external**](MountsFilesApi.md#files_external) | **GET** /api/v2.1/mounts/{mountId}/files/external | TODO
[**files_external_status**](MountsFilesApi.md#files_external_status) | **GET** /api/v2.1/mounts/{mountId}/files/externalstatus | TODO
[**files_folder_new**](MountsFilesApi.md#files_folder_new) | **POST** /api/v2.1/mounts/{mountId}/files/folder | TODO
[**files_get**](MountsFilesApi.md#files_get) | **GET** /api/v2.1/mounts/{mountId}/files/get | TODO
[**files_get_link**](MountsFilesApi.md#files_get_link) | **GET** /api/v2.1/mounts/{mountId}/files/download | TODO
[**files_info**](MountsFilesApi.md#files_info) | **GET** /api/v2.1/mounts/{mountId}/files/info | TODO
[**files_list**](MountsFilesApi.md#files_list) | **GET** /api/v2.1/mounts/{mountId}/files/list | TODO
[**files_move**](MountsFilesApi.md#files_move) | **PUT** /api/v2.1/mounts/{mountId}/files/move | TODO
[**files_remove**](MountsFilesApi.md#files_remove) | **DELETE** /api/v2.1/mounts/{mountId}/files/remove | TODO
[**files_rename**](MountsFilesApi.md#files_rename) | **PUT** /api/v2.1/mounts/{mountId}/files/rename | TODO
[**files_tags_add**](MountsFilesApi.md#files_tags_add) | **POST** /api/v2.1/mounts/{mountId}/files/tags/add | TODO
[**files_tags_remove**](MountsFilesApi.md#files_tags_remove) | **POST** /api/v2.1/mounts/{mountId}/files/tags/remove | TODO
[**files_tags_set**](MountsFilesApi.md#files_tags_set) | **POST** /api/v2.1/mounts/{mountId}/files/tags/set | TODO
[**files_upload**](MountsFilesApi.md#files_upload) | **GET** /api/v2.1/mounts/{mountId}/files/upload | TODO
[**files_versions**](MountsFilesApi.md#files_versions) | **GET** /api/v2.1/mounts/{mountId}/files/versions | TODO
[**files_versions_recover**](MountsFilesApi.md#files_versions_recover) | **POST** /api/v2.1/mounts/{mountId}/files/versions/recover | TODO

# **files_change_version**
> files_change_version(mount_id, path, version)

Change file version

Replace a file with an older version

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 
version = 'version_example' # str | 

try:
    # Change file version
    api_instance.files_change_version(mount_id, path, version)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_change_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get**
> str files_content_files_get(mount_id, path, force=force)

Download a file

Download a file.

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 
force = true # bool | Forces the web browsers to download the file. Adds the `Content-Disposition: attachment; filename=\"file.txt\"; filename*=UTF-8''file.txt` header. (optional)

try:
    # Download a file
    api_response = api_instance.files_content_files_get(mount_id, path, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 
 **force** | **bool**| Forces the web browsers to download the file. Adds the &#x60;Content-Disposition: attachment; filename&#x3D;\&quot;file.txt\&quot;; filename*&#x3D;UTF-8&#x27;&#x27;file.txt&#x60; header. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get_multi**
> str files_content_files_get_multi(files=files)

Download multiple files in a ZIP archive

Download multiple files in a ZIP archive. 

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
files = ['files_example'] # list[str] |  (optional)

try:
    # Download multiple files in a ZIP archive
    api_response = api_instance.files_content_files_get_multi(files=files)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **files** | [**list[str]**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get_multi_name**
> str files_content_files_get_multi_name(name, files=files)

Download multiple files in a ZIP archive

Helper endpoint to include the name of the ZIP archive because web browsers use the last segment of the URL for the downloaded file name.

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 
files = ['files_example'] # list[str] |  (optional)

try:
    # Download multiple files in a ZIP archive
    api_response = api_instance.files_content_files_get_multi_name(name, files=files)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get_multi_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get_name**
> str files_content_files_get_name(mount_id, path, name, force=force)

Download a file

Helper endpoint to include the name of the file because web browsers use the last segment of the URL for the downloaded file name.

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 
name = 'name_example' # str | 
force = true # bool | Forces the web browsers to download the file. Adds the `Content-Disposition: attachment; filename=\"file.txt\"; filename*=UTF-8''file.txt` header. (optional)

try:
    # Download a file
    api_response = api_instance.files_content_files_get_name(mount_id, path, name, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 
 **name** | **str**|  | 
 **force** | **bool**| Forces the web browsers to download the file. Adds the &#x60;Content-Disposition: attachment; filename&#x3D;\&quot;file.txt\&quot;; filename*&#x3D;UTF-8&#x27;&#x27;file.txt&#x60; header. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get_name_post**
> str files_content_files_get_name_post(path, mount_id, name, files=files, force=force)

Download a folder with filtered files

Helper endpoint to include the name of the file because web browsers use the last segment of the URL for the downloaded file name.

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
name = 'name_example' # str | 
files = ['files_example'] # list[str] |  (optional)
force = true # bool | Forces the web browsers to download the file. Adds the `Content-Disposition: attachment; filename=\"file.txt\"; filename*=UTF-8''file.txt` header. (optional)

try:
    # Download a folder with filtered files
    api_response = api_instance.files_content_files_get_name_post(path, mount_id, name, files=files, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **name** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | [optional] 
 **force** | **bool**| Forces the web browsers to download the file. Adds the &#x60;Content-Disposition: attachment; filename&#x3D;\&quot;file.txt\&quot;; filename*&#x3D;UTF-8&#x27;&#x27;file.txt&#x60; header. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_get_post**
> str files_content_files_get_post(path, mount_id, files=files, force=force)

Download a folder with filtered files

Download a folder with filtered files.

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
files = ['files_example'] # list[str] |  (optional)
force = true # bool | Forces the web browsers to download the file. Adds the `Content-Disposition: attachment; filename=\"file.txt\"; filename*=UTF-8''file.txt` header. (optional)

try:
    # Download a folder with filtered files
    api_response = api_instance.files_content_files_get_post(path, mount_id, files=files, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **files** | [**list[str]**](str.md)|  | [optional] 
 **force** | **bool**| Forces the web browsers to download the file. Adds the &#x60;Content-Disposition: attachment; filename&#x3D;\&quot;file.txt\&quot;; filename*&#x3D;UTF-8&#x27;&#x27;file.txt&#x60; header. | [optional] 

### Return type

**str**

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/octet-stream, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_list_recursive**
> FilesListRecursiveItem files_content_files_list_recursive(mount_id, path)

Get a recursive stream of files and folders

 Get a recursive stream of files and folders.  ## Example response  ```json > GET /content/api/v2.1/mounts/f13b5804-563d-4aed-b831-ca0246a1cad1/files/listrecursive?path=/path/to/dir HTTP/1.1 > < HTTP/1.1 200 OK < Content-Type: application/x-ndjson; charset=utf-8 < Transfer-Encoding: chunked < {\"type\":\"file\",\"path\":\"/\",\"file\":{\"name\":\"1\",\"type\":\"dir\",\"modified\":1487861241075,\"size\":0,\"contentType\":\"\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/01ab.jpg\",\"file\":{\"name\":\"01ab.jpg\",\"type\":\"file\",\"modified\":1494936799097,\"size\":36494,\"contentType\":\"image/jpeg\",\"hash\":\"2eedb741f199ecc19f1ba815d3d9914d\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/10 (1).txt\",\"file\":{\"name\":\"10 (1).txt\",\"type\":\"file\",\"modified\":1559913936402,\"size\":3,\"contentType\":\"text/plain\",\"hash\":\"31d30eea8d0968d6458e0ad0027c9f80\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/2\",\"file\":{\"name\":\"2\",\"type\":\"dir\",\"modified\":1487861247967,\"size\":0,\"contentType\":\"\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/2/3\",\"file\":{\"name\":\"3\",\"type\":\"dir\",\"modified\":1487861253650,\"size\":0,\"contentType\":\"\",\"tags\":{}}} ```  ## Example response for an offline device  ```json > GET /content/api/v2.1/mounts/f13b5804-563d-4aed-b831-ca0246a1cad1/files/listrecursive?path=/path/to/dir HTTP/1.1 > < HTTP/1.1 404 Not Found < Content-Length: 115 < Content-Type: application/json; charset=utf-8 < {\"error\":{\"code\":\"DeviceOffline\",\"message\":\"Device is offline\"},\"requestId\":\"7d17fa00-eea6-40d6-4ea8-4ef1496530ae\"} ```  ## External devices  For external cloud devices list recursive only works if the device is synchronized. If the device is not synchronized the error code will be `FilesNotSynced`.  ## Errors  If an error occurs when list items have already been sent the response will end with an error item:  ```json > GET /content/api/v2.1/mounts/f13b5804-563d-4aed-b831-ca0246a1cad1/files/listrecursive?path=/path/to/dir HTTP/1.1 > < HTTP/1.1 200 OK < Content-Type: application/x-ndjson; charset=utf-8 < Transfer-Encoding: chunked < {\"type\":\"file\",\"path\":\"/\",\"file\":{\"name\":\"\",\"type\":\"dir\",\"modified\":1578316978020,\"size\":0,\"contentType\":\"\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/.bin\",\"file\":{\"name\":\".bin\",\"type\":\"dir\",\"modified\":1578316950052,\"size\":0,\"contentType\":\"\",\"tags\":{}}} {\"type\":\"file\",\"path\":\"/.bin/JSONStream\",\"file\":{\"name\":\"JSONStream\",\"type\":\"file\",\"modified\":1578316950024,\"size\":20,\"contentType\":\"application/octet-stream\",\"tags\":{}}} {\"type\":\"error\",\"error\":{\"code\":\"DeviceOffline\",\"message\":\"Device is offline\"}} ```  ## Paths  All paths in items are relative to the specified path. The first item is always an file info for the specified path which means that the first item will always have path `/`. 

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # Get a recursive stream of files and folders
    api_response = api_instance.files_content_files_list_recursive(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_list_recursive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesListRecursiveItem**](FilesListRecursiveItem.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson; charset=utf-8, application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_content_files_put**
> FilesFile files_content_files_put(path, mount_id, body=body, filename=filename, info=info, overwrite=overwrite, overwrite_if_modified=overwrite_if_modified, overwrite_if_size=overwrite_if_size, overwrite_if_hash=overwrite_if_hash, overwrite_ignore_nonexistent=overwrite_ignore_nonexistent, autorename=autorename, modified=modified, tags=tags)

Upload a file

File can be uploaded either using a multi-part form or directly. You can use Chunked transfer encoding if the size of the file is not known in advance (streaming upload).

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.Object() # Object | File (optional)
filename = 'filename_example' # str | Name of the uploaded file. If this parameter is not set and multipart body is used, the file name from the multipart body will be used (this parameter takes precedence). If raw request body is used this parameter is required. (optional)
info = false # bool | Return full file info (`FilesFile`) in the response. (optional) (default to false)
overwrite = false # bool | Overwrite an existing file. (optional) (default to false)
overwrite_if_modified = 1.2 # float | Overwrite an existing file if modified matches. (optional)
overwrite_if_size = 1.2 # float | Overwrite an existing file if size matches. (optional)
overwrite_if_hash = 'overwrite_if_hash_example' # str | Overwrite an existing file if hash matches. (optional)
overwrite_ignore_nonexistent = false # bool | Overwrite an existing file if other parameters match (e.g. overWriteIfModified) but create a new file if the old one does not exist. (optional) (default to false)
autorename = true # bool | Overwrite an existing file. (optional) (default to true)
modified = 1.2 # float | Set custom value for modified. Current time by default. (optional)
tags = ['tags_example'] # list[str] | Tags for the new file. Format: key=value (optional)

try:
    # Upload a file
    api_response = api_instance.files_content_files_put(path, mount_id, body=body, filename=filename, info=info, overwrite=overwrite, overwrite_if_modified=overwrite_if_modified, overwrite_if_size=overwrite_if_size, overwrite_if_hash=overwrite_if_hash, overwrite_ignore_nonexistent=overwrite_ignore_nonexistent, autorename=autorename, modified=modified, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_content_files_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | **Object**| File | [optional] 
 **filename** | **str**| Name of the uploaded file. If this parameter is not set and multipart body is used, the file name from the multipart body will be used (this parameter takes precedence). If raw request body is used this parameter is required. | [optional] 
 **info** | **bool**| Return full file info (&#x60;FilesFile&#x60;) in the response. | [optional] [default to false]
 **overwrite** | **bool**| Overwrite an existing file. | [optional] [default to false]
 **overwrite_if_modified** | **float**| Overwrite an existing file if modified matches. | [optional] 
 **overwrite_if_size** | **float**| Overwrite an existing file if size matches. | [optional] 
 **overwrite_if_hash** | **str**| Overwrite an existing file if hash matches. | [optional] 
 **overwrite_ignore_nonexistent** | **bool**| Overwrite an existing file if other parameters match (e.g. overWriteIfModified) but create a new file if the old one does not exist. | [optional] [default to false]
 **autorename** | **bool**| Overwrite an existing file. | [optional] [default to true]
 **modified** | **float**| Set custom value for modified. Current time by default. | [optional] 
 **tags** | [**list[str]**](str.md)| Tags for the new file. Format: key&#x3D;value | [optional] 

### Return type

[**FilesFile**](FilesFile.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_copy**
> FilesCopyResult files_copy(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesCopy() # FilesCopy | TODO (optional)

try:
    # TODO
    api_response = api_instance.files_copy(path, mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesCopy**](FilesCopy.md)| TODO | [optional] 

### Return type

[**FilesCopyResult**](FilesCopyResult.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_create**
> FilesCreateResult files_create(mount_id, path, template)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 
template = 'template_example' # str | 

try:
    # TODO
    api_response = api_instance.files_create(mount_id, path, template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 
 **template** | **str**|  | 

### Return type

[**FilesCreateResult**](FilesCreateResult.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_external**
> files_external(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_instance.files_external(mount_id, path)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_external: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_external_status**
> FilesExternalStatus files_external_status(mount_id)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 

try:
    # TODO
    api_response = api_instance.files_external_status(mount_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_external_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 

### Return type

[**FilesExternalStatus**](FilesExternalStatus.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_folder_new**
> files_folder_new(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesFolderCreate() # FilesFolderCreate | TODO (optional)

try:
    # TODO
    api_instance.files_folder_new(path, mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_folder_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesFolderCreate**](FilesFolderCreate.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get**
> files_get(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_instance.files_get(mount_id, path)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_get_link**
> FilesGetLink files_get_link(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_get_link(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_get_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesGetLink**](FilesGetLink.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_info**
> FilesFile files_info(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_info(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesFile**](FilesFile.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_list**
> Files files_list(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_list(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**Files**](Files.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_move**
> FilesMoveResult files_move(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesMove() # FilesMove | TODO (optional)

try:
    # TODO
    api_response = api_instance.files_move(path, mount_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_move: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesMove**](FilesMove.md)| TODO | [optional] 

### Return type

[**FilesMoveResult**](FilesMoveResult.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_remove**
> FilesRemove files_remove(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_remove(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesRemove**](FilesRemove.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_rename**
> files_rename(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesRename() # FilesRename | TODO (optional)

try:
    # TODO
    api_instance.files_rename(path, mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_rename: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesRename**](FilesRename.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_tags_add**
> files_tags_add(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesTagsAdd() # FilesTagsAdd | TODO (optional)

try:
    # TODO
    api_instance.files_tags_add(path, mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_tags_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesTagsAdd**](FilesTagsAdd.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_tags_remove**
> files_tags_remove(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesTagsRemove() # FilesTagsRemove | TODO (optional)

try:
    # TODO
    api_instance.files_tags_remove(path, mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_tags_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesTagsRemove**](FilesTagsRemove.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_tags_set**
> files_tags_set(path, mount_id, body=body)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
path = 'path_example' # str | 
mount_id = 'mount_id_example' # str | 
body = swagger_client.FilesTagsSet() # FilesTagsSet | TODO (optional)

try:
    # TODO
    api_instance.files_tags_set(path, mount_id, body=body)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_tags_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 
 **mount_id** | **str**|  | 
 **body** | [**FilesTagsSet**](FilesTagsSet.md)| TODO | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_upload**
> FilesUploadLink files_upload(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_upload(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesUploadLink**](FilesUploadLink.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_versions**
> FilesVersions files_versions(mount_id, path)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 

try:
    # TODO
    api_response = api_instance.files_versions(mount_id, path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 

### Return type

[**FilesVersions**](FilesVersions.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_versions_recover**
> FilesVersionsRecover files_versions_recover(mount_id, path, version)

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
api_instance = swagger_client.MountsFilesApi(swagger_client.ApiClient(configuration))
mount_id = 'mount_id_example' # str | 
path = 'path_example' # str | 
version = 'version_example' # str | 

try:
    # TODO
    api_response = api_instance.files_versions_recover(mount_id, path, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsFilesApi->files_versions_recover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_id** | **str**|  | 
 **path** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**FilesVersionsRecover**](FilesVersionsRecover.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

