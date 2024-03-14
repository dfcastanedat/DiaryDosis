import os
from dotenv import load_dotenv
from lol_spectator_api import LolSpectatorApi


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Initialize LolSpectatorApi with API key from environment variable
    riot_api_key = os.getenv("RIOT_API_KEY")
    if not riot_api_key:
        print("Error: Riot API key not found.")
    else:
        lol_spectator_api = LolSpectatorApi(api_key=riot_api_key)
        platform_data = lol_spectator_api.get_platform_data()  # Health check
        if platform_data:
            print(platform_data)
        else:
            print("Failed to retrieve platform data.")

        summoner_name = "alexanderstar"
        summoner_data = lol_spectator_api.get_summoner_data_by_name(summoner_name)
        # Get puuid from summoner_data
        if puuid := summoner_data.get("puuid"):
            active_games = lol_spectator_api.get_active_games_by_summoner(puuid)
            if active_games:
                print(active_games)
                encryptionKey = active_games.get("observers").get("encryptionKey")
                game_id = str(active_games.get("gameId"))
                is_success = lol_spectator_api.create_diarydosis_file(
                    "diarydosis/windows_template.bat", encryptionKey, game_id
                )
                if is_success:
                    print("Successfully created diarydosis.bat file.")
                else:
                    print("Failed to create diarydosis.bat file.")
