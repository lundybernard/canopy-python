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


class ConfigReferenceTenant(object):
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
        'target_id': 'object',
        'job_index': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenantId',
        'target_id': 'targetId',
        'job_index': 'jobIndex'
    }

    def __init__(self, tenant_id=None, target_id=None, job_index=None, local_vars_configuration=None):  # noqa: E501
        """ConfigReferenceTenant - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tenant_id = None
        self._target_id = None
        self._job_index = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.target_id = target_id
        self.job_index = job_index

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ConfigReferenceTenant.  # noqa: E501


        :return: The tenant_id of this ConfigReferenceTenant.  # noqa: E501
        :rtype: object
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ConfigReferenceTenant.


        :param tenant_id: The tenant_id of this ConfigReferenceTenant.  # noqa: E501
        :type tenant_id: object
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def target_id(self):
        """Gets the target_id of this ConfigReferenceTenant.  # noqa: E501


        :return: The target_id of this ConfigReferenceTenant.  # noqa: E501
        :rtype: object
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ConfigReferenceTenant.


        :param target_id: The target_id of this ConfigReferenceTenant.  # noqa: E501
        :type target_id: object
        """
        if self.local_vars_configuration.client_side_validation and target_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_id`, must not be `None`")  # noqa: E501

        self._target_id = target_id

    @property
    def job_index(self):
        """Gets the job_index of this ConfigReferenceTenant.  # noqa: E501


        :return: The job_index of this ConfigReferenceTenant.  # noqa: E501
        :rtype: int
        """
        return self._job_index

    @job_index.setter
    def job_index(self, job_index):
        """Sets the job_index of this ConfigReferenceTenant.


        :param job_index: The job_index of this ConfigReferenceTenant.  # noqa: E501
        :type job_index: int
        """

        self._job_index = job_index

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
        if not isinstance(other, ConfigReferenceTenant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigReferenceTenant):
            return True

        return self.to_dict() != other.to_dict()
