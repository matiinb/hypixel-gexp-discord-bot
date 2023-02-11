import requests
from collections import OrderedDict
import numpy as np

def topUser():

    # Get Guild Data
    url = 'https://api.hypixel.net/guild'
    apiKey = 'API_KEY'
    guildID = 'GUILD_ID'
    params = {'key': apiKey, 'id': guildID}

    r = requests.get(url = url, params = params)

    data = r.json()


    # Get Guild Members
    members = data['guild']['members']
    GEXPs = {}
    ranks = {}


    # Get GEXP for each Guild Member
    for member in members:
        tempoUUID = member['uuid']
        todayGEXP = list(member['expHistory'].values())[0]
        tempoRank = member['rank']

        if (todayGEXP != 0):
            GEXPs.update({tempoUUID: todayGEXP})
            ranks.update({tempoUUID: tempoRank})


    # Sort the Dictionary by GEXP Earned
    dictKeys = list(GEXPs.keys())
    dictValues = list(GEXPs.values())
    sorted_value_index = np.argsort(dictValues)
    sortedGEXPs = {dictKeys[i]: dictValues[i] for i in sorted_value_index}


    # Select the player with most GEXP earned
    topGEXP = list(sortedGEXPs.values())[-1]
    topUUID = list(sortedGEXPs.keys())[-1]
    topRank = ranks[topUUID]

    # Get the Minecraft IGN of the player with the most GEXP earned
    tempoData = requests.get(url='https://sessionserver.mojang.com/session/minecraft/profile/' + topUUID)
    username = tempoData.json()['name']

    topData = {'username': username, 'gexp': topGEXP, 'rank': topRank}

    return topData