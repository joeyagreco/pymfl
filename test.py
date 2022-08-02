from pymfl.api.CommonLeagueInfoAPIClient import CommonLeagueInfoAPIClient
from pymfl.api.config.APIConfig import APIConfig

if __name__ == "__main__":
    APIConfig.add_config_for_year_and_league_id(year=2019,
                                                username="joeyagreco",
                                                password="Zebrapurple17.",
                                                user_agent_name="joeyg-cua",
                                                league_id="67346")

    response = CommonLeagueInfoAPIClient.get_playoff_bracket(year=2019, league_id="67346", bracket_id="1")
    print()
