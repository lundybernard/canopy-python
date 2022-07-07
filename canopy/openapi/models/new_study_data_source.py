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


class NewStudyDataSource(object):
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
        'config_type': 'object',
        'user_id': 'object',
        'config_id': 'str',
        'name': 'str',
        'is_edited': 'bool'
    }

    attribute_map = {
        'config_type': 'configType',
        'user_id': 'userId',
        'config_id': 'configId',
        'name': 'name',
        'is_edited': 'isEdited'
    }

    def __init__(self, config_type=None, user_id=None, config_id=None, name=None, is_edited=None, local_vars_configuration=None):  # noqa: E501
        """NewStudyDataSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._config_type = None
        self._user_id = None
        self._config_id = None
        self._name = None
        self._is_edited = None
        self.discriminator = None

        self.config_type = config_type
        self.user_id = user_id
        self.config_id = config_id
        self.name = name
        if is_edited is not None:
            self.is_edited = is_edited

    @property
    def config_type(self):
        """Gets the config_type of this NewStudyDataSource.  # noqa: E501


        :return: The config_type of this NewStudyDataSource.  # noqa: E501
        :rtype: object
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this NewStudyDataSource.


        :param config_type: The config_type of this NewStudyDataSource.  # noqa: E501
        :type config_type: object
        """

        self._config_type = config_type

    @property
    def user_id(self):
        """Gets the user_id of this NewStudyDataSource.  # noqa: E501


        :return: The user_id of this NewStudyDataSource.  # noqa: E501
        :rtype: object
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NewStudyDataSource.


        :param user_id: The user_id of this NewStudyDataSource.  # noqa: E501
        :type user_id: object
        """

        self._user_id = user_id

    @property
    def config_id(self):
        """Gets the config_id of this NewStudyDataSource.  # noqa: E501


        :return: The config_id of this NewStudyDataSource.  # noqa: E501
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        """Sets the config_id of this NewStudyDataSource.


        :param config_id: The config_id of this NewStudyDataSource.  # noqa: E501
        :type config_id: str
        """

        self._config_id = config_id

    @property
    def name(self):
        """Gets the name of this NewStudyDataSource.  # noqa: E501


        :return: The name of this NewStudyDataSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewStudyDataSource.


        :param name: The name of this NewStudyDataSource.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def is_edited(self):
        """Gets the is_edited of this NewStudyDataSource.  # noqa: E501


        :return: The is_edited of this NewStudyDataSource.  # noqa: E501
        :rtype: bool
        """
        return self._is_edited

    @is_edited.setter
    def is_edited(self, is_edited):
        """Sets the is_edited of this NewStudyDataSource.


        :param is_edited: The is_edited of this NewStudyDataSource.  # noqa: E501
        :type is_edited: bool
        """

        self._is_edited = is_edited

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
        if not isinstance(other, NewStudyDataSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewStudyDataSource):
            return True

        return self.to_dict() != other.to_dict()
