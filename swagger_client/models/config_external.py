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

class ConfigExternal(object):
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
        'cloud_drive': 'ConfigExternalCloudDrive',
        'dropbox': 'ConfigExternalDropbox',
        'google_drive': 'ConfigExternalGoogleDrive',
        'one_drive': 'ConfigExternalOneDrive'
    }

    attribute_map = {
        'cloud_drive': 'cloudDrive',
        'dropbox': 'dropbox',
        'google_drive': 'googleDrive',
        'one_drive': 'oneDrive'
    }

    def __init__(self, cloud_drive=None, dropbox=None, google_drive=None, one_drive=None):  # noqa: E501
        """ConfigExternal - a model defined in Swagger"""  # noqa: E501
        self._cloud_drive = None
        self._dropbox = None
        self._google_drive = None
        self._one_drive = None
        self.discriminator = None
        self.cloud_drive = cloud_drive
        self.dropbox = dropbox
        self.google_drive = google_drive
        self.one_drive = one_drive

    @property
    def cloud_drive(self):
        """Gets the cloud_drive of this ConfigExternal.  # noqa: E501


        :return: The cloud_drive of this ConfigExternal.  # noqa: E501
        :rtype: ConfigExternalCloudDrive
        """
        return self._cloud_drive

    @cloud_drive.setter
    def cloud_drive(self, cloud_drive):
        """Sets the cloud_drive of this ConfigExternal.


        :param cloud_drive: The cloud_drive of this ConfigExternal.  # noqa: E501
        :type: ConfigExternalCloudDrive
        """
        if cloud_drive is None:
            raise ValueError("Invalid value for `cloud_drive`, must not be `None`")  # noqa: E501

        self._cloud_drive = cloud_drive

    @property
    def dropbox(self):
        """Gets the dropbox of this ConfigExternal.  # noqa: E501


        :return: The dropbox of this ConfigExternal.  # noqa: E501
        :rtype: ConfigExternalDropbox
        """
        return self._dropbox

    @dropbox.setter
    def dropbox(self, dropbox):
        """Sets the dropbox of this ConfigExternal.


        :param dropbox: The dropbox of this ConfigExternal.  # noqa: E501
        :type: ConfigExternalDropbox
        """
        if dropbox is None:
            raise ValueError("Invalid value for `dropbox`, must not be `None`")  # noqa: E501

        self._dropbox = dropbox

    @property
    def google_drive(self):
        """Gets the google_drive of this ConfigExternal.  # noqa: E501


        :return: The google_drive of this ConfigExternal.  # noqa: E501
        :rtype: ConfigExternalGoogleDrive
        """
        return self._google_drive

    @google_drive.setter
    def google_drive(self, google_drive):
        """Sets the google_drive of this ConfigExternal.


        :param google_drive: The google_drive of this ConfigExternal.  # noqa: E501
        :type: ConfigExternalGoogleDrive
        """
        if google_drive is None:
            raise ValueError("Invalid value for `google_drive`, must not be `None`")  # noqa: E501

        self._google_drive = google_drive

    @property
    def one_drive(self):
        """Gets the one_drive of this ConfigExternal.  # noqa: E501


        :return: The one_drive of this ConfigExternal.  # noqa: E501
        :rtype: ConfigExternalOneDrive
        """
        return self._one_drive

    @one_drive.setter
    def one_drive(self, one_drive):
        """Sets the one_drive of this ConfigExternal.


        :param one_drive: The one_drive of this ConfigExternal.  # noqa: E501
        :type: ConfigExternalOneDrive
        """
        if one_drive is None:
            raise ValueError("Invalid value for `one_drive`, must not be `None`")  # noqa: E501

        self._one_drive = one_drive

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
        if issubclass(ConfigExternal, dict):
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
        if not isinstance(other, ConfigExternal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
