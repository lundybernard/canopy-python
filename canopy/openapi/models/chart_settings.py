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


class ChartSettings(object):
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
        'chart_type': 'object',
        'chart_id': 'str',
        'preferred_chart_id': 'str',
        'preferred_chart_user_id': 'object'
    }

    attribute_map = {
        'chart_type': 'chartType',
        'chart_id': 'chartId',
        'preferred_chart_id': 'preferredChartId',
        'preferred_chart_user_id': 'preferredChartUserId'
    }

    def __init__(self, chart_type=None, chart_id=None, preferred_chart_id=None, preferred_chart_user_id=None, local_vars_configuration=None):  # noqa: E501
        """ChartSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._chart_type = None
        self._chart_id = None
        self._preferred_chart_id = None
        self._preferred_chart_user_id = None
        self.discriminator = None

        self.chart_type = chart_type
        self.chart_id = chart_id
        self.preferred_chart_id = preferred_chart_id
        self.preferred_chart_user_id = preferred_chart_user_id

    @property
    def chart_type(self):
        """Gets the chart_type of this ChartSettings.  # noqa: E501


        :return: The chart_type of this ChartSettings.  # noqa: E501
        :rtype: object
        """
        return self._chart_type

    @chart_type.setter
    def chart_type(self, chart_type):
        """Sets the chart_type of this ChartSettings.


        :param chart_type: The chart_type of this ChartSettings.  # noqa: E501
        :type chart_type: object
        """
        if self.local_vars_configuration.client_side_validation and chart_type is None:  # noqa: E501
            raise ValueError("Invalid value for `chart_type`, must not be `None`")  # noqa: E501

        self._chart_type = chart_type

    @property
    def chart_id(self):
        """Gets the chart_id of this ChartSettings.  # noqa: E501


        :return: The chart_id of this ChartSettings.  # noqa: E501
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        """Sets the chart_id of this ChartSettings.


        :param chart_id: The chart_id of this ChartSettings.  # noqa: E501
        :type chart_id: str
        """
        if self.local_vars_configuration.client_side_validation and chart_id is None:  # noqa: E501
            raise ValueError("Invalid value for `chart_id`, must not be `None`")  # noqa: E501

        self._chart_id = chart_id

    @property
    def preferred_chart_id(self):
        """Gets the preferred_chart_id of this ChartSettings.  # noqa: E501


        :return: The preferred_chart_id of this ChartSettings.  # noqa: E501
        :rtype: str
        """
        return self._preferred_chart_id

    @preferred_chart_id.setter
    def preferred_chart_id(self, preferred_chart_id):
        """Sets the preferred_chart_id of this ChartSettings.


        :param preferred_chart_id: The preferred_chart_id of this ChartSettings.  # noqa: E501
        :type preferred_chart_id: str
        """
        if self.local_vars_configuration.client_side_validation and preferred_chart_id is None:  # noqa: E501
            raise ValueError("Invalid value for `preferred_chart_id`, must not be `None`")  # noqa: E501

        self._preferred_chart_id = preferred_chart_id

    @property
    def preferred_chart_user_id(self):
        """Gets the preferred_chart_user_id of this ChartSettings.  # noqa: E501


        :return: The preferred_chart_user_id of this ChartSettings.  # noqa: E501
        :rtype: object
        """
        return self._preferred_chart_user_id

    @preferred_chart_user_id.setter
    def preferred_chart_user_id(self, preferred_chart_user_id):
        """Sets the preferred_chart_user_id of this ChartSettings.


        :param preferred_chart_user_id: The preferred_chart_user_id of this ChartSettings.  # noqa: E501
        :type preferred_chart_user_id: object
        """

        self._preferred_chart_user_id = preferred_chart_user_id

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
        if not isinstance(other, ChartSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChartSettings):
            return True

        return self.to_dict() != other.to_dict()
