import time
import random
import requests 

def response(r):
    if r['ok'] is True:
        print('[' + time.ctime(time.time()) + ']', 'OK:', r['ok'], ';#' + str(r['result']['message_id']))
    else:
        print('[' + time.ctime(time.time()) + ']', 'OK:', r['ok'], '; Error:',r['error_code'],'\n',r['description'],)

class auto():
    def __init__(self):
        self.animememe_url = "https://meme-api.herokuapp.com/gimme/{text}"
        self.subreddits = ["Animememes", "Wholesomeanimemes", "Narutomemes", "JojoMemes", "Onepiecememes", "Memepiece", "AnimeFunny", "AnimeMirchi" "AnimeMeme", "AttackOnTitanmemes", "DankAnimeMemes", "Anime_Memes", "AnimeAnimemes", "GreatestAnimeMemes", "Goodanimemes", "animemes"]

    def animememe(self, token, chat):
        try:
            text = random.choice(SUBREDS)
            anime_url = requests.get(self.animememe_url.format(random.choice(self.subreddits))).json()['url']
            anime_name = requests.get(self.animememe_url.format(random.choice(self.subreddits))).json()['title']
            anime_post = requests.get(self.animememe_url.format(random.choice(self.subreddits))).json()['postLink']
            r = requests.get(
                "https://api.telegram.org/bot" + token + "/sendPhoto?chat_id=" + chat + "&photo=" + anime_url + f"&caption=[{anime_name}]({anime_post})" + "&parse_mode=MarkdownV2").json()
            response(r)
        except Exception as e:
            return "Something Error Occured Report To telegram.me/Aasf_CyberKing\n\n{}".format(e)
