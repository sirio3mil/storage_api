# coding: utf-8

"""
    DIGI storage API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GroupCommon(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'space_total': 'int',
        'space_used': 'int'
    }

    attribute_map = {
        'space_total': 'spaceTotal',
        'space_used': 'spaceUsed'
    }

    def __init__(self, space_total=None, space_used=None):  # noqa: E501
        """GroupCommon - a model defined in Swagger"""  # noqa: E501
        self._space_total = None
        self._space_used = None
        self.discriminator = None
        self.space_total = space_total
        self.space_used = space_used

    @property
    def space_total(self):
        """Gets the space_total of this GroupCommon.  # noqa: E501


        :return: The space_total of this GroupCommon.  # noqa: E501
        :rtype: int
        """
        return self._space_total

    @space_total.setter
    def space_total(self, space_total):
        """Sets the space_total of this GroupCommon.


        :param space_total: The space_total of this GroupCommon.  # noqa: E501
        :type: int
        """
        if space_total is None:
            raise ValueError("Invalid value for `space_total`, must not be `None`")  # noqa: E501

        self._space_total = space_total

    @property
    def space_used(self):
        """Gets the space_used of this GroupCommon.  # noqa: E501


        :return: The space_used of this GroupCommon.  # noqa: E501
        :rtype: int
        """
        return self._space_used

    @space_used.setter
    def space_used(self, space_used):
        """Sets the space_used of this GroupCommon.


        :param space_used: The space_used of this GroupCommon.  # noqa: E501
        :type: int
        """
        if space_used is None:
            raise ValueError("Invalid value for `space_used`, must not be `None`")  # noqa: E501

        self._space_used = space_used

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GroupCommon, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
