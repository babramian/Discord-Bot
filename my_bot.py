import discord
from discord.ext import commands
import random

TOKEN = 'NTA3MDU1Njg3OTI3NDYzOTQ1.XUJGsA.Z8qeFNniLfbYVVUpEs7HSnr5nN4'

description = ''
client = commands.Bot(command_prefix='.', description=description)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

    # Sets role(s) to new members once they join the server the bot is running on
    role = discord.utils.get(member.guild.roles, name='Test Role')
    await member.add_roles(role)


#async def set_default_role():


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    replies = ['It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes, definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy, try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            "Don't count on it",
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful']
    
    await ctx.send(f'Question: {question}\nAnswer: {replies[random.randint(0, len(replies) - 1)]}')
    

@client.command()
async def clear(ctx, amount=5):
    if amount == 0:
        return
    await ctx.channel.purge(limit=amount)



client.run(TOKEN)