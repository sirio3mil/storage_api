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

class ApiError(object):
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
        'error': 'ApiErrorDetails',
        'request_id': 'str'
    }

    attribute_map = {
        'error': 'error',
        'request_id': 'requestId'
    }

    def __init__(self, error=None, request_id=None):  # noqa: E501
        """ApiError - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._request_id = None
        self.discriminator = None
        self.error = error
        self.request_id = request_id

    @property
    def error(self):
        """Gets the error of this ApiError.  # noqa: E501


        :return: The error of this ApiError.  # noqa: E501
        :rtype: ApiErrorDetails
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiError.


        :param error: The error of this ApiError.  # noqa: E501
        :type: ApiErrorDetails
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def request_id(self):
        """Gets the request_id of this ApiError.  # noqa: E501

        RequestID is the unique ID of the request  # noqa: E501

        :return: The request_id of this ApiError.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ApiError.

        RequestID is the unique ID of the request  # noqa: E501

        :param request_id: The request_id of this ApiError.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

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
        if issubclass(ApiError, dict):
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
        if not isinstance(other, ApiError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
