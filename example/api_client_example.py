from pymfl.api import CommonLeagueInfoAPIClient, CommunicationsAPIClient, DraftAndAuctionAPIClient, \
    FantasyContentAPIClient, LeaguePlayersAPIClient, NFLContentAPIClient, OtherLeagueInfoAPIClient, \
    ScoringAndResultsAPIClient, TransactionsAPIClient, UserFunctionsAPIClient

# After your authentication and api config has been set up (see the authentication example for more info),
# you can use any APIClient to get information.

# Here is 1 example from each APIClient for getting 2020 data for a league with ID: "123456".
# Notes:
#   - These are not all the methods that are available, and to see what is all available you can check out each API Client.
#   - Many of these methods have optional parameters that can be passed in.
#   - These responses are returned as dictionary representations of the JSON API response.
#       - Some responses may have the content wrapped into a dictionary if JSON is not returned from the API.

YEAR = 2020
LEAGUE_ID = "123456"

playoff_bracket_response: dict = CommonLeagueInfoAPIClient.get_playoff_bracket(year=YEAR,
                                                                               league_id=LEAGUE_ID,
                                                                               bracket_id="1")

message_board_response: dict = CommunicationsAPIClient.get_message_board(year=YEAR, league_id=LEAGUE_ID, count=5)

draft_results_response: dict = DraftAndAuctionAPIClient.get_draft_results(year=YEAR, league_id=LEAGUE_ID)

players_response: dict = FantasyContentAPIClient.get_players(year=YEAR, league_id=LEAGUE_ID, details=1)

my_watch_list_response: dict = LeaguePlayersAPIClient.get_my_watch_list(year=YEAR, league_id=LEAGUE_ID)

nfl_schedule_response: dict = NFLContentAPIClient.get_nfl_schedule(year=YEAR, league_id=LEAGUE_ID, week="5")

rss_response: dict = OtherLeagueInfoAPIClient.get_rss(year=YEAR, league_id=LEAGUE_ID)

league_standings_response: dict = ScoringAndResultsAPIClient.get_league_standings(year=YEAR, league_id=LEAGUE_ID)

transactions_response: dict = TransactionsAPIClient.get_transactions(year=YEAR, league_id=LEAGUE_ID)

my_leagues_response: dict = UserFunctionsAPIClient.get_my_leagues(year=YEAR, league_id=LEAGUE_ID, franchise_names=1)
