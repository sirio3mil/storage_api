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


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search(self, **kwargs):  # noqa: E501
        """Search files and folders  # noqa: E501

        Search returns search results in the `hits` list. Mounts are normalized and present on the root level to minimize the response size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query term
        :param int offset: Pagination offset (default: 0)
        :param int limit: Max number of search results (default: 256, max: 1000)
        :param str sort_field: Sort field name
        :param str sort_dir: Sort direction (default: asc)
        :param str mount_id: Filter by mount ID
        :param str path: Filter by path (`mountId` is required if `path` is specified)
        :param str content_type: Filter by content type / mime type
        :param str file_type: Filter by file type
        :param list[str] tag: Filter by tag value (key=value pairs)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_with_http_info(self, **kwargs):  # noqa: E501
        """Search files and folders  # noqa: E501

        Search returns search results in the `hits` list. Mounts are normalized and present on the root level to minimize the response size.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query term
        :param int offset: Pagination offset (default: 0)
        :param int limit: Max number of search results (default: 256, max: 1000)
        :param str sort_field: Sort field name
        :param str sort_dir: Sort direction (default: asc)
        :param str mount_id: Filter by mount ID
        :param str path: Filter by path (`mountId` is required if `path` is specified)
        :param str content_type: Filter by content type / mime type
        :param str file_type: Filter by file type
        :param list[str] tag: Filter by tag value (key=value pairs)
        :return: SearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'offset', 'limit', 'sort_field', 'sort_dir', 'mount_id', 'path', 'content_type', 'file_type', 'tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))  # noqa: E501
        if 'sort_dir' in params:
            query_params.append(('sortDir', params['sort_dir']))  # noqa: E501
        if 'mount_id' in params:
            query_params.append(('mountId', params['mount_id']))  # noqa: E501
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'content_type' in params:
            query_params.append(('contentType', params['content_type']))  # noqa: E501
        if 'file_type' in params:
            query_params.append(('fileType', params['file_type']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
            collection_formats['tag'] = 'multi'  # noqa: E501

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
            '/api/v2.1/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
