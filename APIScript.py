import requests

api_endpoint_base = "https://api.battlemetrics.com/servers"
api_token = "battlemetrics_api_token"
server_id = "unique_url_id"

latest_map = None
latest_player_count = None
latest_status = None

def update_server_info():
    global latest_map, latest_player_count, latest_status

    headers = {"Authorization": f"Bearer {api_token}"}
    api_endpoint = f"{api_endpoint_base}/{server_id}"

    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        server_data = response.json().get("data", {}).get("attributes", {})
        server_details = server_data.get("details", {})

        latest_map = server_details.get("map", "Unknown").replace("_", " ")
        latest_player_count = f"{server_data.get('players', '0')}/{server_data.get('maxPlayers', 'Unknown')}"
        latest_status = server_data.get('status', 'Unknown')
    else:
        print(f"Error retrieving server information. Status code: {response.status_code}")
        print(f"Error message: {response.text}")

def get_latest_map():
    global latest_map
    return latest_map

def get_latest_player_count():
    global latest_player_count
    return latest_player_count

def get_latest_status():
    global latest_status
    return latest_status
