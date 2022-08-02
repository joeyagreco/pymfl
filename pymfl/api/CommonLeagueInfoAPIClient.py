from pymfl.api.MFLAPIClient import MFLAPIClient


class CommonLeagueInfoAPIClient(MFLAPIClient):

    @classmethod
    def get_league(cls, *, year: int, league_id: str) -> dict:
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, ("TYPE", "league"), ("L", league_id), ("JSON", 1))
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_rules(cls, *, year: int, league_id: str) -> dict:
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, ("TYPE", "rules"), ("L", league_id), ("JSON", 1))
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_rosters(cls, *, year: int, league_id: str, **kwargs) -> dict:
        # When set, the response will include the current roster of just the specified franchise.
        franchise: str = kwargs.pop("franchise", None)
        # If the week is specified, it returns the roster for that week.
        # The week must be less than or equal to the upcoming week.
        # Changes to salary and contract info is not tracked so those fields (if used) always show the current values.
        week: int = kwargs.pop("week", None)
        filters = [("TYPE", "rosters"), ("L", league_id), ("JSON", 1)]
        if franchise:
            filters.append(("FRANCHISE", franchise))
        if week:
            filters.append(("W", week))
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_free_agents(cls, *, year: int, league_id: str, **kwargs) -> dict:
        # Return only players from this position.
        position: str = kwargs.pop("position", None)
        filters = [("TYPE", "freeAgents"), ("L", league_id), ("JSON", 1)]
        if position:
            filters.append(("POSITION", position))
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
