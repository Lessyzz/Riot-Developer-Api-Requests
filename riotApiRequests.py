#bylessy
import requests

class RiotAPIRequests():
    def __init__(self, apiKey : str, username: str, tag: str, region: str, server: str):
        self.api_key = apiKey
        self.username = username
        self.tag = tag
        self.region = region
        self.server = server

        self.puuid = None
        self.id = None
        self.name = None
        self.profileIconId = None
        self.summonerLevel = None

    def get_puuid_with_riotID(self): # Gets the puuid of the user with the riot id
        url = f"https://{self.region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{self.username}/{self.tag}?api_key={self.api_key}"
        response = requests.get(url).json()
        self.puuid = response["puuid"]
        return self.puuid

    def get_id_with_puuid(self): # Gets the id of the user with the puuid
        url = f"https://{self.server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{self.puuid}?api_key={self.api_key}"
        response = requests.get(url).json()
        self.id = response["id"]
        return self.id
    
    def get_name_with_puuid(self): # Gets the name of the user with the puuid
        url = f"https://{self.server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{self.puuid}?api_key={self.api_key}"
        response = requests.get(url).json()
        self.name = response["name"]
        return self.name
    
    def get_profile_icon_id_with_puuid(self): # Gets the profile icon id of the user with the puuid
        url = f"https://{self.server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{self.puuid}?api_key={self.api_key}"
        response = requests.get(url).json()
        self.profileIconId = response["profileIconId"]
        return self.profileIconId
    
    def get_summonerLevel_with_puuid(self): # Gets the summoner level of the user with the puuid
        url = f"https://{self.server}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{self.puuid}?api_key={self.api_key}"
        response = requests.get(url).json()
        self.summonerLevel = response["summonerLevel"]
        return self.summonerLevel

    def get_live_game_with_id(self): # Gets the live game of the user with the id
        url = f"https://{self.server}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{self.id}?api_key={self.api_key}"
        response = requests.get(url).json()
        return response
