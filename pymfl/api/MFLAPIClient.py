import xml.etree.ElementTree as ET
from abc import ABC
from http import HTTPStatus

import requests
from requests.structures import CaseInsensitiveDict

from pymfl.api.config.APIConfig import APIConfig
from pymfl.util.ConfigReader import ConfigReader


class MFLAPIClient(ABC):
    """
    Should be inherited by all API Clients.
    Sleeper API Documentation: https://api.myfantasyleague.com/2022/api_info
    """
    __API_CONFIG = APIConfig
    _MFL_APP_BASE_URL = ConfigReader.get("api", "mfl_app_base_url")

    # ROUTES
    _EXPORT_ROUTE = ConfigReader.get("api", "export_route")

    @classmethod
    def _build_route(cls, base_url: str, *args) -> str:
        args = (str(arg).replace("/", "") for arg in args)
        return f"{base_url}/{'/'.join(args)}"

    @classmethod
    def _add_filters(cls, url: str, *args) -> str:
        """
        Adds filters to the given url.
        """
        if len(args) > 0:
            symbol = "?"
            for i, arg in enumerate(args):
                if i > 0:
                    symbol = "&"
                url = f"{url}{symbol}{arg[0]}={arg[1]}"
        return url

    @classmethod
    def _get_for_year_and_league_id(cls, *, url: str, year: int, league_id: str) -> dict:
        api_config = cls.__API_CONFIG.get_config_by_year_and_league_id(year=year, league_id=league_id)
        headers = CaseInsensitiveDict()
        cookies = {"MFL_LAST_LEAGUE_ID": api_config.league_id, "MFL_USER_ID": api_config.mfl_user_id}
        response = requests.get(url, cookies=cookies)
        if response.status_code != HTTPStatus.OK:
            raise Exception("BAD STATUS CODE")  # TODO: better error handling
        return response.json()

    @staticmethod
    def _post(url: str, body: dict = None, **kwargs) -> dict | ET.Element:
        if body is None:
            body = dict()
        as_xml = kwargs.pop("as_xml")
        response = requests.post(url, data=body)
        if response.status_code != HTTPStatus.OK:
            raise Exception("BAD STATUS CODE")  # TODO: better error handling
        if as_xml:
            return ET.fromstring(response.content)
        return response.json()
