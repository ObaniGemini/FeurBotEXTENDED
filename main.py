import discord
import random

answers_quoi = ["feur", "feur.", "feur!", "Feur.", "FEUR", "FEUR!!", "coubeh", "COUBEH", "QUOICOUBEH", ";)", "APANIAN"]
answers_comment = ["DANT COUSTEAU", "DANTE CHE GUEVARA"]
answers_hein = ["2", "deux", "DEUX", "deux?", "DEUX!", "deux x)", "deux xD", "deux ^^", "deux! ;)"]
answers_oui = ["STITI", "stiti", "STITI!!!","STICRAM", "LLY WONKA", "lly wonka x)", "lly wonka", "STITI xD"]
answers_nan = ["si", "cy", "CY", "NANCY"]

remove = [".", "!", "?", " ", "`", "\n", "\t"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        s = message.content.lower();
        for r in remove:
            s.replace(r, "");

        if s.endswith("quoi"):
            await message.channel.send(answers_quoi[random.randint(0, len(answers_quoi) - 1)])
        elif s.endswith("comment"):
            await message.channel.send(answers_comment[random.randint(0, len(answers_comment) - 1)])
        elif s.endswith("hein"):
            await message.channel.send(answers_hein[random.randint(0, len(answers_hein) - 1)])
        elif s.endswith("oui"):
            await message.channel.send(answers_oui[random.randint(0, len(answers_oui) - 1)])
        elif s.endswith("nan"):
            await message.channel.send(answers_nan[random.randint(0, len(answers_nan) - 1)])



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