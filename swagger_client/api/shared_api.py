# coding: utf-8

"""
    DIGI storage API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SharedApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def shared(self, **kwargs):  # noqa: E501
        """TODO  # noqa: E501

        TODO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shared(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Shared
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shared_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.shared_with_http_info(**kwargs)  # noqa: E501
            return data

    def shared_with_http_info(self, **kwargs):  # noqa: E501
        """TODO  # noqa: E501

        TODO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shared_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Shared
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shared" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['appPassword', 'bearer', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2.1/shared', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Shared',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def shared_details(self, mount_id, **kwargs):  # noqa: E501
        """TODO  # noqa: E501

        TODO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shared_details(mount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mount_id: (required)
        :return: SharedFile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shared_details_with_http_info(mount_id, **kwargs)  # noqa: E501
        else:
            (data) = self.shared_details_with_http_info(mount_id, **kwargs)  # noqa: E501
            return data

    def shared_details_with_http_info(self, mount_id, **kwargs):  # noqa: E501
        """TODO  # noqa: E501

        TODO  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shared_details_with_http_info(mount_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str mount_id: (required)
        :return: SharedFile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mount_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shared_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'mount_id' is set
        if ('mount_id' not in params or
                params['mount_id'] is None):
            raise ValueError("Missing the required parameter `mount_id` when calling `shared_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'mount_id' in params:
            path_params['mountId'] = params['mount_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['appPassword', 'bearer', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2.1/shared/{mountId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SharedFile',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)