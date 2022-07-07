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


class MembershipPostIdentifiedUserRequest(object):
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
        'is_update': 'bool',
        'tenant': 'str',
        'username': 'str',
        'email': 'str'
    }

    attribute_map = {
        'is_update': 'isUpdate',
        'tenant': 'tenant',
        'username': 'username',
        'email': 'email'
    }

    def __init__(self, is_update=None, tenant=None, username=None, email=None, local_vars_configuration=None):  # noqa: E501
        """MembershipPostIdentifiedUserRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_update = None
        self._tenant = None
        self._username = None
        self._email = None
        self.discriminator = None

        if is_update is not None:
            self.is_update = is_update
        self.tenant = tenant
        self.username = username
        self.email = email

    @property
    def is_update(self):
        """Gets the is_update of this MembershipPostIdentifiedUserRequest.  # noqa: E501


        :return: The is_update of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_update

    @is_update.setter
    def is_update(self, is_update):
        """Sets the is_update of this MembershipPostIdentifiedUserRequest.


        :param is_update: The is_update of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :type is_update: bool
        """

        self._is_update = is_update

    @property
    def tenant(self):
        """Gets the tenant of this MembershipPostIdentifiedUserRequest.  # noqa: E501


        :return: The tenant of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this MembershipPostIdentifiedUserRequest.


        :param tenant: The tenant of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :type tenant: str
        """

        self._tenant = tenant

    @property
    def username(self):
        """Gets the username of this MembershipPostIdentifiedUserRequest.  # noqa: E501


        :return: The username of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MembershipPostIdentifiedUserRequest.


        :param username: The username of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this MembershipPostIdentifiedUserRequest.  # noqa: E501


        :return: The email of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MembershipPostIdentifiedUserRequest.


        :param email: The email of this MembershipPostIdentifiedUserRequest.  # noqa: E501
        :type email: str
        """

        self._email = email

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
        if not isinstance(other, MembershipPostIdentifiedUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MembershipPostIdentifiedUserRequest):
            return True

        return self.to_dict() != other.to_dict()
