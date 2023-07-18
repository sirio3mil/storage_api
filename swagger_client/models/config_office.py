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

class ConfigOffice(object):
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
        'enabled': 'bool',
        'extensions': 'list[str]',
        'office_online_allowed': 'bool',
        'office_online_data_locale': 'str',
        'office_online_enabled': 'bool',
        'office_online_locale': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'extensions': 'extensions',
        'office_online_allowed': 'officeOnlineAllowed',
        'office_online_data_locale': 'officeOnlineDataLocale',
        'office_online_enabled': 'officeOnlineEnabled',
        'office_online_locale': 'officeOnlineLocale'
    }

    def __init__(self, enabled=None, extensions=None, office_online_allowed=None, office_online_data_locale=None, office_online_enabled=None, office_online_locale=None):  # noqa: E501
        """ConfigOffice - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._extensions = None
        self._office_online_allowed = None
        self._office_online_data_locale = None
        self._office_online_enabled = None
        self._office_online_locale = None
        self.discriminator = None
        self.enabled = enabled
        self.extensions = extensions
        self.office_online_allowed = office_online_allowed
        if office_online_data_locale is not None:
            self.office_online_data_locale = office_online_data_locale
        self.office_online_enabled = office_online_enabled
        if office_online_locale is not None:
            self.office_online_locale = office_online_locale

    @property
    def enabled(self):
        """Gets the enabled of this ConfigOffice.  # noqa: E501

        Enabled defines whether Office Web Apps integration is enabled.  # noqa: E501

        :return: The enabled of this ConfigOffice.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConfigOffice.

        Enabled defines whether Office Web Apps integration is enabled.  # noqa: E501

        :param enabled: The enabled of this ConfigOffice.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def extensions(self):
        """Gets the extensions of this ConfigOffice.  # noqa: E501

        Extensions is a list of file extensions for which Office integration is supported.  # noqa: E501

        :return: The extensions of this ConfigOffice.  # noqa: E501
        :rtype: list[str]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this ConfigOffice.

        Extensions is a list of file extensions for which Office integration is supported.  # noqa: E501

        :param extensions: The extensions of this ConfigOffice.  # noqa: E501
        :type: list[str]
        """
        if extensions is None:
            raise ValueError("Invalid value for `extensions`, must not be `None`")  # noqa: E501

        self._extensions = extensions

    @property
    def office_online_allowed(self):
        """Gets the office_online_allowed of this ConfigOffice.  # noqa: E501

        OfficeOnlineEnabled defines whether Office Online integration is allowed for the current user.  # noqa: E501

        :return: The office_online_allowed of this ConfigOffice.  # noqa: E501
        :rtype: bool
        """
        return self._office_online_allowed

    @office_online_allowed.setter
    def office_online_allowed(self, office_online_allowed):
        """Sets the office_online_allowed of this ConfigOffice.

        OfficeOnlineEnabled defines whether Office Online integration is allowed for the current user.  # noqa: E501

        :param office_online_allowed: The office_online_allowed of this ConfigOffice.  # noqa: E501
        :type: bool
        """
        if office_online_allowed is None:
            raise ValueError("Invalid value for `office_online_allowed`, must not be `None`")  # noqa: E501

        self._office_online_allowed = office_online_allowed

    @property
    def office_online_data_locale(self):
        """Gets the office_online_data_locale of this ConfigOffice.  # noqa: E501

        OfficeOnlineLocale is the default locale of the Office Online data (e.g. Excel numbers and dates locale).  # noqa: E501

        :return: The office_online_data_locale of this ConfigOffice.  # noqa: E501
        :rtype: str
        """
        return self._office_online_data_locale

    @office_online_data_locale.setter
    def office_online_data_locale(self, office_online_data_locale):
        """Sets the office_online_data_locale of this ConfigOffice.

        OfficeOnlineLocale is the default locale of the Office Online data (e.g. Excel numbers and dates locale).  # noqa: E501

        :param office_online_data_locale: The office_online_data_locale of this ConfigOffice.  # noqa: E501
        :type: str
        """

        self._office_online_data_locale = office_online_data_locale

    @property
    def office_online_enabled(self):
        """Gets the office_online_enabled of this ConfigOffice.  # noqa: E501

        OfficeOnlineEnabled defines whether Office Online integration is enabled.  # noqa: E501

        :return: The office_online_enabled of this ConfigOffice.  # noqa: E501
        :rtype: bool
        """
        return self._office_online_enabled

    @office_online_enabled.setter
    def office_online_enabled(self, office_online_enabled):
        """Sets the office_online_enabled of this ConfigOffice.

        OfficeOnlineEnabled defines whether Office Online integration is enabled.  # noqa: E501

        :param office_online_enabled: The office_online_enabled of this ConfigOffice.  # noqa: E501
        :type: bool
        """
        if office_online_enabled is None:
            raise ValueError("Invalid value for `office_online_enabled`, must not be `None`")  # noqa: E501

        self._office_online_enabled = office_online_enabled

    @property
    def office_online_locale(self):
        """Gets the office_online_locale of this ConfigOffice.  # noqa: E501

        OfficeOnlineLocale is the locale of the Office Online web interface.  # noqa: E501

        :return: The office_online_locale of this ConfigOffice.  # noqa: E501
        :rtype: str
        """
        return self._office_online_locale

    @office_online_locale.setter
    def office_online_locale(self, office_online_locale):
        """Sets the office_online_locale of this ConfigOffice.

        OfficeOnlineLocale is the locale of the Office Online web interface.  # noqa: E501

        :param office_online_locale: The office_online_locale of this ConfigOffice.  # noqa: E501
        :type: str
        """

        self._office_online_locale = office_online_locale

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
        if issubclass(ConfigOffice, dict):
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
        if not isinstance(other, ConfigOffice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
