import os
import requests

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

    def get_summoner_data_by_name(self, summoner_name: str = "alexanderstar") -> dict:
        """
        Get summoner data by name.

        Args:
            summoner_name (str): The summoner name.

        Returns:
            dict: A dictionary containing the summoner data.
        """
        url = f"{self.base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
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

    def create_diarydosis_file(
        self, file_path: str, encryption_key: str, game_id: str
    ) -> bool:
        """Read a template file and replace variables.

        Args:
            file_path (str): The path to the template file.
            encryption_key (str): The encryption key to replace.
            game_id (str): The game ID to replace.

        Returns:
            bool: True if the file was successfully replaced, False otherwise.
        """
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"Error: Template file not found: {file_path}")
            return False

        file_content = file_content.replace("{{encryptionKey}}", encryption_key)
        file_content = file_content.replace("{{gameid}}", game_id)

        # write file into system
        try:
            with open("diarydosis.bat", "w") as file:
                file.write(file_content)
        except IOError:
            print("Error: Unable to write file diarydosis.bat")
            return False

        return True
