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

class Snapshot(object):
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
        'created': 'int',
        'files': 'int',
        'name': 'str',
        'size': 'int',
        'state': 'str'
    }

    attribute_map = {
        'created': 'created',
        'files': 'files',
        'name': 'name',
        'size': 'size',
        'state': 'state'
    }

    def __init__(self, created=None, files=None, name=None, size=None, state=None):  # noqa: E501
        """Snapshot - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._files = None
        self._name = None
        self._size = None
        self._state = None
        self.discriminator = None
        self.created = created
        self.files = files
        self.name = name
        self.size = size
        self.state = state

    @property
    def created(self):
        """Gets the created of this Snapshot.  # noqa: E501


        :return: The created of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Snapshot.


        :param created: The created of this Snapshot.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def files(self):
        """Gets the files of this Snapshot.  # noqa: E501


        :return: The files of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Snapshot.


        :param files: The files of this Snapshot.  # noqa: E501
        :type: int
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files

    @property
    def name(self):
        """Gets the name of this Snapshot.  # noqa: E501


        :return: The name of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshot.


        :param name: The name of this Snapshot.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def size(self):
        """Gets the size of this Snapshot.  # noqa: E501


        :return: The size of this Snapshot.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Snapshot.


        :param size: The size of this Snapshot.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def state(self):
        """Gets the state of this Snapshot.  # noqa: E501


        :return: The state of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Snapshot.


        :param state: The state of this Snapshot.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if issubclass(Snapshot, dict):
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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
