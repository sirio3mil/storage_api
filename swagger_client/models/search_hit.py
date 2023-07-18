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

class SearchHit(object):
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
        'link': 'Link',
        'modified': 'int',
        'mount': 'Mount',
        'mount_id': 'str',
        'name': 'str',
        'path': 'str',
        'receiver': 'Receiver',
        'score': 'float',
        'size': 'int',
        'tags': 'dict(str, list[str])',
        'type': 'str'
    }

    attribute_map = {
        'content_type': 'contentType',
        'link': 'link',
        'modified': 'modified',
        'mount': 'mount',
        'mount_id': 'mountId',
        'name': 'name',
        'path': 'path',
        'receiver': 'receiver',
        'score': 'score',
        'size': 'size',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, content_type=None, link=None, modified=None, mount=None, mount_id=None, name=None, path=None, receiver=None, score=None, size=None, tags=None, type=None):  # noqa: E501
        """SearchHit - a model defined in Swagger"""  # noqa: E501
        self._content_type = None
        self._link = None
        self._modified = None
        self._mount = None
        self._mount_id = None
        self._name = None
        self._path = None
        self._receiver = None
        self._score = None
        self._size = None
        self._tags = None
        self._type = None
        self.discriminator = None
        self.content_type = content_type
        if link is not None:
            self.link = link
        self.modified = modified
        if mount is not None:
            self.mount = mount
        self.mount_id = mount_id
        self.name = name
        self.path = path
        if receiver is not None:
            self.receiver = receiver
        self.score = score
        self.size = size
        self.tags = tags
        self.type = type

    @property
    def content_type(self):
        """Gets the content_type of this SearchHit.  # noqa: E501


        :return: The content_type of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this SearchHit.


        :param content_type: The content_type of this SearchHit.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def link(self):
        """Gets the link of this SearchHit.  # noqa: E501


        :return: The link of this SearchHit.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this SearchHit.


        :param link: The link of this SearchHit.  # noqa: E501
        :type: Link
        """

        self._link = link

    @property
    def modified(self):
        """Gets the modified of this SearchHit.  # noqa: E501


        :return: The modified of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SearchHit.


        :param modified: The modified of this SearchHit.  # noqa: E501
        :type: int
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def mount(self):
        """Gets the mount of this SearchHit.  # noqa: E501


        :return: The mount of this SearchHit.  # noqa: E501
        :rtype: Mount
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this SearchHit.


        :param mount: The mount of this SearchHit.  # noqa: E501
        :type: Mount
        """

        self._mount = mount

    @property
    def mount_id(self):
        """Gets the mount_id of this SearchHit.  # noqa: E501


        :return: The mount_id of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._mount_id

    @mount_id.setter
    def mount_id(self, mount_id):
        """Sets the mount_id of this SearchHit.


        :param mount_id: The mount_id of this SearchHit.  # noqa: E501
        :type: str
        """
        if mount_id is None:
            raise ValueError("Invalid value for `mount_id`, must not be `None`")  # noqa: E501

        self._mount_id = mount_id

    @property
    def name(self):
        """Gets the name of this SearchHit.  # noqa: E501


        :return: The name of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SearchHit.


        :param name: The name of this SearchHit.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this SearchHit.  # noqa: E501


        :return: The path of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SearchHit.


        :param path: The path of this SearchHit.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def receiver(self):
        """Gets the receiver of this SearchHit.  # noqa: E501


        :return: The receiver of this SearchHit.  # noqa: E501
        :rtype: Receiver
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this SearchHit.


        :param receiver: The receiver of this SearchHit.  # noqa: E501
        :type: Receiver
        """

        self._receiver = receiver

    @property
    def score(self):
        """Gets the score of this SearchHit.  # noqa: E501


        :return: The score of this SearchHit.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SearchHit.


        :param score: The score of this SearchHit.  # noqa: E501
        :type: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score

    @property
    def size(self):
        """Gets the size of this SearchHit.  # noqa: E501


        :return: The size of this SearchHit.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SearchHit.


        :param size: The size of this SearchHit.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def tags(self):
        """Gets the tags of this SearchHit.  # noqa: E501


        :return: The tags of this SearchHit.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SearchHit.


        :param tags: The tags of this SearchHit.  # noqa: E501
        :type: dict(str, list[str])
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this SearchHit.  # noqa: E501


        :return: The type of this SearchHit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SearchHit.


        :param type: The type of this SearchHit.  # noqa: E501
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
        if issubclass(SearchHit, dict):
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
        if not isinstance(other, SearchHit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
