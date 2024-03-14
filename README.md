League of Legends API Interaction Project
=========================================

This Python project facilitates interaction with the League of Legends API. It allows users to make HTTP requests to the endpoint `/lol/spectator/v5/active-games/by-summoner/{encryptedPUUID}` using a specific encrypted PUUID (`hlpuNrEuoN6SijjQnbi3Qww7Jj75stvLHSd4XwVTlNjzXnTkvJe9v4AutMbim55G9jptzWz2HTA5Kw`). Additionally, it involves editing and running a `.bat` script that utilizes the mentioned PUUID and a game encryption key for specific operations related to the game.

Project Overview
----------------

The project includes functionalities to handle HTTP requests, process API responses, interact with the `.bat` script, and potentially perform other operations based on the retrieved data from the League of Legends API. The primary goal is to create a streamlined process for accessing game information and performing actions using the provided encrypted PUUID and encryption key.

Features
--------

*   Interact with League of Legends API
*   Make HTTP requests to the specified endpoint
*   Process API responses
*   Edit and execute a `.bat` script for game-related operations
*   Handle game encryption key for security
*   Spectate the ongoing game using the League of Legends Spectator feature

Usage
-----

1.  Clone the repository to your local machine:

bash

Copy code

`git clone https://github.com/your-username/league-of-legends-api.git`

2.  Navigate to the project directory:

bash

Copy code

`cd league-of-legends-api`

3.  Install the required dependencies:

bash

Copy code

`pip install -r requirements.txt`

4.  Edit the `.bat` script with your specific game encryption key.
    
5.  Run the Python script to interact with the League of Legends API:
    

bash

Copy code

`python main.py`

6.  After retrieving active game data, use the provided functionality to spectate the ongoing game.

Configuration
-------------

Before running the script, make sure to set up your League of Legends API key and encryption key. These keys should be securely stored and not shared publicly.

Contributions
-------------

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or create a pull request.

License
-------

This project is licensed under the [MIT License](LICENSE).

Disclaimer
----------

This project is not affiliated with or endorsed by Riot Games, Inc. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc.

* * *

Feel free to customize this README according to your project's specific requirements and details. Happy coding! 🎮👾