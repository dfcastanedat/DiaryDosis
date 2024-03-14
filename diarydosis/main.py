# 1. http request to /lol/spectator/v5/active-games/by-summoner/{encryptedPUUID} using puuid hlpuNrEuoN6SijjQnbi3Qww7Jj75stvLHSd4XwVTlNjzXnTkvJe9v4AutMbim55G9jptzWz2HTA5Kw
# 2. Edit and run .bat script using mentioned puuid and game encryptionKey

import os
import requests
from dotenv import load_dotenv


class LolSpectatorApi:
    def __init__(self, region: str = "la1", api_key: str = None):
        """Initialize the LolSpectatorApi class.

        Args:
            region (str, optional): The region code for the Riot Games API. Defaults to "la1".
            api_key (str, optional): The API key for authentication. Defaults to None. Example: "RGAPI-xxxx-xxxx-xxxx-xxxx".
        """
        self.base_url = f"https://{region}.api.riotgames.com"
        self.api_key = api_key or os.getenv("RIOT_API_KEY")

    def send_secure_request(self, url: str) -> dict:
        """Send a secure request with API key authentication.

        Args:
            url (str): The URL for the API request.

        Returns:
            dict: A dictionary containing the API response.
        """
        headers = {"X-Riot-Token": self.api_key} if self.api_key else {}
        try:
            with requests.Session() as session:
                response = session.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        except requests.exceptions.RequestException as e:
            print(f"Error sending secure request: {e}")
            return None

        try:
            return response.json()
        except ValueError:
            print(f"Error parsing JSON response: {response.text}")
            return None

    def get_platform_data(self) -> dict:
        """Get platform data.

        Returns:
            dict: A dictionary containing the platform data.
        """
        url = f"{self.base_url}/lol/status/v4/platform-data"
        return self.send_secure_request(url)

    def get_active_games_by_summoner(self, encrypted_puuid: str) -> dict:
        """Get active games by summoner.

        Args:
            encrypted_puuid (str): The encrypted PUUID of the summoner.

        Returns:
            dict: A dictionary containing the active games information.
        """
        url = f"{self.base_url}/lol/spectator/v5/active-games/by-summoner/{encrypted_puuid}"
        return self.send_secure_request(url)


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
