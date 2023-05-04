import discord
import random

answers_quoi = ["feur", "feur.", "feur!", "Feur.", "FEUR", "FEUR!!", "coubeh", "COUBEH", "QUOICOUBEH", ";)", "APANIAN"]
answers_comment = ["DANT COUSTEAU", "DANTE CHE GUEVARA"]
answers_hein = ["2", "deux", "DEUX", "deux?", "DEUX!"]

remove = [".", "!", "?", " ", "`", "\n", "\t"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        def send(message, array):
            message.channel.send(array[random.randint(0, len(array))])

        if message.author == self.user:
            return

        s = message.content.lower();
        for r in remove:
            s.replace(r, "");

        if s.endswith("quoi"):
            await send(message, answers_quoi)
        elif s.endswith("comment"):
            await send(message, answers_comment)
        elif s.endswith("hein"):
            await send(message, answers_hein)



file = open('token.txt', 'r')
token = file.read().replace('\n', '').replace('\t', '').replace(' ', '')

if token == "":
    print("No token in token.txt")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
print("Trying to log in with token '" + token + "'")
client = MyClient(intents=intents)
client.run(token)