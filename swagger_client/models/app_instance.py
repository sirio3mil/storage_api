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

class AppInstance(object):
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
        'client_id': 'str',
        'created_at': 'int',
        'id': 'str',
        'name': 'str',
        'redirect_uri': 'str',
        'scopes': 'list[str]',
        'user_agent': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'created_at': 'createdAt',
        'id': 'id',
        'name': 'name',
        'redirect_uri': 'redirectUri',
        'scopes': 'scopes',
        'user_agent': 'userAgent'
    }

    def __init__(self, client_id=None, created_at=None, id=None, name=None, redirect_uri=None, scopes=None, user_agent=None):  # noqa: E501
        """AppInstance - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._created_at = None
        self._id = None
        self._name = None
        self._redirect_uri = None
        self._scopes = None
        self._user_agent = None
        self.discriminator = None
        self.client_id = client_id
        self.created_at = created_at
        self.id = id
        self.name = name
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        self.scopes = scopes
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def client_id(self):
        """Gets the client_id of this AppInstance.  # noqa: E501


        :return: The client_id of this AppInstance.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AppInstance.


        :param client_id: The client_id of this AppInstance.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def created_at(self):
        """Gets the created_at of this AppInstance.  # noqa: E501


        :return: The created_at of this AppInstance.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AppInstance.


        :param created_at: The created_at of this AppInstance.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this AppInstance.  # noqa: E501


        :return: The id of this AppInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppInstance.


        :param id: The id of this AppInstance.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AppInstance.  # noqa: E501


        :return: The name of this AppInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppInstance.


        :param name: The name of this AppInstance.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this AppInstance.  # noqa: E501


        :return: The redirect_uri of this AppInstance.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this AppInstance.


        :param redirect_uri: The redirect_uri of this AppInstance.  # noqa: E501
        :type: str
        """

        self._redirect_uri = redirect_uri

    @property
    def scopes(self):
        """Gets the scopes of this AppInstance.  # noqa: E501


        :return: The scopes of this AppInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this AppInstance.


        :param scopes: The scopes of this AppInstance.  # noqa: E501
        :type: list[str]
        """
        if scopes is None:
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def user_agent(self):
        """Gets the user_agent of this AppInstance.  # noqa: E501


        :return: The user_agent of this AppInstance.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this AppInstance.


        :param user_agent: The user_agent of this AppInstance.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if issubclass(AppInstance, dict):
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
        if not isinstance(other, AppInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other