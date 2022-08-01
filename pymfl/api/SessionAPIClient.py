from pymfl.api.MFLAPIClient import MFLAPIClient
from pymfl.util.ConfigReader import ConfigReader


class SessionAPIClient(MFLAPIClient):
    __LOGIN_ROUTE = ConfigReader.get("api", "login_route")

    @classmethod
    def get_mfl_user_id(cls, *, year: int, username: str, password: str) -> str:
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls.__LOGIN_ROUTE)
        url = cls._add_filters(url, ("USERNAME", username), ("PASSWORD", password), ("XML", 1))
        response = cls._post(url, as_xml=True)
        return response.attrib["MFL_USER_ID"]  # TODO: do some error handling here
