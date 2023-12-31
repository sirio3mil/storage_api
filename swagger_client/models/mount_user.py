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

class MountUser(object):
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
        'email': 'str',
        'id': 'str',
        'name': 'str',
        'permissions': 'dict(str, bool)'
    }

    attribute_map = {
        'added': 'added',
        'email': 'email',
        'id': 'id',
        'name': 'name',
        'permissions': 'permissions'
    }

    def __init__(self, added=None, email=None, id=None, name=None, permissions=None):  # noqa: E501
        """MountUser - a model defined in Swagger"""  # noqa: E501
        self._added = None
        self._email = None
        self._id = None
        self._name = None
        self._permissions = None
        self.discriminator = None
        self.added = added
        self.email = email
        self.id = id
        self.name = name
        self.permissions = permissions

    @property
    def added(self):
        """Gets the added of this MountUser.  # noqa: E501


        :return: The added of this MountUser.  # noqa: E501
        :rtype: int
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this MountUser.


        :param added: The added of this MountUser.  # noqa: E501
        :type: int
        """
        if added is None:
            raise ValueError("Invalid value for `added`, must not be `None`")  # noqa: E501

        self._added = added

    @property
    def email(self):
        """Gets the email of this MountUser.  # noqa: E501


        :return: The email of this MountUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MountUser.


        :param email: The email of this MountUser.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def id(self):
        """Gets the id of this MountUser.  # noqa: E501


        :return: The id of this MountUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MountUser.


        :param id: The id of this MountUser.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MountUser.  # noqa: E501


        :return: The name of this MountUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MountUser.


        :param name: The name of this MountUser.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def permissions(self):
        """Gets the permissions of this MountUser.  # noqa: E501


        :return: The permissions of this MountUser.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this MountUser.


        :param permissions: The permissions of this MountUser.  # noqa: E501
        :type: dict(str, bool)
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

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
        if issubclass(MountUser, dict):
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
        if not isinstance(other, MountUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
