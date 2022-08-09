from pymfl.api.MFLAPIClient import MFLAPIClient


class UserFunctionsAPIClient(MFLAPIClient):

    @classmethod
    def get_my_leagues(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        All leagues of the current user.
        Private league access restricted to league owners.
        Personal user information, like name and email addresses only returned to league owners.
        """
        filters = [("TYPE", "myleagues"), ("JSON", 1)]
        # Set this argument to 1 to include the franchise names in the response.
        # Note that when this parameter is set and the user has a lot of leagues,
        # this response may take a long time to process and time out.
        franchise_names: int = kwargs.pop("franchise_names", None)
        cls._add_filter_if_given("FRANCHISE_NAMES", franchise_names, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_league_search_results(cls, *, year: int, league_id: str, search: str) -> dict:
        """
        Returns all leagues on MyFantasyLeague.com whose name match the specified string.
        """
        filters = [("TYPE", "leagueSearch"), ("SEARCH", search), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
