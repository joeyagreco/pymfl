from pymfl.api.MFLAPIClient import MFLAPIClient
from pymfl.exception import MFLAPIClientException
from pymfl.util import ConfigReader

from requests import Session


class SessionAPIClient(MFLAPIClient):
    __LOGIN_ROUTE = ConfigReader.get("api", "login_route")

    @classmethod
    def get_mfl_user_id(cls, *, year: int, username: str, password: str, session: Session) -> str:
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls.__LOGIN_ROUTE)
        url = cls._add_filters(url, ("USERNAME", username), ("PASSWORD", password), ("XML", 1))
        response = cls._post(url, session=session, as_xml=True)
        if "MFL_USER_ID" not in response.attrib or response.attrib["MFL_USER_ID"] == "":
            raise MFLAPIClientException(f"Login failed: user={username}")
        return response.attrib["MFL_USER_ID"]
