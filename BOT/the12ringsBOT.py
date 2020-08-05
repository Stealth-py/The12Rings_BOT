import discord  # import the "discord" module
import login_webcrawler_12r
from discord.ext import commands

# token = 'NzM3NjM3NzAxMjU5NDkzMzc2.XyAQpA.hGN_xBipad9Idofq9t5Ii-UggFM'   copy your bot's token from your discord dev
# portal and paste it here
token = 'NzQwMjk0MzU5MzI4NzUxNzY2.Xym62Q.Q4PMJzVh5keLOybHGDmQ0TAtulA'

something = commands.Bot(command_prefix='12')

store = []
already_author = []
already_arg = []


@something.event
async def on_member_join(member):
    await member.send("Welcome to 12rings Players lounge, I am your friendly neighborhood bot and I will be giving you assistance, Firstly use the `12id <your player ID>` command here... then if your level is above 72, go to general channel and use the command `12addrole`")


@something.command()
async def Help(ctx):
    await ctx.send("To record your player ID, DM the bot and use the command `12id <your player ID>`. After you have "
                   "done that, send `12addrole` in general to get your role")


@something.command()
async def id(ctx, arg):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("Please wait, just like any human, for your ID to get recorded")
        global user, store, already_author, already_arg
        user = [str(ctx.author), arg]
        if len(arg) > 0 and arg.isdigit():
            if login_webcrawler_12r.lead_webcr((int(user[1]))) > 0:
                if (user[0] not in already_author) and (user[1] not in already_arg):
                    store.append(user)
                    if user[0] not in already_author:
                        already_author.append(user[0])
                    if user[1] not in already_arg:
                        already_arg.append(user[1])
                    await ctx.send("Your ID has been recorded")
                    channel = something.get_channel(740508339380682752)
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
    global store
    # print(store)
    # print(user, type(user[(str(ctx.author))]))
    for usr in store:
        if usr[0] == str(ctx.author):
            try:
                member = ctx.author
                print(member)
                if member is not None:
                    lvl = login_webcrawler_12r.lead_webcr(int(usr[1]))  # int(usr[(str(ctx.author))]))
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
