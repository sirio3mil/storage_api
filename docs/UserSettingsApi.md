# swagger_client.UserSettingsApi

All URIs are relative to *https://digistorage.es*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_language**](UserSettingsApi.md#settings_language) | **GET** /api/v2.1/user/settings/language | Get current preferred language
[**settings_language_edit**](UserSettingsApi.md#settings_language_edit) | **PUT** /api/v2.1/user/settings/language | Update current preferred language
[**settings_notifications**](UserSettingsApi.md#settings_notifications) | **GET** /api/v2.1/user/settings/notifications | Get notifications settings
[**settings_notifications_edit**](UserSettingsApi.md#settings_notifications_edit) | **PUT** /api/v2.1/user/settings/notifications | Update notification settings
[**settings_security**](UserSettingsApi.md#settings_security) | **GET** /api/v2.1/user/settings/security | Get security settings
[**settings_security_edit**](UserSettingsApi.md#settings_security_edit) | **PUT** /api/v2.1/user/settings/security | Update security settings
[**settings_seen**](UserSettingsApi.md#settings_seen) | **GET** /api/v2.1/user/settings/seen | Get seen settings
[**settings_seen_edit**](UserSettingsApi.md#settings_seen_edit) | **PUT** /api/v2.1/user/settings/seen | Update seen settings

# **settings_language**
> SettingsLanguage settings_language()

Get current preferred language

Get current preferred language. `User / App config` endpoint should be used for the current language (preferred, detected or default).

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get current preferred language
    api_response = api_instance.settings_language()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_language: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsLanguage**](SettingsLanguage.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_language_edit**
> settings_language_edit(body=body)

Update current preferred language

Set current preferred language. Valid languages can be obtained using `User / App config` endpoint.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsLanguage() # SettingsLanguage | New settings (optional)

try:
    # Update current preferred language
    api_instance.settings_language_edit(body=body)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_language_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsLanguage**](SettingsLanguage.md)| New settings | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications**
> SettingsNotifications settings_notifications()

Get notifications settings

Notification settings control whether the user wants to receive an email when new files are shared or a new comment is posted. Device offline setting is deprecated.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get notifications settings
    api_response = api_instance.settings_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_notifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsNotifications**](SettingsNotifications.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_notifications_edit**
> settings_notifications_edit(body=body)

Update notification settings

Notification settings control whether the user wants to receive an email when new files are shared or a new comment is posted.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsNotifications() # SettingsNotifications | New settings (optional)

try:
    # Update notification settings
    api_instance.settings_notifications_edit(body=body)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_notifications_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsNotifications**](SettingsNotifications.md)| New settings | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_security**
> SettingsSecurity settings_security()

Get security settings

Security settings are used to control automatic or mandatory passwords for links.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get security settings
    api_response = api_instance.settings_security()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_security: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsSecurity**](SettingsSecurity.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_security_edit**
> settings_security_edit(body=body)

Update security settings

Security settings are used to control automatic or mandatory passwords for links.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsSecurity() # SettingsSecurity | New settings (optional)

try:
    # Update security settings
    api_instance.settings_security_edit(body=body)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_security_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSecurity**](SettingsSecurity.md)| New settings | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_seen**
> SettingsSeen settings_seen()

Get seen settings

Seen settings are used for saving whether the current user has already seen the web Intro or Desktop app tip.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))

try:
    # Get seen settings
    api_response = api_instance.settings_seen()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_seen: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsSeen**](SettingsSeen.md)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_seen_edit**
> settings_seen_edit(body=body)

Update seen settings

Seen settings are used for saving whether the current user has already seen the web Intro or Desktop app tip. For partial updates non-changed fields should be `null`.

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
api_instance = swagger_client.UserSettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsSeen() # SettingsSeen | New settings (optional)

try:
    # Update seen settings
    api_instance.settings_seen_edit(body=body)
except ApiException as e:
    print("Exception when calling UserSettingsApi->settings_seen_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSeen**](SettingsSeen.md)| New settings | [optional] 

### Return type

void (empty response body)

### Authorization

[appPassword](../README.md#appPassword), [bearer](../README.md#bearer), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

