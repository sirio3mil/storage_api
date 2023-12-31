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

class LinksBundle(object):
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
        'links': 'list[Link]',
        'mounts': 'dict(str, Mount)'
    }

    attribute_map = {
        'links': 'links',
        'mounts': 'mounts'
    }

    def __init__(self, links=None, mounts=None):  # noqa: E501
        """LinksBundle - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._mounts = None
        self.discriminator = None
        self.links = links
        self.mounts = mounts

    @property
    def links(self):
        """Gets the links of this LinksBundle.  # noqa: E501


        :return: The links of this LinksBundle.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LinksBundle.


        :param links: The links of this LinksBundle.  # noqa: E501
        :type: list[Link]
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def mounts(self):
        """Gets the mounts of this LinksBundle.  # noqa: E501


        :return: The mounts of this LinksBundle.  # noqa: E501
        :rtype: dict(str, Mount)
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this LinksBundle.


        :param mounts: The mounts of this LinksBundle.  # noqa: E501
        :type: dict(str, Mount)
        """
        if mounts is None:
            raise ValueError("Invalid value for `mounts`, must not be `None`")  # noqa: E501

        self._mounts = mounts

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
        if issubclass(LinksBundle, dict):
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
        if not isinstance(other, LinksBundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
