import discord
import database
import weather
from discord.ext import commands


class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        # force the slash commands to sync with discord and if there's an error print it on terminal
        try:
            guild = discord.Object(id="disc_id")
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

# GUILD object that represent the discord server (id is the channel id)
GUILD_ID = discord.Object(id="DISC_ID")


# create a slash command to get weather by city
@client.tree.command(name="city_and_weather", description="Get Weather by city!", guild=GUILD_ID)
async def your_city(interaction: discord.Interaction, city: str):
    await interaction.response.send_message(weather.get_weather(city))


# create a slash command to access a user from a database then printout his weather
@client.tree.command(name="search_user", description="Search weather by user!", guild=GUILD_ID)
async def search_by_user(interaction: discord.Interaction, user: str):
    await interaction.response.send_message(database.search_by_user(user))


# create a slash command to enter the username and their city
@client.tree.command(name="user", description="Enter your name and your city!", guild=GUILD_ID)
async def add_name_and_city(interaction: discord.Interaction, name: str, city: str):
    await interaction.response.send_message(database.add_record(name, city))


client.run('TOKEN')
