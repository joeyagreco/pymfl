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

    @classmethod
    def get_accounting(cls, *, year: int, league_id: str) -> dict:
        """
        Returns a summary of the league accounting records.
        In the response, negative amounts are charges against the franchise while positive amounts is money paid by the franchise or owed to the franchise.
        """
        filters = [("TYPE", "accounting"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_pool(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Returns a summary of the league accounting records.
        In the response, negative amounts are charges against the franchise while positive amounts is money paid by the franchise or owed to the franchise.
        """
        filters = [("TYPE", "pool"), ("L", league_id), ("JSON", 1)]
        # Which pool picks to return.
        # Valid values are "NFL" (default) or "Fantasy".
        pool_type: str = kwargs.pop("pool_type", None)
        cls._add_filter_if_given("POOLTYPE", pool_type, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_survivor_pool(cls, *, year: int, league_id: str) -> dict:
        """
        All survivor pool picks for a given league.
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "survivorPool"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
