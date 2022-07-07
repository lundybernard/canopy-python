# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from canopy.openapi.configuration import Configuration


class GetAllSupportSessionsQueryResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'documents': 'list[CanopyDocument]',
        'user_information': 'GetAllSupportSessionsQueryResultUserInformation',
        'query_metadata': 'list[SupportSessionsRequestMetadata]'
    }

    attribute_map = {
        'documents': 'documents',
        'user_information': 'userInformation',
        'query_metadata': 'queryMetadata'
    }

    def __init__(self, documents=None, user_information=None, query_metadata=None, local_vars_configuration=None):  # noqa: E501
        """GetAllSupportSessionsQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._documents = None
        self._user_information = None
        self._query_metadata = None
        self.discriminator = None

        self.documents = documents
        self.user_information = user_information
        self.query_metadata = query_metadata

    @property
    def documents(self):
        """Gets the documents of this GetAllSupportSessionsQueryResult.  # noqa: E501


        :return: The documents of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :rtype: list[CanopyDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this GetAllSupportSessionsQueryResult.


        :param documents: The documents of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :type documents: list[CanopyDocument]
        """
        if self.local_vars_configuration.client_side_validation and documents is None:  # noqa: E501
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def user_information(self):
        """Gets the user_information of this GetAllSupportSessionsQueryResult.  # noqa: E501


        :return: The user_information of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :rtype: GetAllSupportSessionsQueryResultUserInformation
        """
        return self._user_information

    @user_information.setter
    def user_information(self, user_information):
        """Sets the user_information of this GetAllSupportSessionsQueryResult.


        :param user_information: The user_information of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :type user_information: GetAllSupportSessionsQueryResultUserInformation
        """
        if self.local_vars_configuration.client_side_validation and user_information is None:  # noqa: E501
            raise ValueError("Invalid value for `user_information`, must not be `None`")  # noqa: E501

        self._user_information = user_information

    @property
    def query_metadata(self):
        """Gets the query_metadata of this GetAllSupportSessionsQueryResult.  # noqa: E501


        :return: The query_metadata of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :rtype: list[SupportSessionsRequestMetadata]
        """
        return self._query_metadata

    @query_metadata.setter
    def query_metadata(self, query_metadata):
        """Sets the query_metadata of this GetAllSupportSessionsQueryResult.


        :param query_metadata: The query_metadata of this GetAllSupportSessionsQueryResult.  # noqa: E501
        :type query_metadata: list[SupportSessionsRequestMetadata]
        """
        if self.local_vars_configuration.client_side_validation and query_metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `query_metadata`, must not be `None`")  # noqa: E501

        self._query_metadata = query_metadata

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetAllSupportSessionsQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetAllSupportSessionsQueryResult):
            return True

        return self.to_dict() != other.to_dict()
