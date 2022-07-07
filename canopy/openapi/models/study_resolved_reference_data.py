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


class StudyResolvedReferenceData(object):
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
        'creation_date': 'datetime',
        'modified_date': 'datetime',
        'user_id': 'object',
        'name': 'str',
        'study_document': 'StudyResolvedReferenceDataStudyDocument',
        'input_hashes': 'list[StudyInputHashes]',
        'sim_types': 'list[str]',
        'sim_version': 'object',
        'is_support_session_open': 'bool'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'modified_date': 'modifiedDate',
        'user_id': 'userId',
        'name': 'name',
        'study_document': 'studyDocument',
        'input_hashes': 'inputHashes',
        'sim_types': 'simTypes',
        'sim_version': 'simVersion',
        'is_support_session_open': 'isSupportSessionOpen'
    }

    def __init__(self, creation_date=None, modified_date=None, user_id=None, name=None, study_document=None, input_hashes=None, sim_types=None, sim_version=None, is_support_session_open=None, local_vars_configuration=None):  # noqa: E501
        """StudyResolvedReferenceData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._creation_date = None
        self._modified_date = None
        self._user_id = None
        self._name = None
        self._study_document = None
        self._input_hashes = None
        self._sim_types = None
        self._sim_version = None
        self._is_support_session_open = None
        self.discriminator = None

        self.creation_date = creation_date
        self.modified_date = modified_date
        self.user_id = user_id
        self.name = name
        self.study_document = study_document
        self.input_hashes = input_hashes
        self.sim_types = sim_types
        self.sim_version = sim_version
        self.is_support_session_open = is_support_session_open

    @property
    def creation_date(self):
        """Gets the creation_date of this StudyResolvedReferenceData.  # noqa: E501


        :return: The creation_date of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this StudyResolvedReferenceData.


        :param creation_date: The creation_date of this StudyResolvedReferenceData.  # noqa: E501
        :type creation_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def modified_date(self):
        """Gets the modified_date of this StudyResolvedReferenceData.  # noqa: E501


        :return: The modified_date of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this StudyResolvedReferenceData.


        :param modified_date: The modified_date of this StudyResolvedReferenceData.  # noqa: E501
        :type modified_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_date is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_date`, must not be `None`")  # noqa: E501

        self._modified_date = modified_date

    @property
    def user_id(self):
        """Gets the user_id of this StudyResolvedReferenceData.  # noqa: E501


        :return: The user_id of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: object
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this StudyResolvedReferenceData.


        :param user_id: The user_id of this StudyResolvedReferenceData.  # noqa: E501
        :type user_id: object
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this StudyResolvedReferenceData.  # noqa: E501


        :return: The name of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyResolvedReferenceData.


        :param name: The name of this StudyResolvedReferenceData.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def study_document(self):
        """Gets the study_document of this StudyResolvedReferenceData.  # noqa: E501


        :return: The study_document of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: StudyResolvedReferenceDataStudyDocument
        """
        return self._study_document

    @study_document.setter
    def study_document(self, study_document):
        """Sets the study_document of this StudyResolvedReferenceData.


        :param study_document: The study_document of this StudyResolvedReferenceData.  # noqa: E501
        :type study_document: StudyResolvedReferenceDataStudyDocument
        """
        if self.local_vars_configuration.client_side_validation and study_document is None:  # noqa: E501
            raise ValueError("Invalid value for `study_document`, must not be `None`")  # noqa: E501

        self._study_document = study_document

    @property
    def input_hashes(self):
        """Gets the input_hashes of this StudyResolvedReferenceData.  # noqa: E501


        :return: The input_hashes of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: list[StudyInputHashes]
        """
        return self._input_hashes

    @input_hashes.setter
    def input_hashes(self, input_hashes):
        """Sets the input_hashes of this StudyResolvedReferenceData.


        :param input_hashes: The input_hashes of this StudyResolvedReferenceData.  # noqa: E501
        :type input_hashes: list[StudyInputHashes]
        """
        if self.local_vars_configuration.client_side_validation and input_hashes is None:  # noqa: E501
            raise ValueError("Invalid value for `input_hashes`, must not be `None`")  # noqa: E501

        self._input_hashes = input_hashes

    @property
    def sim_types(self):
        """Gets the sim_types of this StudyResolvedReferenceData.  # noqa: E501


        :return: The sim_types of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: list[str]
        """
        return self._sim_types

    @sim_types.setter
    def sim_types(self, sim_types):
        """Sets the sim_types of this StudyResolvedReferenceData.


        :param sim_types: The sim_types of this StudyResolvedReferenceData.  # noqa: E501
        :type sim_types: list[str]
        """
        if self.local_vars_configuration.client_side_validation and sim_types is None:  # noqa: E501
            raise ValueError("Invalid value for `sim_types`, must not be `None`")  # noqa: E501

        self._sim_types = sim_types

    @property
    def sim_version(self):
        """Gets the sim_version of this StudyResolvedReferenceData.  # noqa: E501


        :return: The sim_version of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: object
        """
        return self._sim_version

    @sim_version.setter
    def sim_version(self, sim_version):
        """Sets the sim_version of this StudyResolvedReferenceData.


        :param sim_version: The sim_version of this StudyResolvedReferenceData.  # noqa: E501
        :type sim_version: object
        """
        if self.local_vars_configuration.client_side_validation and sim_version is None:  # noqa: E501
            raise ValueError("Invalid value for `sim_version`, must not be `None`")  # noqa: E501

        self._sim_version = sim_version

    @property
    def is_support_session_open(self):
        """Gets the is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501


        :return: The is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501
        :rtype: bool
        """
        return self._is_support_session_open

    @is_support_session_open.setter
    def is_support_session_open(self, is_support_session_open):
        """Sets the is_support_session_open of this StudyResolvedReferenceData.


        :param is_support_session_open: The is_support_session_open of this StudyResolvedReferenceData.  # noqa: E501
        :type is_support_session_open: bool
        """

        self._is_support_session_open = is_support_session_open

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
        if not isinstance(other, StudyResolvedReferenceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyResolvedReferenceData):
            return True

        return self.to_dict() != other.to_dict()
