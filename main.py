import discord
import random


check_space = [
    [],
    [],
    [],
    [" 1", "1 "],
    [" 2", "2 "]
]

check_nospace = [
    ["quoi", "koi"],
    ["qui", "ki"],
    ["comment"],
    ["hein", "un"],
    ["de", "deux"],
    ["oui"],
    ["nan"],
    ["non"],
    ["allo"],
    ["chaud", "chau", "chauds"],
    ["what", "wat"],
    ["quoicoubeh", "quoicoub", "quoicoube"]
]

answers = [
    ["feur", "feur.", "feur!", "Feur.", "FEUR", "FEUR!!", "coubeh", "COUBEH", "QUOICOUBEH", ";)", "APANIAN"],
    ["quette", "ket", "KET", "QUETTE", "KI", "kou :3", "koulol", "Le ch'i (chinois simplifié : 气 ; chinois traditionnel : 氣 ; pinyin : qì ; Wade : ch'i ; EFEO : ts'i), ou ki (japonais : 気), ou encore chi, que l'on peut traduire par « flux d'énergie naturelle », est une notion des cultures chinoise et japonaise qui désigne un principe fondamental formant et animant l'univers et la vie"],
    ["DANT COUSTEAU", "DANTE CHE GUEVARA"],
    ["2", "deux", "DEUX", "deux?", "DEUX!", "deux x)", "deux xD", "deux ^^", "deux! ;)"],
    ["3", "trois", "TROIS", "Troyes", "Troy", "années x)", "ANNÉES!!", "années?", "années.", "MUSIQUE!", "DE MUSIQUE!", "DE MUSIQUE X)"],
    ["STITI", "stiti", "STITI!!!","STICRAM", "LLY WONKA", "lly wonka x)", "lly wonka", "STITI xD"],
    ["si", "cy", "CY", "NANCY"],
    ["bril", "BRIL", "BRIL X)", "BRIL!!"],
    ["à l'huile", "À L'HUILE", "A L'HUILE!!!!", "a l'huile ^_^", "alohomora", "ALOHOMORA"],
    ["CHAUSSURE", "CHAUSSETTE!", "CHAUSSETTE x)", "chocolat", "CHOCOLAT", "CHAUD CHAUD CHOCOLAT!", "CHAAUD DEVANT!", "CHAUD DEVANT x)", "CHAUDS LES MARRONS CHAUDS!", "CHAUUDS LES MARRONS CHAUDS x))", "CHAUD CACAO", "MAGE :D", "AH x)", "biz"],
    ["feur", "WATI B", "WATTOUAT", "fewr", "wati b!", "wattouat", "wati style", "wati shirt"],
    ["quoicouflop", "quoicounul", "quoicou tg", "quoicoustyle", "quoicoupatroopa", "quoicoubecousseh", "quoicoubecoussecoudeh", "...", "tg", "lol", "tu m'as bien eu xd", "bien joué!!"]
]

taslescramptes = ["hein?", "hein...", "quoi?", "quoi??", "QUOI", "QUOI? xd", "comment ?", "plait-il ?", "Plait-il ?", "pardon ?", "Pardon ?", "...", "oui", "non", "et toi?", "^^", "Excusez-moi?", "Pardonnez?"]

remove = [".", "!", "?", "`", "\n", "*", "`", "'"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return


        s = message.content.lower();
        s = s.replace("é", "e")
        s = s.replace("è", "e")
        s = s.replace("ê", "e")
        s = s.replace("ë", "e")
        
        if message.content == "1":
            await message.channel.send(answers[3][random.randint(0, len(answers[3]) - 1)])

        for r in remove:
            s = s.replace(r, "");

        if "demerde" in s:
            await message.channel.send("https://cdn.discordapp.com/attachments/759836645146755076/1103796462267158588/cover.jpg")
        

        for i in range(len(check_space)):
            for key in check_space[i]:
                if s.endswith(key):
                    await message.channel.send(answers[i][random.randint(0, len(answers[i]) - 1)])
                    return

        s = s.replace(" ", "")

        for i in range(len(check_nospace)):
            for key in check_nospace[i]:
                if s.endswith(key):
                    await message.channel.send(answers[i][random.randint(0, len(answers[i]) - 1)])
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