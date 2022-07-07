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


class SupportSession(object):
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
        'is_open': 'bool',
        'modified_date': 'datetime',
        'modified_tenant_id': 'object',
        'modified_user_id': 'object',
        'responses': 'list[SupportSessionResponse]'
    }

    attribute_map = {
        'is_open': 'isOpen',
        'modified_date': 'modifiedDate',
        'modified_tenant_id': 'modifiedTenantId',
        'modified_user_id': 'modifiedUserId',
        'responses': 'responses'
    }

    def __init__(self, is_open=None, modified_date=None, modified_tenant_id=None, modified_user_id=None, responses=None, local_vars_configuration=None):  # noqa: E501
        """SupportSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_open = None
        self._modified_date = None
        self._modified_tenant_id = None
        self._modified_user_id = None
        self._responses = None
        self.discriminator = None

        self.is_open = is_open
        self.modified_date = modified_date
        self.modified_tenant_id = modified_tenant_id
        self.modified_user_id = modified_user_id
        self.responses = responses

    @property
    def is_open(self):
        """Gets the is_open of this SupportSession.  # noqa: E501


        :return: The is_open of this SupportSession.  # noqa: E501
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this SupportSession.


        :param is_open: The is_open of this SupportSession.  # noqa: E501
        :type is_open: bool
        """
        if self.local_vars_configuration.client_side_validation and is_open is None:  # noqa: E501
            raise ValueError("Invalid value for `is_open`, must not be `None`")  # noqa: E501

        self._is_open = is_open

    @property
    def modified_date(self):
        """Gets the modified_date of this SupportSession.  # noqa: E501


        :return: The modified_date of this SupportSession.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this SupportSession.


        :param modified_date: The modified_date of this SupportSession.  # noqa: E501
        :type modified_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_date is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_date`, must not be `None`")  # noqa: E501

        self._modified_date = modified_date

    @property
    def modified_tenant_id(self):
        """Gets the modified_tenant_id of this SupportSession.  # noqa: E501


        :return: The modified_tenant_id of this SupportSession.  # noqa: E501
        :rtype: object
        """
        return self._modified_tenant_id

    @modified_tenant_id.setter
    def modified_tenant_id(self, modified_tenant_id):
        """Sets the modified_tenant_id of this SupportSession.


        :param modified_tenant_id: The modified_tenant_id of this SupportSession.  # noqa: E501
        :type modified_tenant_id: object
        """
        if self.local_vars_configuration.client_side_validation and modified_tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_tenant_id`, must not be `None`")  # noqa: E501

        self._modified_tenant_id = modified_tenant_id

    @property
    def modified_user_id(self):
        """Gets the modified_user_id of this SupportSession.  # noqa: E501


        :return: The modified_user_id of this SupportSession.  # noqa: E501
        :rtype: object
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        """Sets the modified_user_id of this SupportSession.


        :param modified_user_id: The modified_user_id of this SupportSession.  # noqa: E501
        :type modified_user_id: object
        """
        if self.local_vars_configuration.client_side_validation and modified_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_user_id`, must not be `None`")  # noqa: E501

        self._modified_user_id = modified_user_id

    @property
    def responses(self):
        """Gets the responses of this SupportSession.  # noqa: E501


        :return: The responses of this SupportSession.  # noqa: E501
        :rtype: list[SupportSessionResponse]
        """
        return self._responses

    @responses.setter
    def responses(self, responses):
        """Sets the responses of this SupportSession.


        :param responses: The responses of this SupportSession.  # noqa: E501
        :type responses: list[SupportSessionResponse]
        """

        self._responses = responses

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
        if not isinstance(other, SupportSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportSession):
            return True

        return self.to_dict() != other.to_dict()
