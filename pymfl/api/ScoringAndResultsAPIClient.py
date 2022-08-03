from pymfl.api.MFLAPIClient import MFLAPIClient


class ScoringAndResultsAPIClient(MFLAPIClient):

    @classmethod
    def get_league_standings(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The current league standings for a given league.
        Private league access restricted to league owners.
        """
        # When set to a non-zero value, return a mapping of column keys to column names.
        # This also shows the proper order of the standings columns.
        column_names: str = kwargs.pop("column_names", None)
        filters = [("TYPE", "leagueStandings"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("COLUMN_NAMES", column_names, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
