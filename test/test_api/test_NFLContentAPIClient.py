import unittest
from unittest import mock

from requests import Session

from pymfl.api import NFLContentAPIClient
from pymfl.api.config import APIConfig
from test.helper.helper_classes import MockResponse


class TestNFLContentAPIClient(unittest.TestCase):
    __TEST_YEAR = 2020
    __TEST_LEAGUE_ID = "12345"
    __TEST_USERNAME = "username"
    __TEST_PASSWORD = "password"
    __TEST_USER_AGENT_NAME = "user_agent_name"

    @classmethod
    @mock.patch.object(Session, "post")
    def setUpClass(cls, mock_requests_post):
        mock_xml = """<status MFL_USER_ID="test_user_id=">OK</status>"""
        mock_response = MockResponse(dict(), 200, content=mock_xml)
        mock_requests_post.return_value = mock_response
        APIConfig.add_config_for_year_and_league_id(year=cls.__TEST_YEAR,
                                                    league_id=cls.__TEST_LEAGUE_ID,
                                                    username=cls.__TEST_USERNAME,
                                                    password=cls.__TEST_PASSWORD,
                                                    user_agent_name=cls.__TEST_USER_AGENT_NAME)

    @mock.patch.object(Session, "get")
    def test_get_injuries_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = NFLContentAPIClient.get_injuries(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_nfl_schedule_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = NFLContentAPIClient.get_nfl_schedule(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_nfl_bye_weeks_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = NFLContentAPIClient.get_nfl_bye_weeks(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_points_allowed_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = NFLContentAPIClient.get_points_allowed(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])
