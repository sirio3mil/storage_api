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

class SettingsSecurity(object):
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
        'download_link_auto_password': 'bool',
        'download_link_require_password': 'bool',
        'upload_link_auto_password': 'bool',
        'upload_link_require_password': 'bool'
    }

    attribute_map = {
        'download_link_auto_password': 'downloadLinkAutoPassword',
        'download_link_require_password': 'downloadLinkRequirePassword',
        'upload_link_auto_password': 'uploadLinkAutoPassword',
        'upload_link_require_password': 'uploadLinkRequirePassword'
    }

    def __init__(self, download_link_auto_password=None, download_link_require_password=None, upload_link_auto_password=None, upload_link_require_password=None):  # noqa: E501
        """SettingsSecurity - a model defined in Swagger"""  # noqa: E501
        self._download_link_auto_password = None
        self._download_link_require_password = None
        self._upload_link_auto_password = None
        self._upload_link_require_password = None
        self.discriminator = None
        self.download_link_auto_password = download_link_auto_password
        self.download_link_require_password = download_link_require_password
        self.upload_link_auto_password = upload_link_auto_password
        self.upload_link_require_password = upload_link_require_password

    @property
    def download_link_auto_password(self):
        """Gets the download_link_auto_password of this SettingsSecurity.  # noqa: E501


        :return: The download_link_auto_password of this SettingsSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._download_link_auto_password

    @download_link_auto_password.setter
    def download_link_auto_password(self, download_link_auto_password):
        """Sets the download_link_auto_password of this SettingsSecurity.


        :param download_link_auto_password: The download_link_auto_password of this SettingsSecurity.  # noqa: E501
        :type: bool
        """
        if download_link_auto_password is None:
            raise ValueError("Invalid value for `download_link_auto_password`, must not be `None`")  # noqa: E501

        self._download_link_auto_password = download_link_auto_password

    @property
    def download_link_require_password(self):
        """Gets the download_link_require_password of this SettingsSecurity.  # noqa: E501


        :return: The download_link_require_password of this SettingsSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._download_link_require_password

    @download_link_require_password.setter
    def download_link_require_password(self, download_link_require_password):
        """Sets the download_link_require_password of this SettingsSecurity.


        :param download_link_require_password: The download_link_require_password of this SettingsSecurity.  # noqa: E501
        :type: bool
        """
        if download_link_require_password is None:
            raise ValueError("Invalid value for `download_link_require_password`, must not be `None`")  # noqa: E501

        self._download_link_require_password = download_link_require_password

    @property
    def upload_link_auto_password(self):
        """Gets the upload_link_auto_password of this SettingsSecurity.  # noqa: E501


        :return: The upload_link_auto_password of this SettingsSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._upload_link_auto_password

    @upload_link_auto_password.setter
    def upload_link_auto_password(self, upload_link_auto_password):
        """Sets the upload_link_auto_password of this SettingsSecurity.


        :param upload_link_auto_password: The upload_link_auto_password of this SettingsSecurity.  # noqa: E501
        :type: bool
        """
        if upload_link_auto_password is None:
            raise ValueError("Invalid value for `upload_link_auto_password`, must not be `None`")  # noqa: E501

        self._upload_link_auto_password = upload_link_auto_password

    @property
    def upload_link_require_password(self):
        """Gets the upload_link_require_password of this SettingsSecurity.  # noqa: E501


        :return: The upload_link_require_password of this SettingsSecurity.  # noqa: E501
        :rtype: bool
        """
        return self._upload_link_require_password

    @upload_link_require_password.setter
    def upload_link_require_password(self, upload_link_require_password):
        """Sets the upload_link_require_password of this SettingsSecurity.


        :param upload_link_require_password: The upload_link_require_password of this SettingsSecurity.  # noqa: E501
        :type: bool
        """
        if upload_link_require_password is None:
            raise ValueError("Invalid value for `upload_link_require_password`, must not be `None`")  # noqa: E501

        self._upload_link_require_password = upload_link_require_password

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
        if issubclass(SettingsSecurity, dict):
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
        if not isinstance(other, SettingsSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other