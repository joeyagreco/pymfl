from pymfl.api.MFLAPIClient import MFLAPIClient


class CommunicationsAPIClient(MFLAPIClient):

    @classmethod
    def get_message_board(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Display a summary of the recent message board posts to a league message board.
        Access restricted to league owners.
        """
        filters = [("TYPE", "messageBoard"), ("L", league_id), ("JSON", 1)]
        # If specified, limit the number of threads to display to this value.
        # Default is 10.
        count: str = kwargs.pop("count", None)
        cls._add_filter_if_given("COUNT", count, filters)
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
