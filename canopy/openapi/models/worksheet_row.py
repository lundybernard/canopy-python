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


class WorksheetRow(object):
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
        'name': 'object',
        'configs': 'list[WorksheetConfig]',
        'study': 'WorksheetRowStudy'
    }

    attribute_map = {
        'name': 'name',
        'configs': 'configs',
        'study': 'study'
    }

    def __init__(self, name=None, configs=None, study=None, local_vars_configuration=None):  # noqa: E501
        """WorksheetRow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._configs = None
        self._study = None
        self.discriminator = None

        self.name = name
        self.configs = configs
        self.study = study

    @property
    def name(self):
        """Gets the name of this WorksheetRow.  # noqa: E501


        :return: The name of this WorksheetRow.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorksheetRow.


        :param name: The name of this WorksheetRow.  # noqa: E501
        :type name: object
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def configs(self):
        """Gets the configs of this WorksheetRow.  # noqa: E501


        :return: The configs of this WorksheetRow.  # noqa: E501
        :rtype: list[WorksheetConfig]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this WorksheetRow.


        :param configs: The configs of this WorksheetRow.  # noqa: E501
        :type configs: list[WorksheetConfig]
        """
        if self.local_vars_configuration.client_side_validation and configs is None:  # noqa: E501
            raise ValueError("Invalid value for `configs`, must not be `None`")  # noqa: E501

        self._configs = configs

    @property
    def study(self):
        """Gets the study of this WorksheetRow.  # noqa: E501


        :return: The study of this WorksheetRow.  # noqa: E501
        :rtype: WorksheetRowStudy
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this WorksheetRow.


        :param study: The study of this WorksheetRow.  # noqa: E501
        :type study: WorksheetRowStudy
        """
        if self.local_vars_configuration.client_side_validation and study is None:  # noqa: E501
            raise ValueError("Invalid value for `study`, must not be `None`")  # noqa: E501

        self._study = study

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
        if not isinstance(other, WorksheetRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorksheetRow):
            return True

        return self.to_dict() != other.to_dict()
