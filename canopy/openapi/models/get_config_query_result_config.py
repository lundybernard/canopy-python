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


class GetConfigQueryResultConfig(object):
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
        'document_id': 'object',
        'tenant_id': 'object',
        'user_id': 'object',
        'name': 'str',
        'type': 'str',
        'sub_type': 'object',
        'sim_version': 'object',
        'creation_date': 'datetime',
        'modified_date': 'datetime',
        'properties': 'object',
        'data': 'object',
        'support_session': 'CanopyDocumentSupportSession',
        'notes': 'str',
        'delete_requested': 'bool',
        'parent_worksheet_id': 'object'
    }

    attribute_map = {
        'document_id': 'documentId',
        'tenant_id': 'tenantId',
        'user_id': 'userId',
        'name': 'name',
        'type': 'type',
        'sub_type': 'subType',
        'sim_version': 'simVersion',
        'creation_date': 'creationDate',
        'modified_date': 'modifiedDate',
        'properties': 'properties',
        'data': 'data',
        'support_session': 'supportSession',
        'notes': 'notes',
        'delete_requested': 'deleteRequested',
        'parent_worksheet_id': 'parentWorksheetId'
    }

    def __init__(self, document_id=None, tenant_id=None, user_id=None, name=None, type=None, sub_type=None, sim_version=None, creation_date=None, modified_date=None, properties=None, data=None, support_session=None, notes=None, delete_requested=None, parent_worksheet_id=None, local_vars_configuration=None):  # noqa: E501
        """GetConfigQueryResultConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._document_id = None
        self._tenant_id = None
        self._user_id = None
        self._name = None
        self._type = None
        self._sub_type = None
        self._sim_version = None
        self._creation_date = None
        self._modified_date = None
        self._properties = None
        self._data = None
        self._support_session = None
        self._notes = None
        self._delete_requested = None
        self._parent_worksheet_id = None
        self.discriminator = None

        self.document_id = document_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.name = name
        self.type = type
        self.sub_type = sub_type
        self.sim_version = sim_version
        self.creation_date = creation_date
        self.modified_date = modified_date
        self.properties = properties
        self.data = data
        self.support_session = support_session
        self.notes = notes
        if delete_requested is not None:
            self.delete_requested = delete_requested
        self.parent_worksheet_id = parent_worksheet_id

    @property
    def document_id(self):
        """Gets the document_id of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The document_id of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this GetConfigQueryResultConfig.


        :param document_id: The document_id of this GetConfigQueryResultConfig.  # noqa: E501
        :type document_id: object
        """
        if self.local_vars_configuration.client_side_validation and document_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The tenant_id of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this GetConfigQueryResultConfig.


        :param tenant_id: The tenant_id of this GetConfigQueryResultConfig.  # noqa: E501
        :type tenant_id: object
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def user_id(self):
        """Gets the user_id of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The user_id of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GetConfigQueryResultConfig.


        :param user_id: The user_id of this GetConfigQueryResultConfig.  # noqa: E501
        :type user_id: object
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The name of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetConfigQueryResultConfig.


        :param name: The name of this GetConfigQueryResultConfig.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The type of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetConfigQueryResultConfig.


        :param type: The type of this GetConfigQueryResultConfig.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The sub_type of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this GetConfigQueryResultConfig.


        :param sub_type: The sub_type of this GetConfigQueryResultConfig.  # noqa: E501
        :type sub_type: object
        """
        if self.local_vars_configuration.client_side_validation and sub_type is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_type`, must not be `None`")  # noqa: E501

        self._sub_type = sub_type

    @property
    def sim_version(self):
        """Gets the sim_version of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The sim_version of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this GetConfigQueryResultConfig.


        :param sim_version: The sim_version of this GetConfigQueryResultConfig.  # noqa: E501
        :type sim_version: object
        """
        if self.local_vars_configuration.client_side_validation and sim_version is None:  # noqa: E501
            raise ValueError("Invalid value for `sim_version`, must not be `None`")  # noqa: E501

        self._sim_version = sim_version

    @property
    def creation_date(self):
        """Gets the creation_date of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The creation_date of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this GetConfigQueryResultConfig.


        :param creation_date: The creation_date of this GetConfigQueryResultConfig.  # noqa: E501
        :type creation_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def modified_date(self):
        """Gets the modified_date of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The modified_date of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this GetConfigQueryResultConfig.


        :param modified_date: The modified_date of this GetConfigQueryResultConfig.  # noqa: E501
        :type modified_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_date is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_date`, must not be `None`")  # noqa: E501

        self._modified_date = modified_date

    @property
    def properties(self):
        """Gets the properties of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The properties of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GetConfigQueryResultConfig.


        :param properties: The properties of this GetConfigQueryResultConfig.  # noqa: E501
        :type properties: object
        """

        self._properties = properties

    @property
    def data(self):
        """Gets the data of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The data of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetConfigQueryResultConfig.


        :param data: The data of this GetConfigQueryResultConfig.  # noqa: E501
        :type data: object
        """

        self._data = data

    @property
    def support_session(self):
        """Gets the support_session of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The support_session of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: CanopyDocumentSupportSession
        """
        return self._support_session

    @support_session.setter
    def support_session(self, support_session):
        """Sets the support_session of this GetConfigQueryResultConfig.


        :param support_session: The support_session of this GetConfigQueryResultConfig.  # noqa: E501
        :type support_session: CanopyDocumentSupportSession
        """

        self._support_session = support_session

    @property
    def notes(self):
        """Gets the notes of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The notes of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this GetConfigQueryResultConfig.


        :param notes: The notes of this GetConfigQueryResultConfig.  # noqa: E501
        :type notes: str
        """

        self._notes = notes

    @property
    def delete_requested(self):
        """Gets the delete_requested of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The delete_requested of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: bool
        """
        return self._delete_requested

    @delete_requested.setter
    def delete_requested(self, delete_requested):
        """Sets the delete_requested of this GetConfigQueryResultConfig.


        :param delete_requested: The delete_requested of this GetConfigQueryResultConfig.  # noqa: E501
        :type delete_requested: bool
        """

        self._delete_requested = delete_requested

    @property
    def parent_worksheet_id(self):
        """Gets the parent_worksheet_id of this GetConfigQueryResultConfig.  # noqa: E501


        :return: The parent_worksheet_id of this GetConfigQueryResultConfig.  # noqa: E501
        :rtype: object
        """
        return self._parent_worksheet_id

    @parent_worksheet_id.setter
    def parent_worksheet_id(self, parent_worksheet_id):
        """Sets the parent_worksheet_id of this GetConfigQueryResultConfig.


        :param parent_worksheet_id: The parent_worksheet_id of this GetConfigQueryResultConfig.  # noqa: E501
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
        if not isinstance(other, GetConfigQueryResultConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetConfigQueryResultConfig):
            return True

        return self.to_dict() != other.to_dict()
