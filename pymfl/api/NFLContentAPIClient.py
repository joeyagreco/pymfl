from pymfl.api.MFLAPIClient import MFLAPIClient


class NFLContentAPIClient(MFLAPIClient):

    @classmethod
    def get_injuries(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The player ID, status (IR, Out, Doubtful, Questionable, Inactive, etc.) and details (i.e., 'Knee', 'Foot', 'Ribs', etc.)
        of all players on the NFL injury report.
        The report data is updated daily during the season and pre-season.
        The timestamp attribute tells you the last time this data was updated.
        """
        filters = [("TYPE", "injuries"), ("JSON", 1)]
        # If the week is not specified, it defaults to the most recent week that injury data is available.
        week: int = kwargs.pop("week", None)
        cls._add_filter_if_given("W", week, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
