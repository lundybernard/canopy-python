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


class Worksheet(object):
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
        'tenant_id': 'object',
        'user_id': 'object',
        'worksheet_id': 'object',
        'name': 'str',
        'outline': 'WorksheetOutline',
        'resolved_labels': 'WorksheetResolvedLabels',
        'resolved_references': 'WorksheetResolvedReferences',
        'support_session': 'CanopyDocumentSupportSession',
        'properties': 'object',
        'notes': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'user_id': 'userId',
        'worksheet_id': 'worksheetId',
        'name': 'name',
        'outline': 'outline',
        'resolved_labels': 'resolvedLabels',
        'resolved_references': 'resolvedReferences',
        'support_session': 'supportSession',
        'properties': 'properties',
        'notes': 'notes'
    }

    def __init__(self, tenant_id=None, user_id=None, worksheet_id=None, name=None, outline=None, resolved_labels=None, resolved_references=None, support_session=None, properties=None, notes=None, local_vars_configuration=None):  # noqa: E501
        """Worksheet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tenant_id = None
        self._user_id = None
        self._worksheet_id = None
        self._name = None
        self._outline = None
        self._resolved_labels = None
        self._resolved_references = None
        self._support_session = None
        self._properties = None
        self._notes = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.user_id = user_id
        self.worksheet_id = worksheet_id
        self.name = name
        self.outline = outline
        self.resolved_labels = resolved_labels
        self.resolved_references = resolved_references
        self.support_session = support_session
        self.properties = properties
        self.notes = notes

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Worksheet.  # noqa: E501


        :return: The tenant_id of this Worksheet.  # noqa: E501
        :rtype: object
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Worksheet.


        :param tenant_id: The tenant_id of this Worksheet.  # noqa: E501
        :type tenant_id: object
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """Gets the user_id of this Worksheet.  # noqa: E501


        :return: The user_id of this Worksheet.  # noqa: E501
        :rtype: object
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Worksheet.


        :param user_id: The user_id of this Worksheet.  # noqa: E501
        :type user_id: object
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def worksheet_id(self):
        """Gets the worksheet_id of this Worksheet.  # noqa: E501


        :return: The worksheet_id of this Worksheet.  # noqa: E501
        :rtype: object
        """
        return self._worksheet_id

    @worksheet_id.setter
    def worksheet_id(self, worksheet_id):
        """Sets the worksheet_id of this Worksheet.


        :param worksheet_id: The worksheet_id of this Worksheet.  # noqa: E501
        :type worksheet_id: object
        """
        if self.local_vars_configuration.client_side_validation and worksheet_id is None:  # noqa: E501
            raise ValueError("Invalid value for `worksheet_id`, must not be `None`")  # noqa: E501

        self._worksheet_id = worksheet_id

    @property
    def name(self):
        """Gets the name of this Worksheet.  # noqa: E501


        :return: The name of this Worksheet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Worksheet.


        :param name: The name of this Worksheet.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outline(self):
        """Gets the outline of this Worksheet.  # noqa: E501


        :return: The outline of this Worksheet.  # noqa: E501
        :rtype: WorksheetOutline
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        """Sets the outline of this Worksheet.


        :param outline: The outline of this Worksheet.  # noqa: E501
        :type outline: WorksheetOutline
        """
        if self.local_vars_configuration.client_side_validation and outline is None:  # noqa: E501
            raise ValueError("Invalid value for `outline`, must not be `None`")  # noqa: E501

        self._outline = outline

    @property
    def resolved_labels(self):
        """Gets the resolved_labels of this Worksheet.  # noqa: E501


        :return: The resolved_labels of this Worksheet.  # noqa: E501
        :rtype: WorksheetResolvedLabels
        """
        return self._resolved_labels

    @resolved_labels.setter
    def resolved_labels(self, resolved_labels):
        """Sets the resolved_labels of this Worksheet.


        :param resolved_labels: The resolved_labels of this Worksheet.  # noqa: E501
        :type resolved_labels: WorksheetResolvedLabels
        """

        self._resolved_labels = resolved_labels

    @property
    def resolved_references(self):
        """Gets the resolved_references of this Worksheet.  # noqa: E501


        :return: The resolved_references of this Worksheet.  # noqa: E501
        :rtype: WorksheetResolvedReferences
        """
        return self._resolved_references

    @resolved_references.setter
    def resolved_references(self, resolved_references):
        """Sets the resolved_references of this Worksheet.


        :param resolved_references: The resolved_references of this Worksheet.  # noqa: E501
        :type resolved_references: WorksheetResolvedReferences
        """

        self._resolved_references = resolved_references

    @property
    def support_session(self):
        """Gets the support_session of this Worksheet.  # noqa: E501


        :return: The support_session of this Worksheet.  # noqa: E501
        :rtype: CanopyDocumentSupportSession
        """
        return self._support_session

    @support_session.setter
    def support_session(self, support_session):
        """Sets the support_session of this Worksheet.


        :param support_session: The support_session of this Worksheet.  # noqa: E501
        :type support_session: CanopyDocumentSupportSession
        """

        self._support_session = support_session

    @property
    def properties(self):
        """Gets the properties of this Worksheet.  # noqa: E501


        :return: The properties of this Worksheet.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Worksheet.


        :param properties: The properties of this Worksheet.  # noqa: E501
        :type properties: object
        """

        self._properties = properties

    @property
    def notes(self):
        """Gets the notes of this Worksheet.  # noqa: E501


        :return: The notes of this Worksheet.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Worksheet.


        :param notes: The notes of this Worksheet.  # noqa: E501
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
        if not isinstance(other, Worksheet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Worksheet):
            return True

        return self.to_dict() != other.to_dict()
