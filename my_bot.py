import discord
from discord.ext import commands
import random

TOKEN = 'NTA3MDU1Njg3OTI3NDYzOTQ1.XUJSuA.JVkkV3FYdj5jan-dSVt7m_4trTU'

description = ''
client = commands.Bot(command_prefix='.', description=description)
client.remove_command('help')

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


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.ping', value='Returns Pong! along with bot latency', inline=False)
    embed.add_field(name='.8ball (question)', value='Magic 8ball! Answers your question with precise accuracy!', inline=False)
    embed.add_field(name='.clear (num)', value='Admin command. Clears amount of messages specified. Default amount is 5.', inline=False)
    embed.add_field(name='.kick (@member) (reason)', value='Admin command. Kicks specified user.', inline=False)
    embed.add_field(name='.ban (@member) (reason)', value='Admin command. Bans specified user.', inline=False)
    embed.add_field(name='.unban (member name & ID)', value='Admin command. Unbans specified user.', inline=False)

    await author.send(embed=embed)


client.run(TOKEN)