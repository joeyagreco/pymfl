from pymfl.api.MFLAPIClient import MFLAPIClient


class CommonLeagueInfoAPIClient(MFLAPIClient):

    @classmethod
    def get_league(cls, *, year: int, league_id: str) -> None:
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, ("TYPE", "league"), ("L", league_id), ("JSON", 1))
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
