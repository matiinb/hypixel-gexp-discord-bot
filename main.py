import random
import discord
from data import topUser

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

# rank_colors = {'Member': '32a852', 'Superior': '6232a8', 'Elite': 'a89732', 'Officer': 'a85632', 'GUILDMASTER': '329ba8'}

@bot.event
async def on_ready():
    print("Bot Ready.")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Glorified Bot"))

@bot.slash_command(name='guild_top', description='Announces the top GEXP earner of the day.')
async def guild_top(ctx):
    # channel_id = '[CHANNEL_ID]'
    # if ctx.channel.id == int(channel_id):

    res = topUser()
    # embed_color = int(rank_colors[res['rank']], base=16)
    embed = discord.Embed(title="Today's Top GEXP Earner", color=discord.Color.random())
    embed.set_footer(text='Hypixel Guild')
    embed.add_field(name='Congratulations!', value='', inline=False)
    embed.add_field(name='', value=f"`✧ {res['rank']} ✧ {res['username']}` earned `{res['gexp']:,} GEXP` today!", inline=False)

    await bot.get_channel(ctx.channel.id).send(embed=embed)
    await ctx.respond('Task Done.', ephemeral=True)

    # else:
        # await ctx.respond('Cannot run this command in the current channel.', ephemeral=True)

###########################

bot.run('BOT_TOKEN')