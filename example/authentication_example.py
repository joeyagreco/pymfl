from pymfl.api.config import APIConfig

# You will need to log into your MyFantasyLeague account for the following setup.
# More info on this process can be found at: https://api.myfantasyleague.com/{current_year}/api_info
# Register a client via the API Client Registration Page: http://www.myfantasyleague.com/{current_year}/csetup?C=APICLI
# Set up your API Client, making sure that:
#   - Client Purpose = "Data Collection"
#   - Client User Agent is set (remember what this is as you will need it for the League Loader)
#   - Authorized Users has at least your MFL username
# Validate your client by selecting "Validate" for your newly-created client under "Configured Clients".
#   - This will validate your client by validating via text message.

# Before any API Clients can be used to retrieve information, the APIConfig must be set up.
# A configuration must be added for each league that you would like to get information on.

# Get a League object with years 2019 and 2020 for MyFantasyLeague league with ID: "123456".

MFL_USERNAME = "myUsername"  # The username for your MFL account.
MFL_PASSWORD = "myPassword"  # The password for your MFL account.
MFL_USER_AGENT_NAME = "myUserAgentName"  # The Client User Agent you set for your API Client.
LEAGUE_ID = "123456"

# Set up config for 2019
APIConfig.add_config_for_year_and_league_id(year=2019, league_id=LEAGUE_ID, username=MFL_USERNAME,
                                            password=MFL_PASSWORD, user_agent_name=MFL_USER_AGENT_NAME)

# Set up config for 2020
APIConfig.add_config_for_year_and_league_id(year=2020, league_id=LEAGUE_ID, username=MFL_USERNAME,
                                            password=MFL_PASSWORD, user_agent_name=MFL_USER_AGENT_NAME)

# After this configuration is done, you can use any APIClient to get data on your league for those years.
