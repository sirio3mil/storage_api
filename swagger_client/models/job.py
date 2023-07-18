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

class Job(object):
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
        'created': 'int',
        'id': 'str',
        'parameters': 'dict(str, object)',
        'progress': 'int',
        'result': 'dict(str, object)',
        'state': 'str',
        'type': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'parameters': 'parameters',
        'progress': 'progress',
        'result': 'result',
        'state': 'state',
        'type': 'type'
    }

    def __init__(self, created=None, id=None, parameters=None, progress=None, result=None, state=None, type=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._id = None
        self._parameters = None
        self._progress = None
        self._result = None
        self._state = None
        self._type = None
        self.discriminator = None
        self.created = created
        self.id = id
        self.parameters = parameters
        self.progress = progress
        self.result = result
        self.state = state
        self.type = type

    @property
    def created(self):
        """Gets the created of this Job.  # noqa: E501


        :return: The created of this Job.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Job.


        :param created: The created of this Job.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parameters(self):
        """Gets the parameters of this Job.  # noqa: E501


        :return: The parameters of this Job.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Job.


        :param parameters: The parameters of this Job.  # noqa: E501
        :type: dict(str, object)
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def progress(self):
        """Gets the progress of this Job.  # noqa: E501


        :return: The progress of this Job.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Job.


        :param progress: The progress of this Job.  # noqa: E501
        :type: int
        """
        if progress is None:
            raise ValueError("Invalid value for `progress`, must not be `None`")  # noqa: E501

        self._progress = progress

    @property
    def result(self):
        """Gets the result of this Job.  # noqa: E501


        :return: The result of this Job.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Job.


        :param result: The result of this Job.  # noqa: E501
        :type: dict(str, object)
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def state(self):
        """Gets the state of this Job.  # noqa: E501


        :return: The state of this Job.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Job.


        :param state: The state of this Job.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def type(self):
        """Gets the type of this Job.  # noqa: E501


        :return: The type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.


        :param type: The type of this Job.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other