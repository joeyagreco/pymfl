from dataclasses import dataclass

import requests.utils
from pymfl.exception import MissingYearAPIConfigException
from requests import Session


@dataclass(kw_only=True, frozen=True)
class YearAPIConfig:
    """
    Used to hold the API config for a single year/league combination.
    """
    league_id: str
    user_agent_name: str
    year: int
    session: Session


class APIConfig:
    """
    This class is used to store and set up initial API configuration.
    It should be set before any API calls are made.
    This is a BORG: https://code.activestate.com/recipes/66531/
    """
    config_by_year_and_league_id: dict[str, YearAPIConfig] = dict()

    @classmethod
    def get_config_by_year_and_league_id(cls, *, year: int, league_id: str) -> YearAPIConfig:
        try:
            return cls.config_by_year_and_league_id[f"{year}{league_id}"]
        except KeyError as e:
            raise MissingYearAPIConfigException(
                f"Cannot find YearAPIConfig for year '{year}' and league_id '{league_id}'.")

    @classmethod
    def add_config_for_year_and_league_id(cls, *, year: int, league_id: str, username: str, password: str,
                                          user_agent_name: str, session: Session=None):
        if not session:
            session = Session()
        cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)
        if not "MFL_USER_ID" in cookie_dict:
            from pymfl.api.SessionAPIClient import SessionAPIClient
            SessionAPIClient.get_mfl_user_id(year=year, username=username, password=password, session=session)
        cls.config_by_year_and_league_id[f"{year}{league_id}"] = YearAPIConfig(year=year,
                                                                               league_id=league_id,
                                                                               user_agent_name=user_agent_name,
                                                                               session=session)
