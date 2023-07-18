# coding: utf-8

"""
    DIGI storage API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.trash_api import TrashApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTrashApi(unittest.TestCase):
    """TrashApi unit test stubs"""

    def setUp(self):
        self.api = TrashApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_trash(self):
        """Test case for trash

        Get deleted files  # noqa: E501
        """
        pass

    def test_trash_empty(self):
        """Test case for trash_empty

        Empty trash  # noqa: E501
        """
        pass

    def test_trash_undelete(self):
        """Test case for trash_undelete

        Undelete files from trash  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()