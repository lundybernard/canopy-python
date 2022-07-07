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


class ConfigResolvedLabels(object):
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
        'reference': 'ConfigResolvedLabelsReference',
        'hashes': 'list[ConfigHash]',
        'resolved_labels': 'list[ResolvedLabel]'
    }

    attribute_map = {
        'reference': 'reference',
        'hashes': 'hashes',
        'resolved_labels': 'resolvedLabels'
    }

    def __init__(self, reference=None, hashes=None, resolved_labels=None, local_vars_configuration=None):  # noqa: E501
        """ConfigResolvedLabels - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._reference = None
        self._hashes = None
        self._resolved_labels = None
        self.discriminator = None

        self.reference = reference
        self.hashes = hashes
        self.resolved_labels = resolved_labels

    @property
    def reference(self):
        """Gets the reference of this ConfigResolvedLabels.  # noqa: E501


        :return: The reference of this ConfigResolvedLabels.  # noqa: E501
        :rtype: ConfigResolvedLabelsReference
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ConfigResolvedLabels.


        :param reference: The reference of this ConfigResolvedLabels.  # noqa: E501
        :type reference: ConfigResolvedLabelsReference
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def hashes(self):
        """Gets the hashes of this ConfigResolvedLabels.  # noqa: E501


        :return: The hashes of this ConfigResolvedLabels.  # noqa: E501
        :rtype: list[ConfigHash]
        """
        return self._hashes

    @hashes.setter
    def hashes(self, hashes):
        """Sets the hashes of this ConfigResolvedLabels.


        :param hashes: The hashes of this ConfigResolvedLabels.  # noqa: E501
        :type hashes: list[ConfigHash]
        """
        if self.local_vars_configuration.client_side_validation and hashes is None:  # noqa: E501
            raise ValueError("Invalid value for `hashes`, must not be `None`")  # noqa: E501

        self._hashes = hashes

    @property
    def resolved_labels(self):
        """Gets the resolved_labels of this ConfigResolvedLabels.  # noqa: E501


        :return: The resolved_labels of this ConfigResolvedLabels.  # noqa: E501
        :rtype: list[ResolvedLabel]
        """
        return self._resolved_labels

    @resolved_labels.setter
    def resolved_labels(self, resolved_labels):
        """Sets the resolved_labels of this ConfigResolvedLabels.


        :param resolved_labels: The resolved_labels of this ConfigResolvedLabels.  # noqa: E501
        :type resolved_labels: list[ResolvedLabel]
        """
        if self.local_vars_configuration.client_side_validation and resolved_labels is None:  # noqa: E501
            raise ValueError("Invalid value for `resolved_labels`, must not be `None`")  # noqa: E501

        self._resolved_labels = resolved_labels

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
        if not isinstance(other, ConfigResolvedLabels):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigResolvedLabels):
            return True

        return self.to_dict() != other.to_dict()
