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

class ConfigLocalizationLanguage(object):
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
        'language': 'str',
        'name': 'str'
    }

    attribute_map = {
        'language': 'language',
        'name': 'name'
    }

    def __init__(self, language=None, name=None):  # noqa: E501
        """ConfigLocalizationLanguage - a model defined in Swagger"""  # noqa: E501
        self._language = None
        self._name = None
        self.discriminator = None
        self.language = language
        self.name = name

    @property
    def language(self):
        """Gets the language of this ConfigLocalizationLanguage.  # noqa: E501

        Language is a short code for the language.  # noqa: E501

        :return: The language of this ConfigLocalizationLanguage.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConfigLocalizationLanguage.

        Language is a short code for the language.  # noqa: E501

        :param language: The language of this ConfigLocalizationLanguage.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def name(self):
        """Gets the name of this ConfigLocalizationLanguage.  # noqa: E501

        Name is the full name of the language.  # noqa: E501

        :return: The name of this ConfigLocalizationLanguage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigLocalizationLanguage.

        Name is the full name of the language.  # noqa: E501

        :param name: The name of this ConfigLocalizationLanguage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(ConfigLocalizationLanguage, dict):
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
        if not isinstance(other, ConfigLocalizationLanguage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other