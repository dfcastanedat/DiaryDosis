import pytest
from unittest.mock import MagicMock, patch

from requests.exceptions import HTTPError
from ..lol_spectator_api import LolSpectatorApi


@pytest.fixture
def lol_api():
    return LolSpectatorApi(region="test", api_key="test_api_key")


def test_send_secure_request_success(lol_api):
    # Define the expected behavior and response data
    expected_data = {"key": "value"}
    url = "https://test.api.riotgames.com/test_endpoint"

    # Mock the requests.get method to return the expected response data
    with patch("requests.Session.get") as mock_get:
        mock_get.return_value.json.return_value = expected_data

        # Call the method being tested
        response = lol_api.send_secure_request(url)

        # Assert that the response is as expected
        assert response == expected_data

        # Assert that the method was called with the expected URL and headers
        mock_get.assert_called_once_with(url, headers={"X-Riot-Token": "test_api_key"})


def test_send_secure_request_failure(lol_api):
    # Define the URL for a failed request
    url = "https://test.api.riotgames.com/non_existent_endpoint"

    # Mock the requests.get method to raise an exception
    with patch("requests.Session.get") as mock_get:
        # Create a MagicMock instance to represent the response
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = HTTPError("Mocked exception")
        mock_get.return_value = mock_response

        # Call the method being tested
        response = lol_api.send_secure_request(url)

        # # Assert that the response is None
        assert response is None


def test_get_platform_data(lol_api):
    # Define the expected platform data response
    expected_data = {"platform_data": "test_platform_data"}

    # Mock the send_secure_request method to return the expected response data
    with patch.object(lol_api, "send_secure_request") as mock_send_secure_request:
        mock_send_secure_request.return_value = expected_data

        # Call the method being tested
        platform_data = lol_api.get_platform_data()

        # Assert that the platform data is as expected
        assert platform_data == expected_data

        # Assert that send_secure_request was called with the correct URL
        mock_send_secure_request.assert_called_once_with(
            "https://test.api.riotgames.com/lol/status/v4/platform-data"
        )


def test_get_summoner_data_by_name(lol_api):
    # Define the summoner name and the expected URL
    summoner_name = "test_summoner"
    expected_url = f"https://test.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"

    with patch("requests.Session.get") as mock_get:
        lol_api.get_summoner_data_by_name(summoner_name)

        # Assert that requests.get was called with the correct URL and headers
        mock_get.assert_called_once_with(
            expected_url, headers={"X-Riot-Token": "test_api_key"}
        )

        # Assert that the method returned the correct result (this could be further improved if we knew the expected response)
        assert lol_api.get_summoner_data_by_name(summoner_name) is not None


def test_get_active_games_by_summoner(lol_api):
    # Define the encrypted PUUID and the expected URL
    encrypted_puuid = "test_encrypted_puuid"
    expected_url = f"https://test.api.riotgames.com/lol/spectator/v5/active-games/by-summoner/{encrypted_puuid}"

    with patch("requests.Session.get") as mock_get:
        expected_response = {"active_games": ["game1", "game2"]}
        mock_get.return_value.json.return_value = expected_response

        active_games = lol_api.get_active_games_by_summoner(encrypted_puuid)

        # Assert that requests.get was called with the correct URL and headers
        mock_get.assert_called_once_with(
            expected_url, headers={"X-Riot-Token": "test_api_key"}
        )

        # Assert that the method returned the correct result
        assert active_games == expected_response


# def test_create_diarydosis_file_success(lol_api):
#     # Step 1: Define the inputs and expected behavior of the create_diarydosis_file method
#     file_path = "test_template.bat"
#     encryption_key = "test_key"
#     game_id = "test_game_id"
#     expected_content = "Mocked template content"

#     # Step 2: Write a test case based on the expected behavior
#     with patch("builtins.open") as mock_open:
#         # Mock the open function to return a file object with the expected content
#         mock_open.side_effect = [
#             mock_open(read_data=expected_content),
#             mock_open(),
#         ]
        
#         # Call the method being tested
#         result = lol_api.create_diarydosis_file(file_path, encryption_key, game_id)
        
#         # Step 3: Implement the code to satisfy the test case
#         # Assert that open was called with the correct file path and that the file was written correctly
#         mock_open.assert_any_call(file_path, "r")
#         mock_open.assert_any_call("diarydosis.bat", "w")
        
#         # Assert that the method returned True to indicate success
#         assert result is True
