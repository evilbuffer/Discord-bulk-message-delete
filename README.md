# Why?
Due to Discord's inability to allow users to bulk delete messages, i saw the need to create my own tool for it.

# How?
Usage is fairly simple.\
There is the following args:
- channel_id (If you want to delete messages from a specific channel, defaults to all channels [Optional])
- server (ID of the server to delete messages from)
- token (Discord authentication token)

## Example
```bash
python3 deletemsg.py --token <token>  --server <server_id>
```

## Warning
Using selfbots are against Discord ToS, and you can get banned.\
To add a delay to the deletion, uncomment the line with #time.sleep(random.randint(1,10)).\
Also, the script loads all messages of the channel / server into memory, in some servers this can easily hit 1 million+.\
So the script can take a while to finish, but it will get trough them all, so make yourself a cup of coffee and watch a movie.
