import discord
from discord.ext import commands
import argparse
import random



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel_id", help="ID of channel to delete messages in (default all channels")
    parser.add_argument("--server", help="ID of server")
    parser.add_argument("--token", help="Discord authentication token")
    

    return parser.parse_args()

args = parse_args()

bot = commands.Bot(command_prefix="!test ")


@bot.event
async def on_ready():

    if not args.server:
        print("[*] You need to pass a server ID")
        exit(0)
    for guild in bot.guilds:
        if guild.id == int(args.server):
            channels = []
            if(args.channel_id):
                channels.append(args.channel_id)
            else:
                for channel in guild.text_channels:
                    channels.append(channel)

            for channel in channels:
                if(type(channel) == str):
                    channel = bot.get_channel(int(channel))
                print("[*] Getting all messages from channel, please standby")
                try:
                    messages = await channel.history(limit=None).flatten()
                except:
                    print("[*] ERROR: Tried accessing channel without perms")
                    messages = []
                print("[*] All messages have been collected")

                print("[*] Number of messages {}".format(len(messages)))
                msg_count = 0
                for message in messages:
                    print("[*] Attempting to delete message nr {} in channel {}".format(msg_count, channel))
                    msg_count = msg_count + 1
                    if message.author.id == bot.user.id:
                        try:
                            print("[*]Deleting message")
                            print("[*] Content {}".format(message.content))
                            print("[*] Message was created at {}".format(message.created_at))
                            await message.delete()
                            #time.sleep(random.randint(1,10))
                        except:
                            continue

    print("[*] Done")
    exit(0)

bot.run(args.token,bot=False)
