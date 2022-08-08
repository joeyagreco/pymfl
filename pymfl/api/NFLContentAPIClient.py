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

    @classmethod
    def get_nfl_schedule(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The NFL schedule for one week of the season, including:
            - The scheduled kickoff of the game
            - Home team (and their score)
            - Away team (and their score)
        Starting with the 2020 season, this request will no longer update while games are in progress, and it's meant to be used to get the NFL schedule.
        To obtain the current scores of games, please check out this FAQ.
        """
        filters = [("TYPE", "nflSchedule"), ("JSON", 1)]
        # If the week is not specified, it defaults to the current week.
        # If set to 'ALL', it returns the full season schedule.
        week: str = kwargs.pop("week", None)
        cls._add_filter_if_given("W", week, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_nfl_bye_weeks(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The bye weeks for every NFL team.
        """
        filters = [("TYPE", "nflByeWeeks"), ("JSON", 1)]
        # If the week is specified, it returns just the teams with a bye in that week.
        week: int = kwargs.pop("week", None)
        cls._add_filter_if_given("W", week, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_points_allowed(cls, *, year: int, league_id: str) -> dict:
        """
        Fantasy points allowed by each NFL team, broken out by position.
        """
        filters = [("TYPE", "pointsAllowed"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
