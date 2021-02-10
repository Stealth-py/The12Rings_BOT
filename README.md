# The 12 Rings Bot

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![current-status](https://img.shields.io/badge/Current%20Status%20of%20the%20Game-Finished-%236c0101)](https://the12rings.com/)]

This bot was made specifically for the moderation and for providing privacy to the players in higher levels of the game in The 12 Rings Players Lounge's official discord server.

## WORKING

### Registering the Player ID
> The bot accesses the leaderboard of 12r and stores it in a text file. We make roles for each question and each channel is made private to that specific role only, when a discord user dms the bot and uses the cmd `12id <player id>`, the bot goes through the leaderboard to see if the ID is valid, if the ID is valid the bot will record the ID of that user.

### Assigning Roles to the player
> After the ID has been recorded by the bot, the player would need to enter the command `12addrole`, in the required channel, and whenever this command is read by the bot, a script is run in the backend, which extracts the data from the current leaderboard, and the bot assigns the player with the role of the level the player is on, which does not allow players of levels below that of the current player to read chats of the current player's channel. Only, those on the same level or on levels higher than the current player's can see the channel and/or it's contents.

### How will the admins be moderating the bot
> We will have an audit logs channel that can be only seen by the bot admins and The12Rings, whenever a player registers his/her ID, we will know about it through logs. If someone enters an ID that is someone else's and has already been used, (for eg if someone tries to add my ID, and I've already registered my ID), the bot won't let the user register the ID, also one player cannot register ID two times, in other words, only one discord ID and only one player ID (both are unique) can exist in the bot's records.

### Error Handling
> If someone enters wrong ID by mistake, he/she can contact the admins and we can remove their ID from the recorded IDs, But it's a request that the ID should be carefully entered and in case you don't contact admins and enter a wrong ID, you will be questioned and if found guilty will be punished accordingly, Again, Please enter the ID carefully, the backend is full of data and correcting your mistake will be time consuming for you as well as the admins.


## HOSTING

> The bot will be hosted on a cloud platform, `Heroku`, which means the bot will be available 24/7, the bot will rarely go offline, almost never, but if it does the data is stored in recent logs and the admins will be able to record your IDs back.
