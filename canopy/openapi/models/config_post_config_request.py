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


class ConfigPostConfigRequest(object):
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
        'config_type': 'object',
        'properties': 'list[DocumentCustomPropertyData]',
        'config': 'object',
        'notes': 'str',
        'sim_version': 'str',
        'parent_worksheet_id': 'object'
    }

    attribute_map = {
        'name': 'name',
        'config_type': 'configType',
        'properties': 'properties',
        'config': 'config',
        'notes': 'notes',
        'sim_version': 'simVersion',
        'parent_worksheet_id': 'parentWorksheetId'
    }

    def __init__(self, name=None, config_type=None, properties=None, config=None, notes=None, sim_version=None, parent_worksheet_id=None, local_vars_configuration=None):  # noqa: E501
        """ConfigPostConfigRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._config_type = None
        self._properties = None
        self._config = None
        self._notes = None
        self._sim_version = None
        self._parent_worksheet_id = None
        self.discriminator = None

        self.name = name
        self.config_type = config_type
        self.properties = properties
        self.config = config
        self.notes = notes
        self.sim_version = sim_version
        self.parent_worksheet_id = parent_worksheet_id

    @property
    def name(self):
        """Gets the name of this ConfigPostConfigRequest.  # noqa: E501


        :return: The name of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigPostConfigRequest.


        :param name: The name of this ConfigPostConfigRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def config_type(self):
        """Gets the config_type of this ConfigPostConfigRequest.  # noqa: E501


        :return: The config_type of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: object
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this ConfigPostConfigRequest.


        :param config_type: The config_type of this ConfigPostConfigRequest.  # noqa: E501
        :type config_type: object
        """

        self._config_type = config_type

    @property
    def properties(self):
        """Gets the properties of this ConfigPostConfigRequest.  # noqa: E501


        :return: The properties of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: list[DocumentCustomPropertyData]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ConfigPostConfigRequest.


        :param properties: The properties of this ConfigPostConfigRequest.  # noqa: E501
        :type properties: list[DocumentCustomPropertyData]
        """

        self._properties = properties

    @property
    def config(self):
        """Gets the config of this ConfigPostConfigRequest.  # noqa: E501


        :return: The config of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ConfigPostConfigRequest.


        :param config: The config of this ConfigPostConfigRequest.  # noqa: E501
        :type config: object
        """

        self._config = config

    @property
    def notes(self):
        """Gets the notes of this ConfigPostConfigRequest.  # noqa: E501


        :return: The notes of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ConfigPostConfigRequest.


        :param notes: The notes of this ConfigPostConfigRequest.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def sim_version(self):
        """Gets the sim_version of this ConfigPostConfigRequest.  # noqa: E501


        :return: The sim_version of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: str
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this ConfigPostConfigRequest.


        :param sim_version: The sim_version of this ConfigPostConfigRequest.  # noqa: E501
        :type sim_version: str
        """

        self._sim_version = sim_version

    @property
    def parent_worksheet_id(self):
        """Gets the parent_worksheet_id of this ConfigPostConfigRequest.  # noqa: E501


        :return: The parent_worksheet_id of this ConfigPostConfigRequest.  # noqa: E501
        :rtype: object
        """
        return self._parent_worksheet_id

    @parent_worksheet_id.setter
    def parent_worksheet_id(self, parent_worksheet_id):
        """Sets the parent_worksheet_id of this ConfigPostConfigRequest.


        :param parent_worksheet_id: The parent_worksheet_id of this ConfigPostConfigRequest.  # noqa: E501
        :type parent_worksheet_id: object
        """

        self._parent_worksheet_id = parent_worksheet_id

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
        if not isinstance(other, ConfigPostConfigRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigPostConfigRequest):
            return True

        return self.to_dict() != other.to_dict()
