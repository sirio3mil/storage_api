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

class Device(object):
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
        'api_key': 'str',
        'can_edit': 'bool',
        'can_remove': 'bool',
        'id': 'str',
        'name': 'str',
        'provider': 'DeviceProvider',
        'root_mount_id': 'str',
        'search_enabled': 'bool',
        'space_free': 'int',
        'space_total': 'int',
        'space_used': 'int',
        'status': 'str',
        'version': 'int'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'can_edit': 'canEdit',
        'can_remove': 'canRemove',
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'root_mount_id': 'rootMountId',
        'search_enabled': 'searchEnabled',
        'space_free': 'spaceFree',
        'space_total': 'spaceTotal',
        'space_used': 'spaceUsed',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, api_key=None, can_edit=None, can_remove=None, id=None, name=None, provider=None, root_mount_id=None, search_enabled=None, space_free=None, space_total=None, space_used=None, status=None, version=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._api_key = None
        self._can_edit = None
        self._can_remove = None
        self._id = None
        self._name = None
        self._provider = None
        self._root_mount_id = None
        self._search_enabled = None
        self._space_free = None
        self._space_total = None
        self._space_used = None
        self._status = None
        self._version = None
        self.discriminator = None
        self.api_key = api_key
        self.can_edit = can_edit
        self.can_remove = can_remove
        self.id = id
        self.name = name
        self.provider = provider
        if root_mount_id is not None:
            self.root_mount_id = root_mount_id
        self.search_enabled = search_enabled
        self.space_free = space_free
        self.space_total = space_total
        self.space_used = space_used
        self.status = status
        self.version = version

    @property
    def api_key(self):
        """Gets the api_key of this Device.  # noqa: E501


        :return: The api_key of this Device.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Device.


        :param api_key: The api_key of this Device.  # noqa: E501
        :type: str
        """
        if api_key is None:
            raise ValueError("Invalid value for `api_key`, must not be `None`")  # noqa: E501

        self._api_key = api_key

    @property
    def can_edit(self):
        """Gets the can_edit of this Device.  # noqa: E501


        :return: The can_edit of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        """Sets the can_edit of this Device.


        :param can_edit: The can_edit of this Device.  # noqa: E501
        :type: bool
        """
        if can_edit is None:
            raise ValueError("Invalid value for `can_edit`, must not be `None`")  # noqa: E501

        self._can_edit = can_edit

    @property
    def can_remove(self):
        """Gets the can_remove of this Device.  # noqa: E501


        :return: The can_remove of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._can_remove

    @can_remove.setter
    def can_remove(self, can_remove):
        """Sets the can_remove of this Device.


        :param can_remove: The can_remove of this Device.  # noqa: E501
        :type: bool
        """
        if can_remove is None:
            raise ValueError("Invalid value for `can_remove`, must not be `None`")  # noqa: E501

        self._can_remove = can_remove

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501


        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.


        :param name: The name of this Device.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this Device.  # noqa: E501


        :return: The provider of this Device.  # noqa: E501
        :rtype: DeviceProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Device.


        :param provider: The provider of this Device.  # noqa: E501
        :type: DeviceProvider
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def root_mount_id(self):
        """Gets the root_mount_id of this Device.  # noqa: E501


        :return: The root_mount_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._root_mount_id

    @root_mount_id.setter
    def root_mount_id(self, root_mount_id):
        """Sets the root_mount_id of this Device.


        :param root_mount_id: The root_mount_id of this Device.  # noqa: E501
        :type: str
        """

        self._root_mount_id = root_mount_id

    @property
    def search_enabled(self):
        """Gets the search_enabled of this Device.  # noqa: E501


        :return: The search_enabled of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._search_enabled

    @search_enabled.setter
    def search_enabled(self, search_enabled):
        """Sets the search_enabled of this Device.


        :param search_enabled: The search_enabled of this Device.  # noqa: E501
        :type: bool
        """
        if search_enabled is None:
            raise ValueError("Invalid value for `search_enabled`, must not be `None`")  # noqa: E501

        self._search_enabled = search_enabled

    @property
    def space_free(self):
        """Gets the space_free of this Device.  # noqa: E501


        :return: The space_free of this Device.  # noqa: E501
        :rtype: int
        """
        return self._space_free

    @space_free.setter
    def space_free(self, space_free):
        """Sets the space_free of this Device.


        :param space_free: The space_free of this Device.  # noqa: E501
        :type: int
        """
        if space_free is None:
            raise ValueError("Invalid value for `space_free`, must not be `None`")  # noqa: E501

        self._space_free = space_free

    @property
    def space_total(self):
        """Gets the space_total of this Device.  # noqa: E501


        :return: The space_total of this Device.  # noqa: E501
        :rtype: int
        """
        return self._space_total

    @space_total.setter
    def space_total(self, space_total):
        """Sets the space_total of this Device.


        :param space_total: The space_total of this Device.  # noqa: E501
        :type: int
        """
        if space_total is None:
            raise ValueError("Invalid value for `space_total`, must not be `None`")  # noqa: E501

        self._space_total = space_total

    @property
    def space_used(self):
        """Gets the space_used of this Device.  # noqa: E501


        :return: The space_used of this Device.  # noqa: E501
        :rtype: int
        """
        return self._space_used

    @space_used.setter
    def space_used(self, space_used):
        """Sets the space_used of this Device.


        :param space_used: The space_used of this Device.  # noqa: E501
        :type: int
        """
        if space_used is None:
            raise ValueError("Invalid value for `space_used`, must not be `None`")  # noqa: E501

        self._space_used = space_used

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501


        :return: The status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.


        :param status: The status of this Device.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def version(self):
        """Gets the version of this Device.  # noqa: E501


        :return: The version of this Device.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Device.


        :param version: The version of this Device.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
