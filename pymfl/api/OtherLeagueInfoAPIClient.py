from pymfl.api import MFLAPIClient
from pymfl.enum import APIResponseType


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

    @classmethod
    def get_abilities(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Returns the abilities of the current franchise.
        A value of 0 means the franchise does not have the ability and a value of 1 means it has the ability. Test it!
        Access restricted to league owners.
        """
        filters = [("TYPE", "abilities"), ("L", league_id), ("JSON", 1)]
        # Franchise ID.
        # When the request comes from the commissioner, this indicates which franchise's abilities to return.
        # It's ignored if the request comes from an owner.
        franchise_id: str = kwargs.pop("franchise_id", None)
        details: int = kwargs.pop("details", None)
        cls._add_filter_if_given("F", franchise_id, filters)
        cls._add_filter_if_given("DETAILS", details, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_appearance(cls, *, year: int, league_id: str) -> dict:
        """
        The skin, home page tabs, and modules within each tab set up by the commissioner for a given league.
        """
        filters = [("TYPE", "appearance"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_rss(cls, *, year: int, league_id: str) -> dict:
        """
        An RSS feed of key league data for a given league, including:
            - league standings
            - current week's live scoring
            - last week's fantasy results
            - the five newest message board topics
        """
        filters = [("TYPE", "rss"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)

    @classmethod
    def get_ics(cls, *, year: int, league_id: str) -> str:
        """
        Returns a summary of the league calendar in .ics format.
        This format is suitable for importing into many modern calendaring programs such as:
            - Apple's Calendar
            - Google Calendar
            - Microsoft Outlook
        Access restricted to league owners.
        """
        filters = [("TYPE", "ics"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        response = cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id,
                                                   api_response_type=APIResponseType.CONTENT)
        return response.decode("utf-8")
