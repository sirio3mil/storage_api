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

class SettingsLanguage(object):
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
        'office_online_data_locale': 'str',
        'office_online_locale': 'str',
        'preferred': 'str'
    }

    attribute_map = {
        'office_online_data_locale': 'officeOnlineDataLocale',
        'office_online_locale': 'officeOnlineLocale',
        'preferred': 'preferred'
    }

    def __init__(self, office_online_data_locale=None, office_online_locale=None, preferred=None):  # noqa: E501
        """SettingsLanguage - a model defined in Swagger"""  # noqa: E501
        self._office_online_data_locale = None
        self._office_online_locale = None
        self._preferred = None
        self.discriminator = None
        if office_online_data_locale is not None:
            self.office_online_data_locale = office_online_data_locale
        if office_online_locale is not None:
            self.office_online_locale = office_online_locale
        if preferred is not None:
            self.preferred = preferred

    @property
    def office_online_data_locale(self):
        """Gets the office_online_data_locale of this SettingsLanguage.  # noqa: E501


        :return: The office_online_data_locale of this SettingsLanguage.  # noqa: E501
        :rtype: str
        """
        return self._office_online_data_locale

    @office_online_data_locale.setter
    def office_online_data_locale(self, office_online_data_locale):
        """Sets the office_online_data_locale of this SettingsLanguage.


        :param office_online_data_locale: The office_online_data_locale of this SettingsLanguage.  # noqa: E501
        :type: str
        """

        self._office_online_data_locale = office_online_data_locale

    @property
    def office_online_locale(self):
        """Gets the office_online_locale of this SettingsLanguage.  # noqa: E501


        :return: The office_online_locale of this SettingsLanguage.  # noqa: E501
        :rtype: str
        """
        return self._office_online_locale

    @office_online_locale.setter
    def office_online_locale(self, office_online_locale):
        """Sets the office_online_locale of this SettingsLanguage.


        :param office_online_locale: The office_online_locale of this SettingsLanguage.  # noqa: E501
        :type: str
        """

        self._office_online_locale = office_online_locale

    @property
    def preferred(self):
        """Gets the preferred of this SettingsLanguage.  # noqa: E501


        :return: The preferred of this SettingsLanguage.  # noqa: E501
        :rtype: str
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this SettingsLanguage.


        :param preferred: The preferred of this SettingsLanguage.  # noqa: E501
        :type: str
        """

        self._preferred = preferred

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
        if issubclass(SettingsLanguage, dict):
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
        if not isinstance(other, SettingsLanguage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
