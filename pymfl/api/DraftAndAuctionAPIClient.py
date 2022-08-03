from pymfl.api.MFLAPIClient import MFLAPIClient


class DraftAndAuctionAPIClient(MFLAPIClient):

    @classmethod
    def get_draft_results(cls, *, year: int, league_id: str, **kwargs) -> dict:
        """
        Draft results for a given league.
        Note that this data may be up to 15 minutes delayed as it is meant to display draft results after a draft is completed.
        To access this data while drafts are in progress, check out this FAQ: https://api.myfantasyleague.com/2022/support?FAQ=935
        Private league access restricted to league owners.
        """
        filters = [("TYPE", "draftResults"), ("L", league_id), ("JSON", 1)]
        url = cls._build_route(cls._MFL_APP_BASE_URL, year, cls._EXPORT_ROUTE)
        url = cls._add_filters(url, *filters)
        return cls._get_for_year_and_league_id(url=url, year=year, league_id=league_id)
