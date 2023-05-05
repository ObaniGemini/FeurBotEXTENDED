import discord
import random

answers = {
    "quoi": ["feur", "feur.", "feur!", "Feur.", "FEUR", "FEUR!!", "coubeh", "COUBEH", "QUOICOUBEH", ";)", "APANIAN"],
    "qui": ["quette", "ket", "KET", "QUETTE", "KI", "kou :3", "koulol", "Le ch'i (chinois simplifié : 气 ; chinois traditionnel : 氣 ; pinyin : qì ; Wade : ch'i ; EFEO : ts'i), ou ki (japonais : 気), ou encore chi, que l'on peut traduire par « flux d'énergie naturelle », est une notion des cultures chinoise et japonaise qui désigne un principe fondamental formant et animant l'univers et la vie"],
    "comment": ["DANT COUSTEAU", "DANTE CHE GUEVARA"],
    "hein": ["2", "deux", "DEUX", "deux?", "DEUX!", "deux x)", "deux xD", "deux ^^", "deux! ;)"],
    "oui": ["STITI", "stiti", "STITI!!!","STICRAM", "LLY WONKA", "lly wonka x)", "lly wonka", "STITI xD"],
    "nan": ["si", "cy", "CY", "NANCY"],
    "non": ["bril", "BRIL", "BRIL X)", "BRIL!!"],
    "allo": ["à l'huile", "À L'HUILE", "A L'HUILE!!!!", "a l'huile ^_^", "alohomora", "ALOHOMORA"],
    "chaud": ["CHAUSSURE", "CHAUSSETTE!", "CHAUSSETTE x)", "chocolat", "CHOCOLAT", "CHAUD CHAUD CHOCOLAT!", "CHAAUD DEVANT!", "CHAUD DEVANT x)", "CHAUDS LES MARRONS CHAUDS!", "CHAUUDS LES MARRONS CHAUDS x))", "CHAUD CACAO", "MAGE :D", "AH x)", "biz"],
    "what": ["feur", "WATI B", "WATTOUAT", "fewr", "wati b!", "wattouat", "wati style", "wati shirt"],
    "quoicoubeh": ["quoicouflop", "quoicounul", "quoicou tg", "quoicoustyle", "quoicoupatroopa", "quoicoubecousseh", "quoicoubecoussecoudeh", "...", "tg", "lol", "tu m'as bien eu xd", "bien joué!!"]
}

taslescramptes = ["hein?", "hein...", "quoi?", "quoi??", "QUOI", "QUOI? xd", "comment ?", "plait-il ?", "Plait-il ?", "pardon ?", "Pardon ?", "...", "oui", "non", "et toi?", "^^"]

remove = [".", "!", "?", " ", "`", "\n", "\t", "*", "`", "'"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        s = s.replace("é", "e")
        s = s.replace("è", "e")
        s = s.replace("ê", "e")
        s = s.replace("ë", "e")

        s = message.content.lower();
        for r in remove:
            s = s.replace(r, "");

        if "jeudemerde" in s or "jeuxdemerde" in s:
            await message.channel.send("https://cdn.discordapp.com/attachments/759836645146755076/1103796462267158588/cover.jpg")
        
        for key in answers.keys():
            if s.endswith(key):
                await message.channel.send(answers[key][random.randint(0, len(answers[key]) - 1)])
                return

        s = s.replace("s", "");
        if "lecrampte" in s or "lecrante" in s or "lecramte" in s:
            await message.channel.send(taslescramptes[random.randint(0, len(taslescramptes) - 1)])



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