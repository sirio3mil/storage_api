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

class ConfigFrontend(object):
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
        'activity': 'ConfigFrontendActivity',
        'links': 'ConfigFrontendLinks',
        'mfa': 'ConfigFrontendMfa',
        'navigation': 'ConfigFrontendNavigation',
        'settings': 'ConfigFrontendSettings',
        'upgrade': 'ConfigFrontendUpgrade'
    }

    attribute_map = {
        'activity': 'activity',
        'links': 'links',
        'mfa': 'mfa',
        'navigation': 'navigation',
        'settings': 'settings',
        'upgrade': 'upgrade'
    }

    def __init__(self, activity=None, links=None, mfa=None, navigation=None, settings=None, upgrade=None):  # noqa: E501
        """ConfigFrontend - a model defined in Swagger"""  # noqa: E501
        self._activity = None
        self._links = None
        self._mfa = None
        self._navigation = None
        self._settings = None
        self._upgrade = None
        self.discriminator = None
        self.activity = activity
        self.links = links
        self.mfa = mfa
        self.navigation = navigation
        self.settings = settings
        self.upgrade = upgrade

    @property
    def activity(self):
        """Gets the activity of this ConfigFrontend.  # noqa: E501


        :return: The activity of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ConfigFrontend.


        :param activity: The activity of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendActivity
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

    @property
    def links(self):
        """Gets the links of this ConfigFrontend.  # noqa: E501


        :return: The links of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConfigFrontend.


        :param links: The links of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def mfa(self):
        """Gets the mfa of this ConfigFrontend.  # noqa: E501


        :return: The mfa of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendMfa
        """
        return self._mfa

    @mfa.setter
    def mfa(self, mfa):
        """Sets the mfa of this ConfigFrontend.


        :param mfa: The mfa of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendMfa
        """
        if mfa is None:
            raise ValueError("Invalid value for `mfa`, must not be `None`")  # noqa: E501

        self._mfa = mfa

    @property
    def navigation(self):
        """Gets the navigation of this ConfigFrontend.  # noqa: E501


        :return: The navigation of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendNavigation
        """
        return self._navigation

    @navigation.setter
    def navigation(self, navigation):
        """Sets the navigation of this ConfigFrontend.


        :param navigation: The navigation of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendNavigation
        """
        if navigation is None:
            raise ValueError("Invalid value for `navigation`, must not be `None`")  # noqa: E501

        self._navigation = navigation

    @property
    def settings(self):
        """Gets the settings of this ConfigFrontend.  # noqa: E501


        :return: The settings of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this ConfigFrontend.


        :param settings: The settings of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def upgrade(self):
        """Gets the upgrade of this ConfigFrontend.  # noqa: E501


        :return: The upgrade of this ConfigFrontend.  # noqa: E501
        :rtype: ConfigFrontendUpgrade
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this ConfigFrontend.


        :param upgrade: The upgrade of this ConfigFrontend.  # noqa: E501
        :type: ConfigFrontendUpgrade
        """
        if upgrade is None:
            raise ValueError("Invalid value for `upgrade`, must not be `None`")  # noqa: E501

        self._upgrade = upgrade

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
        if issubclass(ConfigFrontend, dict):
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
        if not isinstance(other, ConfigFrontend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
