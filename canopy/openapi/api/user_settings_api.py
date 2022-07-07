# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from canopy.openapi.api_client import ApiClient
from canopy.openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UserSettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_settings_get_user_settings(self, tenant_id, user_id, **kwargs):  # noqa: E501
        """user_settings_get_user_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_settings_get_user_settings(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        :param tenant_id: (required)
        :type tenant_id: str
        :param user_id: (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetUserSettingsQueryResult
        """
        kwargs['_return_http_data_only'] = True
        return self.user_settings_get_user_settings_with_http_info(tenant_id, user_id, **kwargs)  # noqa: E501

    def user_settings_get_user_settings_with_http_info(self, tenant_id, user_id, **kwargs):  # noqa: E501
        """user_settings_get_user_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_settings_get_user_settings_with_http_info(tenant_id, user_id, async_req=True)
        >>> result = thread.get()

        :param tenant_id: (required)
        :type tenant_id: str
        :param user_id: (required)
        :type user_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetUserSettingsQueryResult, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'tenant_id',
            'user_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_settings_get_user_settings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and local_var_params.get('tenant_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `tenant_id` when calling `user_settings_get_user_settings`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `user_settings_get_user_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenantId'] = local_var_params['tenant_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        response_types_map = {
            200: "GetUserSettingsQueryResult",
        }

        return self.api_client.call_api(
            '/user-settings/{tenantId}/{userId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def user_settings_put_user_settings(self, tenant_id, user_id, user_settings_put_user_settings_request, **kwargs):  # noqa: E501
        """user_settings_put_user_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_settings_put_user_settings(tenant_id, user_id, user_settings_put_user_settings_request, async_req=True)
        >>> result = thread.get()

        :param tenant_id: (required)
        :type tenant_id: str
        :param user_id: (required)
        :type user_id: str
        :param user_settings_put_user_settings_request: (required)
        :type user_settings_put_user_settings_request: UserSettingsPutUserSettingsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        return self.user_settings_put_user_settings_with_http_info(tenant_id, user_id, user_settings_put_user_settings_request, **kwargs)  # noqa: E501

    def user_settings_put_user_settings_with_http_info(self, tenant_id, user_id, user_settings_put_user_settings_request, **kwargs):  # noqa: E501
        """user_settings_put_user_settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.user_settings_put_user_settings_with_http_info(tenant_id, user_id, user_settings_put_user_settings_request, async_req=True)
        >>> result = thread.get()

        :param tenant_id: (required)
        :type tenant_id: str
        :param user_id: (required)
        :type user_id: str
        :param user_settings_put_user_settings_request: (required)
        :type user_settings_put_user_settings_request: UserSettingsPutUserSettingsRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'tenant_id',
            'user_id',
            'user_settings_put_user_settings_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_settings_put_user_settings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if self.api_client.client_side_validation and local_var_params.get('tenant_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `tenant_id` when calling `user_settings_put_user_settings`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `user_settings_put_user_settings`")  # noqa: E501
        # verify the required parameter 'user_settings_put_user_settings_request' is set
        if self.api_client.client_side_validation and local_var_params.get('user_settings_put_user_settings_request') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_settings_put_user_settings_request` when calling `user_settings_put_user_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in local_var_params:
            path_params['tenantId'] = local_var_params['tenant_id']  # noqa: E501
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_settings_put_user_settings_request' in local_var_params:
            body_params = local_var_params['user_settings_put_user_settings_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'],
                'PUT', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        response_types_map = {
            200: "str",
        }

        return self.api_client.call_api(
            '/user-settings/{tenantId}/{userId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
