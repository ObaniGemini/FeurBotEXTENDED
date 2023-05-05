import discord
import random

answers = {
    "quoi": ["feur", "feur.", "feur!", "Feur.", "FEUR", "FEUR!!", "coubeh", "COUBEH", "QUOICOUBEH", ";)", "APANIAN"],
    "comment": ["DANT COUSTEAU", "DANTE CHE GUEVARA"],
    "hein": ["2", "deux", "DEUX", "deux?", "DEUX!", "deux x)", "deux xD", "deux ^^", "deux! ;)"],
    "oui": ["STITI", "stiti", "STITI!!!","STICRAM", "LLY WONKA", "lly wonka x)", "lly wonka", "STITI xD"],
    "nan": ["si", "cy", "CY", "NANCY"],
    "allo": ["à l'huile", "À L'HUILE", "A L'HUILE!!!!", "a l'huile ^_^", "alohomora", "ALOHOMORA"],
    "chaud": ["CHAUSSURE", "CHAUSSETTE!", "CHAUSSETTE x)", "chocolat", "CHOCOLAT", "CHAUD CHAUD CHOCOLAT!", "CHAAUD DEVANT!", "CHAUD DEVANT x)", "CHAUDS LES MARRONS CHAUDS!", "CHAUUDS LES MARRONS CHAUDS x))", "CHAUD CACAO", "MAGE :D", "AH x)", "biz"]
}


remove = [".", "!", "?", " ", "`", "\n", "\t", "*", "`"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        s = message.content.lower();
        for r in remove:
            s = s.replace(r, "");

        for key in answers.keys():
            if s.endswith(key):
                await message.channel.send(answers[key][random.randint(0, len(answers[key]) - 1)])
                break

        if "jeudemerde" in s or "jeuxdemerde" in s:
            await message.channel.send("https://cdn.discordapp.com/attachments/759836645146755076/1103796462267158588/cover.jpg")


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