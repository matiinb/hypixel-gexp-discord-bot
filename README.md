# Hypixel GEXP Discord Bot
You can use this Discord Bot for automatically getting the most amount of daily GEXP earned in a Hypixel Guild.


## NOTE
In order to get ANY type of data from the Hypixel API, you need to have an API Key. If you don't have one created yet:

1. Login to Hypixel.
2. Create a new API Key using `/api new`.
3. Copy the API Key and keep it in a safe place.
4. Replace it with the API Key in the code ([data.py](./data.py))


## Retrieveing the Hypixel Guild ID
For finding your Guild ID, you need to:

1. Copy the Minecraft UUID of the account that is already in the Hypixel Guild from `https://api.mojang.com/users/profiles/minecraft/[USERNAME]`
2. Retrieve the Hypixel Guild ID from `https://api.hypixel.net/findGuild?key=[API_KEY]&byUuid=[UUID]`
3. Copy the Guild ID and replace it in the code ([data.py](./data.py)).

**( Replace `API_KEY` with the API Key created on Hypixel and `UUID` with the Minecraft UUID retrieved in the first section )**


## Running the Bot
It is assumed that you already have a Discord Application and Discord Bot created in the [Discord Developer Portal](https://discord.com/developers/applications). If you have not created one yet, you can follow the instructions at the [Discord Developer Documentations](https://discord.com/developers/docs/intro).

After having a Discord Application/Bot set-up, you need to copy the Bot Token and store it in a safe place (Do NOT share the Token with others) and replace it with the Token in the code. ([main.py](./main.py))


## Libraries
To be able to run the code, you need to have a few Python Libraries installed on your machine.
These libraries include:

1. [PyCord](https://docs.pycord.dev/en/stable/installing.html)
2. [NumPy](https://numpy.org/install/)
3. [Requests](https://pypi.org/project/requests/)
