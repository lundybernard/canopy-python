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


class ConfigTypeMetadata(object):
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
        'singular_key': 'object',
        'plural_key': 'str',
        'name': 'str',
        'title_name': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'singular_key': 'singularKey',
        'plural_key': 'pluralKey',
        'name': 'name',
        'title_name': 'titleName',
        'icon': 'icon'
    }

    def __init__(self, singular_key=None, plural_key=None, name=None, title_name=None, icon=None, local_vars_configuration=None):  # noqa: E501
        """ConfigTypeMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._singular_key = None
        self._plural_key = None
        self._name = None
        self._title_name = None
        self._icon = None
        self.discriminator = None

        self.singular_key = singular_key
        self.plural_key = plural_key
        self.name = name
        self.title_name = title_name
        self.icon = icon

    @property
    def singular_key(self):
        """Gets the singular_key of this ConfigTypeMetadata.  # noqa: E501


        :return: The singular_key of this ConfigTypeMetadata.  # noqa: E501
        :rtype: object
        """
        return self._singular_key

    @singular_key.setter
    def singular_key(self, singular_key):
        """Sets the singular_key of this ConfigTypeMetadata.


        :param singular_key: The singular_key of this ConfigTypeMetadata.  # noqa: E501
        :type singular_key: object
        """
        if self.local_vars_configuration.client_side_validation and singular_key is None:  # noqa: E501
            raise ValueError("Invalid value for `singular_key`, must not be `None`")  # noqa: E501

        self._singular_key = singular_key

    @property
    def plural_key(self):
        """Gets the plural_key of this ConfigTypeMetadata.  # noqa: E501


        :return: The plural_key of this ConfigTypeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._plural_key

    @plural_key.setter
    def plural_key(self, plural_key):
        """Sets the plural_key of this ConfigTypeMetadata.


        :param plural_key: The plural_key of this ConfigTypeMetadata.  # noqa: E501
        :type plural_key: str
        """
        if self.local_vars_configuration.client_side_validation and plural_key is None:  # noqa: E501
            raise ValueError("Invalid value for `plural_key`, must not be `None`")  # noqa: E501

        self._plural_key = plural_key

    @property
    def name(self):
        """Gets the name of this ConfigTypeMetadata.  # noqa: E501


        :return: The name of this ConfigTypeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigTypeMetadata.


        :param name: The name of this ConfigTypeMetadata.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title_name(self):
        """Gets the title_name of this ConfigTypeMetadata.  # noqa: E501


        :return: The title_name of this ConfigTypeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._title_name

    @title_name.setter
    def title_name(self, title_name):
        """Sets the title_name of this ConfigTypeMetadata.


        :param title_name: The title_name of this ConfigTypeMetadata.  # noqa: E501
        :type title_name: str
        """
        if self.local_vars_configuration.client_side_validation and title_name is None:  # noqa: E501
            raise ValueError("Invalid value for `title_name`, must not be `None`")  # noqa: E501

        self._title_name = title_name

    @property
    def icon(self):
        """Gets the icon of this ConfigTypeMetadata.  # noqa: E501


        :return: The icon of this ConfigTypeMetadata.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this ConfigTypeMetadata.


        :param icon: The icon of this ConfigTypeMetadata.  # noqa: E501
        :type icon: str
        """

        self._icon = icon

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
        if not isinstance(other, ConfigTypeMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigTypeMetadata):
            return True

        return self.to_dict() != other.to_dict()
