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


class GetStudiesQueryResultQueryResults(object):
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
        'continuation_token': 'str',
        'has_more_results': 'bool'
    }

    attribute_map = {
        'documents': 'documents',
        'continuation_token': 'continuationToken',
        'has_more_results': 'hasMoreResults'
    }

    def __init__(self, documents=None, continuation_token=None, has_more_results=None, local_vars_configuration=None):  # noqa: E501
        """GetStudiesQueryResultQueryResults - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._documents = None
        self._continuation_token = None
        self._has_more_results = None
        self.discriminator = None

        self.documents = documents
        self.continuation_token = continuation_token
        self.has_more_results = has_more_results

    @property
    def documents(self):
        """Gets the documents of this GetStudiesQueryResultQueryResults.  # noqa: E501


        :return: The documents of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :rtype: list[CanopyDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this GetStudiesQueryResultQueryResults.


        :param documents: The documents of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :type documents: list[CanopyDocument]
        """
        if self.local_vars_configuration.client_side_validation and documents is None:  # noqa: E501
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def continuation_token(self):
        """Gets the continuation_token of this GetStudiesQueryResultQueryResults.  # noqa: E501


        :return: The continuation_token of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this GetStudiesQueryResultQueryResults.


        :param continuation_token: The continuation_token of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :type continuation_token: str
        """

        self._continuation_token = continuation_token

    @property
    def has_more_results(self):
        """Gets the has_more_results of this GetStudiesQueryResultQueryResults.  # noqa: E501


        :return: The has_more_results of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :rtype: bool
        """
        return self._has_more_results

    @has_more_results.setter
    def has_more_results(self, has_more_results):
        """Sets the has_more_results of this GetStudiesQueryResultQueryResults.


        :param has_more_results: The has_more_results of this GetStudiesQueryResultQueryResults.  # noqa: E501
        :type has_more_results: bool
        """
        if self.local_vars_configuration.client_side_validation and has_more_results is None:  # noqa: E501
            raise ValueError("Invalid value for `has_more_results`, must not be `None`")  # noqa: E501

        self._has_more_results = has_more_results

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
        if not isinstance(other, GetStudiesQueryResultQueryResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStudiesQueryResultQueryResults):
            return True

        return self.to_dict() != other.to_dict()
