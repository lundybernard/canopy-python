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


class GetStudyJobQueryResult(object):
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
        'study_job': 'GetConfigQueryResultConfig',
        'study_job_input': 'object',
        'converted_sim_version': 'object',
        'sim_types': 'list[str]',
        'access_information': 'GetStudyJobMetadataQueryResultAccessInformation'
    }

    attribute_map = {
        'study_job': 'studyJob',
        'study_job_input': 'studyJobInput',
        'converted_sim_version': 'convertedSimVersion',
        'sim_types': 'simTypes',
        'access_information': 'accessInformation'
    }

    def __init__(self, study_job=None, study_job_input=None, converted_sim_version=None, sim_types=None, access_information=None, local_vars_configuration=None):  # noqa: E501
        """GetStudyJobQueryResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._study_job = None
        self._study_job_input = None
        self._converted_sim_version = None
        self._sim_types = None
        self._access_information = None
        self.discriminator = None

        self.study_job = study_job
        self.study_job_input = study_job_input
        self.converted_sim_version = converted_sim_version
        self.sim_types = sim_types
        self.access_information = access_information

    @property
    def study_job(self):
        """Gets the study_job of this GetStudyJobQueryResult.  # noqa: E501


        :return: The study_job of this GetStudyJobQueryResult.  # noqa: E501
        :rtype: GetConfigQueryResultConfig
        """
        return self._study_job

    @study_job.setter
    def study_job(self, study_job):
        """Sets the study_job of this GetStudyJobQueryResult.


        :param study_job: The study_job of this GetStudyJobQueryResult.  # noqa: E501
        :type study_job: GetConfigQueryResultConfig
        """
        if self.local_vars_configuration.client_side_validation and study_job is None:  # noqa: E501
            raise ValueError("Invalid value for `study_job`, must not be `None`")  # noqa: E501

        self._study_job = study_job

    @property
    def study_job_input(self):
        """Gets the study_job_input of this GetStudyJobQueryResult.  # noqa: E501


        :return: The study_job_input of this GetStudyJobQueryResult.  # noqa: E501
        :rtype: object
        """
        return self._study_job_input

    @study_job_input.setter
    def study_job_input(self, study_job_input):
        """Sets the study_job_input of this GetStudyJobQueryResult.


        :param study_job_input: The study_job_input of this GetStudyJobQueryResult.  # noqa: E501
        :type study_job_input: object
        """

        self._study_job_input = study_job_input

    @property
    def converted_sim_version(self):
        """Gets the converted_sim_version of this GetStudyJobQueryResult.  # noqa: E501


        :return: The converted_sim_version of this GetStudyJobQueryResult.  # noqa: E501
        :rtype: object
        """
        return self._converted_sim_version

    @converted_sim_version.setter
    def converted_sim_version(self, converted_sim_version):
        """Sets the converted_sim_version of this GetStudyJobQueryResult.


        :param converted_sim_version: The converted_sim_version of this GetStudyJobQueryResult.  # noqa: E501
        :type converted_sim_version: object
        """

        self._converted_sim_version = converted_sim_version

    @property
    def sim_types(self):
        """Gets the sim_types of this GetStudyJobQueryResult.  # noqa: E501


        :return: The sim_types of this GetStudyJobQueryResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._sim_types

    @sim_types.setter
    def sim_types(self, sim_types):
        """Sets the sim_types of this GetStudyJobQueryResult.


        :param sim_types: The sim_types of this GetStudyJobQueryResult.  # noqa: E501
        :type sim_types: list[str]
        """

        self._sim_types = sim_types

    @property
    def access_information(self):
        """Gets the access_information of this GetStudyJobQueryResult.  # noqa: E501


        :return: The access_information of this GetStudyJobQueryResult.  # noqa: E501
        :rtype: GetStudyJobMetadataQueryResultAccessInformation
        """
        return self._access_information

    @access_information.setter
    def access_information(self, access_information):
        """Sets the access_information of this GetStudyJobQueryResult.


        :param access_information: The access_information of this GetStudyJobQueryResult.  # noqa: E501
        :type access_information: GetStudyJobMetadataQueryResultAccessInformation
        """
        if self.local_vars_configuration.client_side_validation and access_information is None:  # noqa: E501
            raise ValueError("Invalid value for `access_information`, must not be `None`")  # noqa: E501

        self._access_information = access_information

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
        if not isinstance(other, GetStudyJobQueryResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStudyJobQueryResult):
            return True

        return self.to_dict() != other.to_dict()
