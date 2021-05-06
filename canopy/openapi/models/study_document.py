# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from canopy.openapi.configuration import Configuration


class StudyDocument(object):
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
        'error_messages': 'list[str]',
        'job_count': 'int',
        'dispatched_job_count': 'int',
        'completed_job_count': 'int',
        'succeeded_job_count': 'int',
        'dispatched_compute_credits': 'float',
        'completed_compute_credits': 'float',
        'succeeded_compute_credits': 'float',
        'dispatched_storage_credits': 'float',
        'completed_storage_credits': 'float',
        'succeeded_storage_credits': 'float',
        'succeeded_simulation_count': 'int',
        'seed': 'int',
        'is_transient': 'bool',
        'execution_time_seconds': 'float',
        'study_type': 'str',
        'study_state': 'str',
        'sources': 'list[StudyDocumentStudyDocumentDataSource]',
        'definition': 'object',
        'shard_dispatched_job_counts': 'list[int]',
        'shard_dispatched_compute_credits': 'list[float]',
        'shard_dispatched_storage_credits': 'list[float]'
    }

    attribute_map = {
        'error_messages': 'errorMessages',
        'job_count': 'jobCount',
        'dispatched_job_count': 'dispatchedJobCount',
        'completed_job_count': 'completedJobCount',
        'succeeded_job_count': 'succeededJobCount',
        'dispatched_compute_credits': 'dispatchedComputeCredits',
        'completed_compute_credits': 'completedComputeCredits',
        'succeeded_compute_credits': 'succeededComputeCredits',
        'dispatched_storage_credits': 'dispatchedStorageCredits',
        'completed_storage_credits': 'completedStorageCredits',
        'succeeded_storage_credits': 'succeededStorageCredits',
        'succeeded_simulation_count': 'succeededSimulationCount',
        'seed': 'seed',
        'is_transient': 'isTransient',
        'execution_time_seconds': 'executionTimeSeconds',
        'study_type': 'studyType',
        'study_state': 'studyState',
        'sources': 'sources',
        'definition': 'definition',
        'shard_dispatched_job_counts': 'shardDispatchedJobCounts',
        'shard_dispatched_compute_credits': 'shardDispatchedComputeCredits',
        'shard_dispatched_storage_credits': 'shardDispatchedStorageCredits'
    }

    def __init__(self, error_messages=None, job_count=None, dispatched_job_count=None, completed_job_count=None, succeeded_job_count=None, dispatched_compute_credits=None, completed_compute_credits=None, succeeded_compute_credits=None, dispatched_storage_credits=None, completed_storage_credits=None, succeeded_storage_credits=None, succeeded_simulation_count=None, seed=None, is_transient=None, execution_time_seconds=None, study_type=None, study_state=None, sources=None, definition=None, shard_dispatched_job_counts=None, shard_dispatched_compute_credits=None, shard_dispatched_storage_credits=None, local_vars_configuration=None):  # noqa: E501
        """StudyDocument - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_messages = None
        self._job_count = None
        self._dispatched_job_count = None
        self._completed_job_count = None
        self._succeeded_job_count = None
        self._dispatched_compute_credits = None
        self._completed_compute_credits = None
        self._succeeded_compute_credits = None
        self._dispatched_storage_credits = None
        self._completed_storage_credits = None
        self._succeeded_storage_credits = None
        self._succeeded_simulation_count = None
        self._seed = None
        self._is_transient = None
        self._execution_time_seconds = None
        self._study_type = None
        self._study_state = None
        self._sources = None
        self._definition = None
        self._shard_dispatched_job_counts = None
        self._shard_dispatched_compute_credits = None
        self._shard_dispatched_storage_credits = None
        self.discriminator = None

        if error_messages is not None:
            self.error_messages = error_messages
        if job_count is not None:
            self.job_count = job_count
        if dispatched_job_count is not None:
            self.dispatched_job_count = dispatched_job_count
        if completed_job_count is not None:
            self.completed_job_count = completed_job_count
        if succeeded_job_count is not None:
            self.succeeded_job_count = succeeded_job_count
        if dispatched_compute_credits is not None:
            self.dispatched_compute_credits = dispatched_compute_credits
        if completed_compute_credits is not None:
            self.completed_compute_credits = completed_compute_credits
        if succeeded_compute_credits is not None:
            self.succeeded_compute_credits = succeeded_compute_credits
        if dispatched_storage_credits is not None:
            self.dispatched_storage_credits = dispatched_storage_credits
        if completed_storage_credits is not None:
            self.completed_storage_credits = completed_storage_credits
        if succeeded_storage_credits is not None:
            self.succeeded_storage_credits = succeeded_storage_credits
        if succeeded_simulation_count is not None:
            self.succeeded_simulation_count = succeeded_simulation_count
        if seed is not None:
            self.seed = seed
        if is_transient is not None:
            self.is_transient = is_transient
        if execution_time_seconds is not None:
            self.execution_time_seconds = execution_time_seconds
        if study_type is not None:
            self.study_type = study_type
        if study_state is not None:
            self.study_state = study_state
        if sources is not None:
            self.sources = sources
        if definition is not None:
            self.definition = definition
        if shard_dispatched_job_counts is not None:
            self.shard_dispatched_job_counts = shard_dispatched_job_counts
        if shard_dispatched_compute_credits is not None:
            self.shard_dispatched_compute_credits = shard_dispatched_compute_credits
        if shard_dispatched_storage_credits is not None:
            self.shard_dispatched_storage_credits = shard_dispatched_storage_credits

    @property
    def error_messages(self):
        """Gets the error_messages of this StudyDocument.  # noqa: E501


        :return: The error_messages of this StudyDocument.  # noqa: E501
        :rtype: list[str]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """Sets the error_messages of this StudyDocument.


        :param error_messages: The error_messages of this StudyDocument.  # noqa: E501
        :type: list[str]
        """

        self._error_messages = error_messages

    @property
    def job_count(self):
        """Gets the job_count of this StudyDocument.  # noqa: E501


        :return: The job_count of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._job_count

    @job_count.setter
    def job_count(self, job_count):
        """Sets the job_count of this StudyDocument.


        :param job_count: The job_count of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._job_count = job_count

    @property
    def dispatched_job_count(self):
        """Gets the dispatched_job_count of this StudyDocument.  # noqa: E501


        :return: The dispatched_job_count of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._dispatched_job_count

    @dispatched_job_count.setter
    def dispatched_job_count(self, dispatched_job_count):
        """Sets the dispatched_job_count of this StudyDocument.


        :param dispatched_job_count: The dispatched_job_count of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._dispatched_job_count = dispatched_job_count

    @property
    def completed_job_count(self):
        """Gets the completed_job_count of this StudyDocument.  # noqa: E501


        :return: The completed_job_count of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._completed_job_count

    @completed_job_count.setter
    def completed_job_count(self, completed_job_count):
        """Sets the completed_job_count of this StudyDocument.


        :param completed_job_count: The completed_job_count of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._completed_job_count = completed_job_count

    @property
    def succeeded_job_count(self):
        """Gets the succeeded_job_count of this StudyDocument.  # noqa: E501


        :return: The succeeded_job_count of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._succeeded_job_count

    @succeeded_job_count.setter
    def succeeded_job_count(self, succeeded_job_count):
        """Sets the succeeded_job_count of this StudyDocument.


        :param succeeded_job_count: The succeeded_job_count of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._succeeded_job_count = succeeded_job_count

    @property
    def dispatched_compute_credits(self):
        """Gets the dispatched_compute_credits of this StudyDocument.  # noqa: E501


        :return: The dispatched_compute_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._dispatched_compute_credits

    @dispatched_compute_credits.setter
    def dispatched_compute_credits(self, dispatched_compute_credits):
        """Sets the dispatched_compute_credits of this StudyDocument.


        :param dispatched_compute_credits: The dispatched_compute_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._dispatched_compute_credits = dispatched_compute_credits

    @property
    def completed_compute_credits(self):
        """Gets the completed_compute_credits of this StudyDocument.  # noqa: E501


        :return: The completed_compute_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._completed_compute_credits

    @completed_compute_credits.setter
    def completed_compute_credits(self, completed_compute_credits):
        """Sets the completed_compute_credits of this StudyDocument.


        :param completed_compute_credits: The completed_compute_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._completed_compute_credits = completed_compute_credits

    @property
    def succeeded_compute_credits(self):
        """Gets the succeeded_compute_credits of this StudyDocument.  # noqa: E501


        :return: The succeeded_compute_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._succeeded_compute_credits

    @succeeded_compute_credits.setter
    def succeeded_compute_credits(self, succeeded_compute_credits):
        """Sets the succeeded_compute_credits of this StudyDocument.


        :param succeeded_compute_credits: The succeeded_compute_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._succeeded_compute_credits = succeeded_compute_credits

    @property
    def dispatched_storage_credits(self):
        """Gets the dispatched_storage_credits of this StudyDocument.  # noqa: E501


        :return: The dispatched_storage_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._dispatched_storage_credits

    @dispatched_storage_credits.setter
    def dispatched_storage_credits(self, dispatched_storage_credits):
        """Sets the dispatched_storage_credits of this StudyDocument.


        :param dispatched_storage_credits: The dispatched_storage_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._dispatched_storage_credits = dispatched_storage_credits

    @property
    def completed_storage_credits(self):
        """Gets the completed_storage_credits of this StudyDocument.  # noqa: E501


        :return: The completed_storage_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._completed_storage_credits

    @completed_storage_credits.setter
    def completed_storage_credits(self, completed_storage_credits):
        """Sets the completed_storage_credits of this StudyDocument.


        :param completed_storage_credits: The completed_storage_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._completed_storage_credits = completed_storage_credits

    @property
    def succeeded_storage_credits(self):
        """Gets the succeeded_storage_credits of this StudyDocument.  # noqa: E501


        :return: The succeeded_storage_credits of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._succeeded_storage_credits

    @succeeded_storage_credits.setter
    def succeeded_storage_credits(self, succeeded_storage_credits):
        """Sets the succeeded_storage_credits of this StudyDocument.


        :param succeeded_storage_credits: The succeeded_storage_credits of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._succeeded_storage_credits = succeeded_storage_credits

    @property
    def succeeded_simulation_count(self):
        """Gets the succeeded_simulation_count of this StudyDocument.  # noqa: E501


        :return: The succeeded_simulation_count of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._succeeded_simulation_count

    @succeeded_simulation_count.setter
    def succeeded_simulation_count(self, succeeded_simulation_count):
        """Sets the succeeded_simulation_count of this StudyDocument.


        :param succeeded_simulation_count: The succeeded_simulation_count of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._succeeded_simulation_count = succeeded_simulation_count

    @property
    def seed(self):
        """Gets the seed of this StudyDocument.  # noqa: E501


        :return: The seed of this StudyDocument.  # noqa: E501
        :rtype: int
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """Sets the seed of this StudyDocument.


        :param seed: The seed of this StudyDocument.  # noqa: E501
        :type: int
        """

        self._seed = seed

    @property
    def is_transient(self):
        """Gets the is_transient of this StudyDocument.  # noqa: E501


        :return: The is_transient of this StudyDocument.  # noqa: E501
        :rtype: bool
        """
        return self._is_transient

    @is_transient.setter
    def is_transient(self, is_transient):
        """Sets the is_transient of this StudyDocument.


        :param is_transient: The is_transient of this StudyDocument.  # noqa: E501
        :type: bool
        """

        self._is_transient = is_transient

    @property
    def execution_time_seconds(self):
        """Gets the execution_time_seconds of this StudyDocument.  # noqa: E501


        :return: The execution_time_seconds of this StudyDocument.  # noqa: E501
        :rtype: float
        """
        return self._execution_time_seconds

    @execution_time_seconds.setter
    def execution_time_seconds(self, execution_time_seconds):
        """Sets the execution_time_seconds of this StudyDocument.


        :param execution_time_seconds: The execution_time_seconds of this StudyDocument.  # noqa: E501
        :type: float
        """

        self._execution_time_seconds = execution_time_seconds

    @property
    def study_type(self):
        """Gets the study_type of this StudyDocument.  # noqa: E501


        :return: The study_type of this StudyDocument.  # noqa: E501
        :rtype: str
        """
        return self._study_type

    @study_type.setter
    def study_type(self, study_type):
        """Sets the study_type of this StudyDocument.


        :param study_type: The study_type of this StudyDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["straightSim", "apexSim", "quasiStaticLap", "generateRacingLine", "quasiStaticLapWithGenerateRacingLine", "deploymentLap", "failureSim", "successSim", "virtual4Post", "limitSim", "driveCycleSim", "dynamicLap", "dynamicLapWithSLS", "dynamicLapHD", "dynamicMultiLap", "tyreThermalDynamicLap", "tyreThermalDynamicMultiLap", "overtakingLap", "allLapSims", "dragSim", "thermalReplay", "tyreReplay", "pacejkaCanopyConverter", "aircraftSim", "channelInference", "telemetry", "iliadCollocation", "subLimitSim", "bankedLimitSim", "postProcessUserMaths", "trackConverter", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and study_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `study_type` ({0}), must be one of {1}"  # noqa: E501
                .format(study_type, allowed_values)
            )

        self._study_type = study_type

    @property
    def study_state(self):
        """Gets the study_state of this StudyDocument.  # noqa: E501


        :return: The study_state of this StudyDocument.  # noqa: E501
        :rtype: str
        """
        return self._study_state

    @study_state.setter
    def study_state(self, study_state):
        """Sets the study_state of this StudyDocument.


        :param study_state: The study_state of this StudyDocument.  # noqa: E501
        :type: str
        """
        allowed_values = ["completed", "failed", "running", "buildingAndRunning", "posponed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and study_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `study_state` ({0}), must be one of {1}"  # noqa: E501
                .format(study_state, allowed_values)
            )

        self._study_state = study_state

    @property
    def sources(self):
        """Gets the sources of this StudyDocument.  # noqa: E501


        :return: The sources of this StudyDocument.  # noqa: E501
        :rtype: list[StudyDocumentStudyDocumentDataSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this StudyDocument.


        :param sources: The sources of this StudyDocument.  # noqa: E501
        :type: list[StudyDocumentStudyDocumentDataSource]
        """

        self._sources = sources

    @property
    def definition(self):
        """Gets the definition of this StudyDocument.  # noqa: E501


        :return: The definition of this StudyDocument.  # noqa: E501
        :rtype: object
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this StudyDocument.


        :param definition: The definition of this StudyDocument.  # noqa: E501
        :type: object
        """

        self._definition = definition

    @property
    def shard_dispatched_job_counts(self):
        """Gets the shard_dispatched_job_counts of this StudyDocument.  # noqa: E501


        :return: The shard_dispatched_job_counts of this StudyDocument.  # noqa: E501
        :rtype: list[int]
        """
        return self._shard_dispatched_job_counts

    @shard_dispatched_job_counts.setter
    def shard_dispatched_job_counts(self, shard_dispatched_job_counts):
        """Sets the shard_dispatched_job_counts of this StudyDocument.


        :param shard_dispatched_job_counts: The shard_dispatched_job_counts of this StudyDocument.  # noqa: E501
        :type: list[int]
        """

        self._shard_dispatched_job_counts = shard_dispatched_job_counts

    @property
    def shard_dispatched_compute_credits(self):
        """Gets the shard_dispatched_compute_credits of this StudyDocument.  # noqa: E501


        :return: The shard_dispatched_compute_credits of this StudyDocument.  # noqa: E501
        :rtype: list[float]
        """
        return self._shard_dispatched_compute_credits

    @shard_dispatched_compute_credits.setter
    def shard_dispatched_compute_credits(self, shard_dispatched_compute_credits):
        """Sets the shard_dispatched_compute_credits of this StudyDocument.


        :param shard_dispatched_compute_credits: The shard_dispatched_compute_credits of this StudyDocument.  # noqa: E501
        :type: list[float]
        """

        self._shard_dispatched_compute_credits = shard_dispatched_compute_credits

    @property
    def shard_dispatched_storage_credits(self):
        """Gets the shard_dispatched_storage_credits of this StudyDocument.  # noqa: E501


        :return: The shard_dispatched_storage_credits of this StudyDocument.  # noqa: E501
        :rtype: list[float]
        """
        return self._shard_dispatched_storage_credits

    @shard_dispatched_storage_credits.setter
    def shard_dispatched_storage_credits(self, shard_dispatched_storage_credits):
        """Sets the shard_dispatched_storage_credits of this StudyDocument.


        :param shard_dispatched_storage_credits: The shard_dispatched_storage_credits of this StudyDocument.  # noqa: E501
        :type: list[float]
        """

        self._shard_dispatched_storage_credits = shard_dispatched_storage_credits

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StudyDocument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StudyDocument):
            return True

        return self.to_dict() != other.to_dict()
