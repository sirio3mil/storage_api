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

class Comment(object):
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
        'added': 'int',
        'content': 'str',
        'id': 'str',
        'user': 'UserInfo'
    }

    attribute_map = {
        'added': 'added',
        'content': 'content',
        'id': 'id',
        'user': 'user'
    }

    def __init__(self, added=None, content=None, id=None, user=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        self._added = None
        self._content = None
        self._id = None
        self._user = None
        self.discriminator = None
        self.added = added
        self.content = content
        self.id = id
        if user is not None:
            self.user = user

    @property
    def added(self):
        """Gets the added of this Comment.  # noqa: E501


        :return: The added of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this Comment.


        :param added: The added of this Comment.  # noqa: E501
        :type: int
        """
        if added is None:
            raise ValueError("Invalid value for `added`, must not be `None`")  # noqa: E501

        self._added = added

    @property
    def content(self):
        """Gets the content of this Comment.  # noqa: E501


        :return: The content of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Comment.


        :param content: The content of this Comment.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501


        :return: The id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.


        :param id: The id of this Comment.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user(self):
        """Gets the user of this Comment.  # noqa: E501


        :return: The user of this Comment.  # noqa: E501
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Comment.


        :param user: The user of this Comment.  # noqa: E501
        :type: UserInfo
        """

        self._user = user

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
        if issubclass(Comment, dict):
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
        if not isinstance(other, Comment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other