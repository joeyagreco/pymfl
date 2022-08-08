from pymfl.api import MFLAPIClient


class FantasyContentAPIClient(MFLAPIClient):

    @classmethod
    def get_players(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        TODO: caching for this method
        All player IDs, names and positions that MyFantasyLeague.com has in our database for the current year.
        All other data types refer only to player IDs, so if you'd like to later present any data to people,
        you'll need this data type for translating player IDs to player names.
        Our player database is updated at most once per day, and it contains more than 2,000 players.
        In other words, you're strongly encouraged to read this data type no more than once per day and store it locally as needed to optimize your system performance.
        """
        filters = [("TYPE", "players"), ("JSON", 1)]
        # Set this value to 1 to return complete player details, including player IDs from other sources.
        details: int = kwargs.pop("details", None)
        # Pass a unix timestamp via this parameter to receive only changes to the player database since that time.
        since: str = kwargs.pop("since", None)
        # Pass a list of player ids separated by commas (or just a single player id) to receive back just the info on those players.
        players: str = kwargs.pop("players", None)
        cls._add_filter_if_given("DETAILS", details, filters)
        cls._add_filter_if_given("SINCE", since, filters)
        cls._add_filter_if_given("PLAYERS", players, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_player_profile(cls, *, year: int, league_id: str, player_id_or_ids: str) -> dict:
        """
        Returns a summary of information regarding a player, including DOB, ADP ranking, height/weight.

        player_id_or_ids: Player id or list of player ids separated by commas
        """
        filters = [("TYPE", "playerProfile"), ("P", player_id_or_ids), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_all_rules(cls, *, year: int, league_id: str) -> dict:
        """
        All scoring rules that MyFantasyLeague.com currently supports, including:
        if the rule is scored for players, teams or coaches, as well as an abbreviation of the scoring rule, a short description, and a detailed description.
        If you plan on using the 'rules' data type, you'll also need this data type to look up the abbreviations to translate them to their detailed description for people.
        """
        filters = [("TYPE", "allRules"), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_player_ranks(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        This report provides overall player rankings from the experts at FantasySharks.com.
        These rankings can be used instead of Average Draft Position (ADP) rankings for guidance during your draft, or when generating your own draft list.
        """
        filters = [("TYPE", "playerRanks"), ("JSON", 1)]
        position: str = kwargs.pop("POS", None)
        cls._add_filter_if_given("POS", position, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_adp(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        ADP results, including:
            - When the result were last updated
            - How many drafts the player was selected in
            - The average pick
            - Minimum pick
            - Maximum pick
        """
        filters = [("TYPE", "adp"), ("JSON", 1)]
        # This returns draft data for just drafts that started after the specified period. Valid values are ALL, RECENT, DRAFT, JUNE, JULY, AUG1, AUG15, START, MID, PLAYOFF.
        # This option is not valid for previous seasons.
        period: str = kwargs.pop("PERIOD", None)
        # This returns draft data from just leagues with this number of franchises.
        # Valid values are 8, 10, 12, 14 or 16.
        # If the value is 8, it returns data from leagues with 8 or fewer franchises.
        # If the value is 16 it returns data from leagues with 16 or more franchises.
        f_count: int = kwargs.pop("f_count", None)
        # Filters the data returned as follows:
        #   - If set to 0, data is from leagues that not use a PPR scoring system
        #   - If set to 1, only from PPR scoring system
        #   - If set to -1 (or not set), all leagues
        is_ppr: int = kwargs.pop("is_ppr", None)
        # Pass a string with some combination of N, K and R:
        #   - If N specified, returns data from redraft leagues
        #   - If 'K' is specified, returns data for keeper leagues
        #   - If 'R' is specified, return data from rookie-only drafts.
        # You can combine these.
        # If you specify 'KR' it will return rookie and keeper drafts only. Default is 'NKR'.
        is_keeper: str = kwargs.pop("is_keeper", None)
        # If set to 1, returns data from mock draft leagues only.
        # If set to 0, excludes data from mock draft leagues.
        # If set to -1, returns all
        is_mock: int = kwargs.pop("is_mock", None)
        # Only returns data for players selected in at least this percentage of drafts.
        # So if you pass 10, it means that players selected in less than 10% of all drafts will not be returned.
        # Note that if the value is less than 5, the results may be unpredictable.
        cutoff: int = kwargs.pop("cutoff", None)
        # If set to 1, it returns the leagues that were included in the results.
        # This option only works for the current season.
        details: int = kwargs.pop("details", None)

        cls._add_filter_if_given("PERIOD", period, filters)
        cls._add_filter_if_given("FCOUNT", f_count, filters)
        cls._add_filter_if_given("IS_PPR", is_ppr, filters)
        cls._add_filter_if_given("IS_KEEPER", is_keeper, filters)
        cls._add_filter_if_given("IS_MOCK", is_mock, filters)
        cls._add_filter_if_given("CUTOFF", cutoff, filters)
        cls._add_filter_if_given("DETAILS", details, filters)

        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_aav(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        AAV results, including:
            - When the result were last updated
            - How many auctions the player was selected in
            - Average auction value
        Average auction value is relative to an auction where a total of $1000 is available across all franchises.
        """
        filters = [("TYPE", "aav"), ("JSON", 1)]
        # This returns auction data for just auctions that started after the specified period.
        # Valid values are ALL, RECENT, DRAFT, JUNE, JULY, AUG1, AUG15, START, MID, PLAYOFF.
        # This option is not valid for previous seasons.
        period: str = kwargs.pop("period", None)
        # Filters the data returned as follows:
        #   - If set to 0, data is from leagues that not use a PPR scoring system
        #   - If set to 1, only from PPR scoring system
        #   - If set to -1 (or not set), all leagues
        is_ppr: int = kwargs.pop("is_ppr", None)
        # Pass a string with some combination of N, K and R:
        #   - If N specified, returns data from redraft leagues
        #   - If 'K' is specified, returns data for keeper leagues
        #   - If 'R' is specified, return data from rookie-only drafts
        # You can combine these.
        # If you specify 'KR' it will return rookie and keeper drafts only.
        # Default is 'NKR'.
        is_keeper: str = kwargs.pop("is_keeper", None)

        cls._add_filter_if_given("PERIOD", period, filters)
        cls._add_filter_if_given("IS_PPR", is_ppr, filters)
        cls._add_filter_if_given("IS_KEEPER", is_keeper, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_top_adds(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The most added players across all MyFantasyLeague.com-hosted leagues during the current week
        (or the past 7 days during the pre-season), as well as the percentage of leagues that they've been added in.
        Only players that have been added in at least 1% of our leagues will be returned.
        This data would be helpful in creating some sort of "Who's Hot?" list.
        """
        filters = [("TYPE", "topAdds"), ("JSON", 1)]
        # Limits the result to this many players.
        count: int = kwargs.pop("count", None)
        # Set this value to FA to only return available free agents.
        # This option is not available for deluxe leagues.
        status: str = kwargs.pop("status", None)
        cls._add_filter_if_given("COUNT", count, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_top_drops(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The most dropped players across all MyFantasyLeague.com-hosted leagues during the current week
        (or the past 7 days during the pre-season), as well as the percentage of leagues that they've been dropped in.
        Only players that have been dropped in at least 1% of our leagues will be displayed.
        This data would be helpful in creating some sort of "Who's Cold?" list.
        """
        filters = [("TYPE", "topDrops"), ("JSON", 1)]
        # Limits the result to this many players.
        count: int = kwargs.pop("count", None)
        # Set this value to FA to only return available free agents.
        # This option is not available for deluxe leagues.
        status: str = kwargs.pop("status", None)
        cls._add_filter_if_given("COUNT", count, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_top_starters(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The most started players across all MyFantasyLeague.com-hosted leagues for the current week,
        as well as the percentage of leagues that they've been started in.
        Only players that have been started in at least 1% of our leagues will be displayed.
        """
        filters = [("TYPE", "topStarters"), ("JSON", 1)]
        # Limits the result to this many players.
        count: int = kwargs.pop("count", None)
        # Set this value to FA to only return available free agents.
        # This option is not available for deluxe leagues.
        status: str = kwargs.pop("status", None)
        cls._add_filter_if_given("COUNT", count, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_top_trades(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The most traded players across all MyFantasyLeague.com-hosted leagues in the current week
        (or past 7 days during the pre-season),
        as well as the percentage of leagues that they have been traded in.
        Only players that are traded in more than 0.25% of our leagues will be displayed.
        """
        filters = [("TYPE", "topTrades"), ("JSON", 1)]
        # Limits the result to this many players.
        count: int = kwargs.pop("count", None)
        cls._add_filter_if_given("COUNT", count, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_top_owns(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The most owned players across all MyFantasyLeague.com-hosted leagues,
        as well as the percentage of leagues that they're owned in.
        Only players that are owned in more than 2% of our leagues will be displayed.
        """
        filters = [("TYPE", "topOwns"), ("JSON", 1)]
        # Limits the result to this many players.
        count: int = kwargs.pop("count", None)
        # Set this value to FA to only return available free agents.
        # This option is not available for deluxe leagues.
        status: str = kwargs.pop("status", None)
        cls._add_filter_if_given("COUNT", count, filters)
        cls._add_filter_if_given("STATUS", status, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_site_news(cls, *, year: int, league_id: str) -> dict:
        """
        An RSS feed of MyFantasyLeague.com site news.
        """
        filters = [("TYPE", "siteNews"), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_who_should_i_start(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Site-wide 'Who Should I Start?' data - offering a comparison between any two players at the same position,
        letting you know what percent of all MFL customers would choose one player over another player.
        Access restricted to league owners.
        """
        filters = [("TYPE", "whoShouldIStart"), ("JSON", 1)]
        # If specified, filter the results to the passed player ids (separated by commas).
        players: str = kwargs.pop("players", None)
        cls._add_filter_if_given("PLAYERS", players, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
