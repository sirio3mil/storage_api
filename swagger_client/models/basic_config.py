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

class BasicConfig(object):
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
        'assets': 'ConfigAssets',
        'localization': 'ConfigLocalization',
        'mobile': 'ConfigMobile',
        'product': 'ConfigProduct'
    }

    attribute_map = {
        'assets': 'assets',
        'localization': 'localization',
        'mobile': 'mobile',
        'product': 'product'
    }

    def __init__(self, assets=None, localization=None, mobile=None, product=None):  # noqa: E501
        """BasicConfig - a model defined in Swagger"""  # noqa: E501
        self._assets = None
        self._localization = None
        self._mobile = None
        self._product = None
        self.discriminator = None
        self.assets = assets
        self.localization = localization
        self.mobile = mobile
        self.product = product

    @property
    def assets(self):
        """Gets the assets of this BasicConfig.  # noqa: E501


        :return: The assets of this BasicConfig.  # noqa: E501
        :rtype: ConfigAssets
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this BasicConfig.


        :param assets: The assets of this BasicConfig.  # noqa: E501
        :type: ConfigAssets
        """
        if assets is None:
            raise ValueError("Invalid value for `assets`, must not be `None`")  # noqa: E501

        self._assets = assets

    @property
    def localization(self):
        """Gets the localization of this BasicConfig.  # noqa: E501


        :return: The localization of this BasicConfig.  # noqa: E501
        :rtype: ConfigLocalization
        """
        return self._localization

    @localization.setter
    def localization(self, localization):
        """Sets the localization of this BasicConfig.


        :param localization: The localization of this BasicConfig.  # noqa: E501
        :type: ConfigLocalization
        """
        if localization is None:
            raise ValueError("Invalid value for `localization`, must not be `None`")  # noqa: E501

        self._localization = localization

    @property
    def mobile(self):
        """Gets the mobile of this BasicConfig.  # noqa: E501


        :return: The mobile of this BasicConfig.  # noqa: E501
        :rtype: ConfigMobile
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this BasicConfig.


        :param mobile: The mobile of this BasicConfig.  # noqa: E501
        :type: ConfigMobile
        """
        if mobile is None:
            raise ValueError("Invalid value for `mobile`, must not be `None`")  # noqa: E501

        self._mobile = mobile

    @property
    def product(self):
        """Gets the product of this BasicConfig.  # noqa: E501


        :return: The product of this BasicConfig.  # noqa: E501
        :rtype: ConfigProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this BasicConfig.


        :param product: The product of this BasicConfig.  # noqa: E501
        :type: ConfigProduct
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

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
        if issubclass(BasicConfig, dict):
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
        if not isinstance(other, BasicConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other