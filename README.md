League of Legends API Interaction Project
=========================================


Project Overview
----------------

This Python project facilitates interaction with the League of Legends API. It enables users to perform two main actions:
1. Send an HTTP request to retrieve active game data by summoner using the provided PUUID.
2. Edit and run a .bat script using the mentioned PUUID and game encryption key.


Features
--------

- Interact with the League of Legends API to retrieve platform data, summoner data, and active game information.
- Create a .bat script for specific game-related operations using retrieved data.


Usage
-----

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/dfcastanedat/DiaryDosis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd DiaryDosis
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment by creating a `.env` file and adding your Riot API key:

    ```
    RIOT_API_KEY=RGAPI-xxxx-xxxx-xxxx-xxxx
    ```

5. Run the Python script to interact with the League of Legends API:

    ```bash
    python main.py
    ```

6. After retrieving active game data, the script will create a `diarydosis.bat` file with the necessary parameters for game-related operations.


Configuration
-------------

Before running the script, make sure to set up your League of Legends API key and encryption key in the `.env` file. These keys should be securely stored and not shared publicly.


Contributions
-------------

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.


License
-------

This project is licensed under the [MIT License](LICENSE).


Disclaimer
----------

This project is not affiliated with or endorsed by Riot Games, Inc. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc.
