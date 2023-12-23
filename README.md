# Squad-Discord-Activity-Status-Bot
A discord bot that will show your servers player count and current map as the discord bots playing status allowing a quick and easy way for your community to see what map is being played and how many players straight from your discord server. Alternatively if your server is offline, the bot will go into idle and diplay "Server Offline :(".

**Required Libs**
- discord.py (pip install discord.py)
- requests (pip install requests)
- itertools (pip install itertools)

This code is free to use and edit for your own use, the Battlemetrics and discord code are in sperate .py files in order to maintain simplicity and readability for maybe less experienced people trying to get it running.

<img width="237" alt="Screenshot 2023-12-23 at 12 07 59" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/62013be8-df4b-4ac8-a75b-252de10d3361">
<img width="232" alt="Screenshot 2023-12-23 at 12 08 10" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/8130d625-f7ec-45d2-944d-e9fd31c20c80">
<img width="235" alt="Screenshot 2023-12-23 at 12 09 59" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/8f7a35ab-0bc5-4800-b9b0-025d622d0057">


## Developers:
- LukeeSucks


## All You Need To Edit
The bot was made as simple as possible allowing an easy editing proccess for all below are all the things you will need to change to get it running.

you will need to get the unique server ID from the url of your server on battlemetrics (This is the numbers at the end of your servers url) and replace it with **unique_url_id** at the top of the **APIScript.py** file.

<img width="475" alt="Screenshot 2023-12-23 at 12 10 30" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/3ab0bc39-398a-4f03-a6a6-6e6680ea66af">

You will also need to get your API token from your battlemetrics account once created this will also need to be to be replaced with **battlemetrics_api_token** also at the top of the **APIScript.py** file.

<img width="308" alt="Screenshot 2023-12-23 at 12 11 59" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/a33fedcf-bc37-45bf-a499-1507fc626730">

Finally, you will need to get your bot token after you create your bot on the Discord Developer Portal and add replace **bot_token** at the bottom of **main.py** file.

<img width="173" alt="Screenshot 2023-12-23 at 12 16 38" src="https://github.com/LukeeSucks/Squad-Discord-Activity-Status-Bot/assets/105941171/7d3a72ee-cedf-40ed-b2be-9b8e12484879">

Any issues or questions feel free to message me on discord: **@lukeesucks**


