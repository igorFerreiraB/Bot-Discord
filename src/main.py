class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('MTEwNzQwMjE2OTYzNzk0OTU1MA.GkwdcC.sXATBtKoUVZSUov4zQU5zfmeoVfnA7ChEyBH_c')