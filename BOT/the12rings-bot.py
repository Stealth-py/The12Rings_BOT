import discord  # import the "discord" module
import login_webcrawler_12r
from discord.ext import commands

# copy your bot's token from your discord dev
# portal and paste it here
token = '<your-token-here>'

something = commands.Bot(command_prefix='12', case_insensitive=True)
something.remove_command('help')

store = []
already_author = []
already_arg = []


@something.event
async def on_member_join(ctx):
    msg = "Welcome to The 12 Rings Players Lounge. I am a bot and I can be used to give you access to some channels where discussion for your levels will take place. To understand how you can do that, go to the server and type 12Help (It's capital H, Do not use 12help)  in the general chat. Thank You"
    embedvar = discord.Embed(title="Welcome", color=0x6c0101)
    embedvar.add_field(name="Hello", value=msg, inline=False)
    await ctx.channel.send(embed=embedvar)


@something.command()
async def help(ctx):
    msg1 = "These commands will help you get access to the channel that holds the discussion for the current level. Follow these instructions:\n\n"
    msg2 = "Use `12id <your player ID>` [NOTE: THIS COMMAND IS TO BE **DMed (Directly messaged) TO THE BOT**]\nCommand example: __`12id XXXXX`__ (__XXXXX = YOUR PLAYER ID__)\nThis command registers your player ID with the bot\nIf you don't know your player ID, just log into your the12rings account and you will see a 5 digit number on the top left (That's your Player ID)\n\n"
    msg3 = "__After you have registered your ID with the bot, use the #addrole chat to enter the following command__ - __`12addrole`__\nThis command gives you the role to access the channel in which you can discuss your current level. (Please wait for some time, you WILL be given the role, do not spam any commands)\n\n"
    msg4 = "PLEASE ENTER YOUR ID VERY CAREFULLY BECAUSE IF YOU MESS UP YOUR ID IT WILL TAKE TIME FOR THE BOT ADMINS TO FIX THE MISTAKE AS WELL AS IT WILL TAKE TIME FOR YOU TO GET THE ROLE, PLEASE CONTACT THE ADMINS IN CASE YOU MAKE ANY MISTAKE. "
    embedvar = discord.Embed(title="Help", color=0x6c0101)
    embedvar.add_field(name="Help Section", value=msg1, inline=False)
    embedvar.add_field(name="1)", value=msg2, inline=False)
    embedvar.add_field(name="2)", value=msg3, inline=False)
    embedvar.add_field(name="P.S.", value=msg4, inline=False)
    await ctx.channel.send(embed=embedvar)


@something.command()
async def id(ctx, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("Please wait, just like any human, for your ID to get recorded")
        global user, store, already_author, already_arg
        user = [str(ctx.author.discriminator), arg]
        if len(arg) > 0 and arg.isdigit():
            if login_webcrawler_12r.lead_webcr((int(user[1]))) > 0:
                if (user[0] not in already_author) and (user[1] not in already_arg):
                    store.append(user)
                    if user[0] not in already_author:
                        already_author.append(user[0])
                    if user[1] not in already_arg:
                        already_arg.append(user[1])
                    await ctx.send("Your ID has been recorded")
                    channel = something.get_channel(740981553181491321)
                    await channel.send(f'the user {user[0]} has entered the ID {user[1]}')
                    await channel.send(store)

                else:
                    await ctx.send("This ID/User has already been registered")
                print(store, already_arg, already_author, sep='\n')
                f = open("test_data.txt", "a")
                f.write(str(store) + "\n")
                f.close()
            else:
                await ctx.send("The 12r ID {} doesn't exist".format(user[1]))
        else:
            await ctx.send("The 12r ID {} doesn't exist".format(user[1]))


@something.command(pass_context=True)
async def addrole(ctx):
    await ctx.send("Please wait, just like any human, to get your role...")
    await ctx.message.delete()
    global store
    for usr in store:
        if usr[0] == str(ctx.author.discriminator):
            try:
                member = ctx.author
                print(member)
                if member is not None:
                    lvls = login_webcrawler_12r.lead_webcr(int(usr[1]))  # int(usr[(str(ctx.author.discriminator))]))
                    for lvl in range(lvls, 72, -1):
                        role = discord.utils.get(ctx.guild.roles, name='q{}'.format(lvl))
                        if role is not None:
                            await member.add_roles(role)
                        else:
                            print("role not found")
                else:
                    print("member is none :))))")
            except:
                print("key_error")
        else:
            print("skipping those users who have not yet used the command 12addrole")


something.run(token)
