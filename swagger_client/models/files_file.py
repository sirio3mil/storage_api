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

class FilesFile(object):
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
        'content_type': 'str',
        'hash': 'str',
        'modified': 'int',
        'name': 'str',
        'size': 'int',
        'tags': 'dict(str, list[str])',
        'type': 'str'
    }

    attribute_map = {
        'content_type': 'contentType',
        'hash': 'hash',
        'modified': 'modified',
        'name': 'name',
        'size': 'size',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, content_type=None, hash=None, modified=None, name=None, size=None, tags=None, type=None):  # noqa: E501
        """FilesFile - a model defined in Swagger"""  # noqa: E501
        self._content_type = None
        self._hash = None
        self._modified = None
        self._name = None
        self._size = None
        self._tags = None
        self._type = None
        self.discriminator = None
        self.content_type = content_type
        if hash is not None:
            self.hash = hash
        self.modified = modified
        self.name = name
        self.size = size
        self.tags = tags
        self.type = type

    @property
    def content_type(self):
        """Gets the content_type of this FilesFile.  # noqa: E501


        :return: The content_type of this FilesFile.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FilesFile.


        :param content_type: The content_type of this FilesFile.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def hash(self):
        """Gets the hash of this FilesFile.  # noqa: E501


        :return: The hash of this FilesFile.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this FilesFile.


        :param hash: The hash of this FilesFile.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def modified(self):
        """Gets the modified of this FilesFile.  # noqa: E501


        :return: The modified of this FilesFile.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this FilesFile.


        :param modified: The modified of this FilesFile.  # noqa: E501
        :type: int
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this FilesFile.  # noqa: E501


        :return: The name of this FilesFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilesFile.


        :param name: The name of this FilesFile.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this FilesFile.  # noqa: E501


        :return: The size of this FilesFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FilesFile.


        :param size: The size of this FilesFile.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def tags(self):
        """Gets the tags of this FilesFile.  # noqa: E501


        :return: The tags of this FilesFile.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FilesFile.


        :param tags: The tags of this FilesFile.  # noqa: E501
        :type: dict(str, list[str])
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this FilesFile.  # noqa: E501


        :return: The type of this FilesFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FilesFile.


        :param type: The type of this FilesFile.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(FilesFile, dict):
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
        if not isinstance(other, FilesFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
