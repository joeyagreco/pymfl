from pymfl.api.MFLAPIClient import MFLAPIClient


class LeaguePlayersAPIClient(MFLAPIClient):

    @classmethod
    def get_player_roster_status(cls, *, year: int, league_id: str, player_id_or_ids: str, **kwargs) -> dict:
        """
        Get the player's current roster status.
        The franchise(s) the player is on are listed in the sub-element.
        There may more than one of this for leagues that have multiple copies of players.
        Each of these elements will have a franchise id and status attribute.
        The status attribute can be one of: R (roster), S (starter), NS (non-starter), IR (injured reserve) or TS (taxi squad).
        The R value is only provided when there's no lineup submitted or the caller has no visibility into the lineup.
        If the player is a free agent, there will be a 'is_fa' attribute on the parent element.
        In those cases the elements 'cant_add' and 'locked' attributes may be set indicating whether a player can't be added or is locked.

        player_id_or_ids: Player id or list of player ids separated by commas
        """
        filters = [("TYPE", "playerRosterStatus"), ("L", league_id), ("P", player_id_or_ids), ("JSON", 1)]
        # Week. If a week is specified, it returns the player status for that week.
        # The default is the current Live Scoring week.
        week: int = kwargs.pop("week", None)
        # Franchise ID.
        # If present it uses the franchise id to determine which conference or division to use for the purposes of identifying free agents.
        # If not present it uses the user's franchise id.
        # Only matters on deluxe leagues.
        franchise_id: str = kwargs.pop("franchise_id", None)
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("F", franchise_id, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_contest_players(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        On Contest Leagues, this returns all players eligible to be in a franchise's starting lineup.
        While this request can be used by any league, it's best suited for leagues with the loadRosters setting set to either 'contest' or 'setem'.
        Access restricted to league owners.
        """
        filters = [("TYPE", "contestPlayers"), ("L", league_id), ("JSON", 1)]
        # Week. If a week is specified, it returns the players for that week.
        # The default is the upcoming week.
        week: int = kwargs.pop("week", None)
        # Franchise ID.
        # If present it returns the players eligible for that franchise.
        # Only matters when called by the commissioner.
        # When called by an owner, this parameter is ignored and the owner's franchise is used.
        franchise_id: str = kwargs.pop("franchise_id", None)
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("F", franchise_id, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_my_watch_list(cls, *, year: int, league_id: str) -> dict:
        """
        My Watch List for the current franchise.
        Access restricted to league owners.
        """
        filters = [("TYPE", "myWatchList"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_salaries(cls, *, year: int, league_id: str) -> dict:
        """
        The current player salaries and contract fields.
        Only players with values are returned.
        If a value is empty it means that the default value is in effect.
        The default values are specified under the player id '0000'.
        """
        filters = [("TYPE", "salaries"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_salary_adjustments(cls, *, year: int, league_id: str) -> dict:
        """
        All extra salary adjustments for a given league.
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "salaryAdjustments"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
