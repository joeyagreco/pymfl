from pymfl.api import MFLAPIClient


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

    @classmethod
    def get_weekly_results(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The weekly results for a given league/week, including the scores for all starter and non-starter players for all franchises in a league.
        The week parameter can be "YTD" to give all year-to-date weekly results.
        Private league access restricted to league owners.
        """
        # If the week is specified, it returns the data for that week, otherwise the most current data is returned.
        # If the value is 'YTD', then it returns year-to-date data (or the entire season when called on historical leagues).
        week: int = kwargs.pop("week", None)
        filters = [("TYPE", "weeklyResults"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_live_scoring(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Live scoring for a given league and week, including:
        - Each franchise's current score
        - How many game seconds remaining that franchise has
        - Players who have yet to play
        - Players who are currently playing
        """
        # If the week is specified, it returns the data for that week, otherwise the most current data is returned.
        week: int = kwargs.pop("week", None)
        # Setting this argument to 1 will return data for non-starters as well
        details: int = kwargs.pop("details", None)
        filters = [("TYPE", "liveScoring"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("DETAILS", details, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_player_scores(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        All player scores for a given league/week, including all rostered players as well as all free agents.
        Private league access restricted to league owners.
        """
        # If the week is specified, it returns the data for that week, otherwise the current week data is returned.
        # If the value is 'YTD', then it returns year-to-date data.
        # If the value is 'AVG', then it returns a weekly average.
        week: int | str = kwargs.pop("week", None)
        # The year for the data to be returned.
        for_year: int = kwargs.pop("for_year", None)
        # Pass a list of player ids separated by commas (or just a single player id) to receive back just the info on those players.
        players: str = kwargs.pop("players", None)
        # Return only players from this position.
        position: str = kwargs.pop("position", None)
        # If set to 'freeagent', returns only players that are fantasy league free agents.
        status: str = kwargs.pop("status", None)
        # If set, and a league id passed, it re-calculates the fantasy score for each player according to that league's rules.
        # This is only valid when specifying the current year and current week.
        rules: str = kwargs.pop("rules", None)
        # Limit the result to this many players.
        count: int = kwargs.pop("count", None)
        filters = [("TYPE", "playerScores"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("YEAR", for_year, filters)
        cls._add_filter_if_given("PLAYERS", players, filters)
        cls._add_filter_if_given("POSITION", position, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        cls._add_filter_if_given("RULES", rules, filters)
        cls._add_filter_if_given("COUNT", count, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_projected_scores(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Given a player ID, calculate the expected fantasy points, using that league's scoring system.
        The system will use the raw stats that fantasysharks.com projects.
        Private league access restricted to league owners.
        """
        # If the week is specified, it returns the projected scores for that week, otherwise the upcoming week is used.
        week: int = kwargs.pop("week", None)
        # Pass a list of player ids separated by commas (or just a single player id) to receive back just the info on those players.
        players: str = kwargs.pop("players", None)
        # Return only players from this position.
        position: str = kwargs.pop("position", None)
        # If set to 'freeagent', returns only players that are fantasy league free agents (note that this refers to players that current free agents, not that were free agents during the specified week).
        status: str = kwargs.pop("status", None)
        # Limit the result to this many players.
        count: int = kwargs.pop("count", None)
        filters = [("TYPE", "projectedScores"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("PLAYERS", players, filters)
        cls._add_filter_if_given("POSITION", position, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        cls._add_filter_if_given("COUNT", count, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
