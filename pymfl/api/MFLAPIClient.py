import xml.etree.ElementTree as ET
from abc import ABC
from typing import Optional, Any

import requests
from requests import Response, Session

from pymfl.api.config import APIConfig
from pymfl.enum import APIResponseType
from pymfl.exception import MFLAPIClientException
from pymfl.util import ConfigReader


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

    @staticmethod
    def _add_filter_if_given(key: str, value: Optional[Any], filter_list: list[tuple[str, Any]]):
        """
        Helper method for adding filters.
        """
        if value is not None:
            filter_list.append((key, value))

    @classmethod
    def _get_for_year_and_league_id(cls, *, url: str, year: int, league_id: str,
                                    api_response_type: APIResponseType = APIResponseType.JSON) -> dict | bytes:
        response = cls.__get_response_for_year_and_league_id(url=url, year=year, league_id=league_id)
        if api_response_type == APIResponseType.JSON:
            json_response = response.json()
            if "error" in json_response:
                raise MFLAPIClientException(json_response["error"])
            return json_response
        elif api_response_type == APIResponseType.CONTENT:
            return response.content

    @classmethod
    def __get_response_for_year_and_league_id(cls, *, url: str, year: int, league_id: str) -> Response:
        api_config = cls.__API_CONFIG.get_config_by_year_and_league_id(year=year, league_id=league_id)
        response = api_config.session.get(url)
        response.raise_for_status()
        return response

    @staticmethod
    def _post(url: str, body: dict = None, **kwargs) -> dict | ET.Element:
        if body is None:
            body = dict()
        as_xml = kwargs.pop("as_xml")
        session: Session = kwargs.pop("session")
        response = session.post(url, data=body)
        response.raise_for_status()
        if as_xml:
            xml_response = ET.fromstring(response.content)
            if xml_response.tag == "error":
                raise MFLAPIClientException(xml_response.text)
            return xml_response
        return response.json()
