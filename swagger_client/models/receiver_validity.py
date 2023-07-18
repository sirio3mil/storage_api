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

class ReceiverValidity(object):
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
        'valid_from': 'int',
        'valid_to': 'int'
    }

    attribute_map = {
        'valid_from': 'validFrom',
        'valid_to': 'validTo'
    }

    def __init__(self, valid_from=None, valid_to=None):  # noqa: E501
        """ReceiverValidity - a model defined in Swagger"""  # noqa: E501
        self._valid_from = None
        self._valid_to = None
        self.discriminator = None
        if valid_from is not None:
            self.valid_from = valid_from
        if valid_to is not None:
            self.valid_to = valid_to

    @property
    def valid_from(self):
        """Gets the valid_from of this ReceiverValidity.  # noqa: E501


        :return: The valid_from of this ReceiverValidity.  # noqa: E501
        :rtype: int
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this ReceiverValidity.


        :param valid_from: The valid_from of this ReceiverValidity.  # noqa: E501
        :type: int
        """

        self._valid_from = valid_from

    @property
    def valid_to(self):
        """Gets the valid_to of this ReceiverValidity.  # noqa: E501


        :return: The valid_to of this ReceiverValidity.  # noqa: E501
        :rtype: int
        """
        return self._valid_to

    @valid_to.setter
    def valid_to(self, valid_to):
        """Sets the valid_to of this ReceiverValidity.


        :param valid_to: The valid_to of this ReceiverValidity.  # noqa: E501
        :type: int
        """

        self._valid_to = valid_to

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
        if issubclass(ReceiverValidity, dict):
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
        if not isinstance(other, ReceiverValidity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
