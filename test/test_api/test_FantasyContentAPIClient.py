import unittest
from unittest import mock

from requests import Session

from pymfl.api import FantasyContentAPIClient
from pymfl.api.config import APIConfig
from test.helper.helper_classes import MockResponse


class TestFantasyContentAPIClient(unittest.TestCase):
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
    def test_get_players_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_players(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_player_profile_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_player_profile(year=self.__TEST_YEAR,
                                                              league_id=self.__TEST_LEAGUE_ID,
                                                              player_id_or_ids="1")

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_all_rules_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_all_rules(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_player_ranks_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_player_ranks(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_adp_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_adp(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_aav_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_aav(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_top_adds_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_top_adds(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_top_drops_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_top_drops(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_top_starters_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_top_starters(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_top_trades_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_top_trades(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_top_owns_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_top_owns(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_site_news_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_site_news(year=self.__TEST_YEAR, league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])

    @mock.patch.object(Session, "get")
    def test_get_who_should_i_start_happy_path(self, mock_requests_get):
        mock_dict = {
            "k": "v"
        }

        mock_response = MockResponse(mock_dict, 200)
        mock_requests_get.return_value = mock_response
        response = FantasyContentAPIClient.get_who_should_i_start(year=self.__TEST_YEAR,
                                                                  league_id=self.__TEST_LEAGUE_ID)

        self.assertIsInstance(response, dict)
        self.assertEqual(1, len(response.keys()))
        self.assertEqual("v", response["k"])
