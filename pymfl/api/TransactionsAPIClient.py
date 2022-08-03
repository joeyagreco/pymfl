from pymfl.api.MFLAPIClient import MFLAPIClient


class TransactionsAPIClient(MFLAPIClient):

    @classmethod
    def get_transactions(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        All non-pending transactions for a given league.
        Note that this can be a very large set, so it's recommended that you filter the result using one or more of the available parameters.
        If the request comes from an owner in the league, it will return the pending transactions for that owner's franchise.
        If it comes from the commissioner, it will return all pending transactions.
        Private league access restricted to league owners.
        """
        # If the week is specified, it returns the transactions for that week.
        week: int = kwargs.pop("week", None)
        # Returns only transactions of the specified type.
        # Types are: WAIVER, BBID_WAIVER, FREE_AGENT, WAIVER_REQUEST, BBID_WAIVER_REQUEST, TRADE, IR, TAXI, AUCTION_INIT, AUCTION_BID, AUCTION_WON, SURVIVOR_PICK, POOL_PICK.
        # You may also specify a value of * to indicate all transaction types or DEFAULT for the default transaction type set.
        # You can ask for multiple types by separating them with commas.
        trans_type: str = kwargs.pop("trans_type", None)
        # When set, returns just the transactions for the specified franchise.
        franchise: str = kwargs.pop("franchise", None)
        # When set, returns just the transactions for the number of days specified by this parameter.
        days: int = kwargs.pop("days", None)
        # Restricts the results to just this many entries.
        # Note than when this field is specified, only transactions from the most common types are returned.
        count: int = kwargs.pop("count", None)
        filters = [("TYPE", "transactions"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("W", week, filters)
        cls._add_filter_if_given("TRANS_TYPE", trans_type, filters)
        cls._add_filter_if_given("FRANCHISE", franchise, filters)
        cls._add_filter_if_given("DAYS", days, filters)
        cls._add_filter_if_given("COUNT", count, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_pending_waivers(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Pending waivers that the current franchise has submitted, but have not yet been processed.
        Access restricted to league owners.
        """
        # When request comes from the league commissioner, this indicates which franchise they want.
        # Pass in '0000' to get trades pending commissioner action).
        franchise_id: str = kwargs.pop("franchise_id", None)
        filters = [("TYPE", "pendingWaivers"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("FRANCHISE_ID", franchise_id, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_pending_trades(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Pending trades that the current franchise has offered to other franchises, or has been offered to by other franchises.
        Access restricted to league owners.
        """
        # When request comes from the league commissioner, this indicates which franchise they want.
        # Pass in '0000' to get trades pending commissioner action).
        franchise_id: str = kwargs.pop("franchise_id", None)
        filters = [("TYPE", "pendingTrades"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("FRANCHISE_ID", franchise_id, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_trade_bait(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        The Trade Bait for all franchises in a league.
        Private league access restricted to league owners.
        """
        # When set, this will also return draft picks offered.
        # Current year draft picks look like DP_02_05 which refers to the 3rd round 6th pick
        # (the round and pick values in the string are one less than the actual round/pick).
        # For future years picks, they are identified like FP_0005_2018_2
        # where 0005 refers to the franchise id who originally owns the draft pick, then the year and then the round
        # (in this case the rounds are the actual rounds, not one less).
        # This also includes Blind Bid dollars (in leagues that use them), which will be specified as BB_10 to indicate $10 in blind bid dollars.
        include_draft_picks: bool = kwargs.pop("include_draft_picks", None)
        filters = [("TYPE", "tradeBait"), ("L", league_id), ("JSON", 1)]
        cls._add_filter_if_given("INCLUDE_DRAFT_PICKS", include_draft_picks, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_assets(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        All tradable assets (players, current year draft picks, future draft picks) for a given league.
        Access restricted to league owners.
        """
        filters = [("TYPE", "assets"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
