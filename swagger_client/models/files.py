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

class Files(object):
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
        'files': 'list[FilesFile]'
    }

    attribute_map = {
        'files': 'files'
    }

    def __init__(self, files=None):  # noqa: E501
        """Files - a model defined in Swagger"""  # noqa: E501
        self._files = None
        self.discriminator = None
        self.files = files

    @property
    def files(self):
        """Gets the files of this Files.  # noqa: E501


        :return: The files of this Files.  # noqa: E501
        :rtype: list[FilesFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Files.


        :param files: The files of this Files.  # noqa: E501
        :type: list[FilesFile]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

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
        if issubclass(Files, dict):
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
        if not isinstance(other, Files):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
