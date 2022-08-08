from pymfl.api.MFLAPIClient import MFLAPIClient


class CommonLeagueInfoAPIClient(MFLAPIClient):

    @classmethod
    def get_league(cls, *, year: int, league_id: str) -> dict:
        """
        General league setup parameters for a given league.
        Personal user information like name and email addresses only returned to league owners.
        """
        filters = [("TYPE", "league"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_rules(cls, *, year: int, league_id: str) -> dict:
        """
        League scoring rules for a given league.
        """
        filters = ("TYPE", "rules"), ("L", league_id), ("JSON", 1)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_rosters(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The current rosters for all franchises in a league, including player status (active roster, IR, TS), as well as all salary/contract information for that player.
        """
        # When set, the response will include the current roster of just the specified franchise.
        franchise: str = kwargs.pop("franchise", None)
        # If the week is specified, it returns the roster for that week.
        # The week must be less than or equal to the upcoming week.
        # Changes to salary and contract info is not tracked so those fields (if used) always show the current values.
        week: int = kwargs.pop("week", None)
        filters = [("TYPE", "rosters"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("FRANCHISE", franchise, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_free_agents(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Fantasy free agents for a given league.
        Private league access restricted to league owners.
        """
        # Return only players from this position.
        position: str = kwargs.pop("position", None)
        filters = [("TYPE", "freeAgents"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("POSITION", position, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_schedule(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The fantasy schedule for a given league/week.
        Weeks in the past will show the score of each matchup.
        Private league access restricted to league owners.
        """
        # If a week is specified, it returns the fantasy schedule for that week, otherwise the full schedule is returned.
        week: int = kwargs.pop("week", None)
        # If a franchise id is specified, the schedule for just that franchise is returned.
        franchise_id: str = kwargs.pop("franchise_id", None)
        filters = [("TYPE", "schedule"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("F", franchise_id, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_calendar(cls, *, year: int, league_id: str) -> dict:
        """
        Returns a summary of the league calendar events.
        Access restricted to league owners.
        """
        filters = [("TYPE", "calendar"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_playoff_brackets(cls, *, year: int, league_id: str) -> dict:
        """
        All playoff brackets for a given league.
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "playoffBrackets"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_playoff_bracket(cls, *, year: int, league_id: str, bracket_id: str) -> dict:
        """
        Returns the games (with results if available) of the specified playoff bracket.
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "playoffBracket"), ("L", league_id), ("JSON", 1), ("BRACKET_ID", bracket_id)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
