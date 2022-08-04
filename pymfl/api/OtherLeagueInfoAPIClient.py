from pymfl.api.MFLAPIClient import MFLAPIClient


class OtherLeagueInfoAPIClient(MFLAPIClient):

    @classmethod
    def get_future_draft_picks(cls, *, year: int, league_id: str) -> dict:
        """
        Future draft picks for a given league.
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "futureDraftPicks"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
