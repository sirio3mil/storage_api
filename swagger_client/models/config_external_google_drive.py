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

class ConfigExternalGoogleDrive(object):
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
        'connect_url': 'str',
        'enabled': 'bool',
        'logout_url': 'str'
    }

    attribute_map = {
        'connect_url': 'connectUrl',
        'enabled': 'enabled',
        'logout_url': 'logoutUrl'
    }

    def __init__(self, connect_url=None, enabled=None, logout_url=None):  # noqa: E501
        """ConfigExternalGoogleDrive - a model defined in Swagger"""  # noqa: E501
        self._connect_url = None
        self._enabled = None
        self._logout_url = None
        self.discriminator = None
        self.connect_url = connect_url
        self.enabled = enabled
        self.logout_url = logout_url

    @property
    def connect_url(self):
        """Gets the connect_url of this ConfigExternalGoogleDrive.  # noqa: E501

        ConnectUrl is the URL for connecting new Google Drive places.  # noqa: E501

        :return: The connect_url of this ConfigExternalGoogleDrive.  # noqa: E501
        :rtype: str
        """
        return self._connect_url

    @connect_url.setter
    def connect_url(self, connect_url):
        """Sets the connect_url of this ConfigExternalGoogleDrive.

        ConnectUrl is the URL for connecting new Google Drive places.  # noqa: E501

        :param connect_url: The connect_url of this ConfigExternalGoogleDrive.  # noqa: E501
        :type: str
        """
        if connect_url is None:
            raise ValueError("Invalid value for `connect_url`, must not be `None`")  # noqa: E501

        self._connect_url = connect_url

    @property
    def enabled(self):
        """Gets the enabled of this ConfigExternalGoogleDrive.  # noqa: E501

        Enabled defines whether Google Drive integration is enabled.  # noqa: E501

        :return: The enabled of this ConfigExternalGoogleDrive.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConfigExternalGoogleDrive.

        Enabled defines whether Google Drive integration is enabled.  # noqa: E501

        :param enabled: The enabled of this ConfigExternalGoogleDrive.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def logout_url(self):
        """Gets the logout_url of this ConfigExternalGoogleDrive.  # noqa: E501

        ConnectUrl is the URL for Google Drive user logout.  # noqa: E501

        :return: The logout_url of this ConfigExternalGoogleDrive.  # noqa: E501
        :rtype: str
        """
        return self._logout_url

    @logout_url.setter
    def logout_url(self, logout_url):
        """Sets the logout_url of this ConfigExternalGoogleDrive.

        ConnectUrl is the URL for Google Drive user logout.  # noqa: E501

        :param logout_url: The logout_url of this ConfigExternalGoogleDrive.  # noqa: E501
        :type: str
        """
        if logout_url is None:
            raise ValueError("Invalid value for `logout_url`, must not be `None`")  # noqa: E501

        self._logout_url = logout_url

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
        if issubclass(ConfigExternalGoogleDrive, dict):
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
        if not isinstance(other, ConfigExternalGoogleDrive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
