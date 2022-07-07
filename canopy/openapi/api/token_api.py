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


class TokenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def token_post_token(self, **kwargs):  # noqa: E501
        """token_post_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_post_token(async_req=True)
        >>> result = thread.get()

        :param grant_type:
        :type grant_type: str
        :param refresh_token:
        :type refresh_token: str
        :param username:
        :type username: str
        :param tenant:
        :type tenant: str
        :param password:
        :type password: str
        :param client_id:
        :type client_id: str
        :param client_secret:
        :type client_secret: str
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
        :rtype: GrantTypeHandlerResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.token_post_token_with_http_info(**kwargs)  # noqa: E501

    def token_post_token_with_http_info(self, **kwargs):  # noqa: E501
        """token_post_token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.token_post_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param grant_type:
        :type grant_type: str
        :param refresh_token:
        :type refresh_token: str
        :param username:
        :type username: str
        :param tenant:
        :type tenant: str
        :param password:
        :type password: str
        :param client_id:
        :type client_id: str
        :param client_secret:
        :type client_secret: str
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
        :rtype: tuple(GrantTypeHandlerResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'grant_type',
            'refresh_token',
            'username',
            'tenant',
            'password',
            'client_id',
            'client_secret'
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
                    " to method token_post_token" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}
        if 'grant_type' in local_var_params:
            form_params.append(('grant_type', local_var_params['grant_type']))  # noqa: E501
        if 'refresh_token' in local_var_params:
            form_params.append(('refresh_token', local_var_params['refresh_token']))  # noqa: E501
        if 'username' in local_var_params:
            form_params.append(('username', local_var_params['username']))  # noqa: E501
        if 'tenant' in local_var_params:
            form_params.append(('tenant', local_var_params['tenant']))  # noqa: E501
        if 'password' in local_var_params:
            form_params.append(('password', local_var_params['password']))  # noqa: E501
        if 'client_id' in local_var_params:
            form_params.append(('client_id', local_var_params['client_id']))  # noqa: E501
        if 'client_secret' in local_var_params:
            form_params.append(('client_secret', local_var_params['client_secret']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = []  # noqa: E501

        response_types_map = {
            200: "GrantTypeHandlerResponse",
        }

        return self.api_client.call_api(
            '/token', 'POST',
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
