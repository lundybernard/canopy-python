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


class UpdatedStudyData(object):
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
        'name': 'str',
        'properties': 'list[DocumentCustomPropertyData]',
        'notes': 'str'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties',
        'notes': 'notes'
    }

    def __init__(self, name=None, properties=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """UpdatedStudyData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._properties = None
        self._notes = None
        self.discriminator = None

        self.name = name
        self.properties = properties
        self.notes = notes

    @property
    def name(self):
        """Gets the name of this UpdatedStudyData.  # noqa: E501


        :return: The name of this UpdatedStudyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatedStudyData.


        :param name: The name of this UpdatedStudyData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this UpdatedStudyData.  # noqa: E501


        :return: The properties of this UpdatedStudyData.  # noqa: E501
        :rtype: list[DocumentCustomPropertyData]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdatedStudyData.


        :param properties: The properties of this UpdatedStudyData.  # noqa: E501
        :type properties: list[DocumentCustomPropertyData]
        """

        self._properties = properties

    @property
    def notes(self):
        """Gets the notes of this UpdatedStudyData.  # noqa: E501


        :return: The notes of this UpdatedStudyData.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this UpdatedStudyData.


        :param notes: The notes of this UpdatedStudyData.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

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
        if not isinstance(other, UpdatedStudyData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatedStudyData):
            return True

        return self.to_dict() != other.to_dict()
