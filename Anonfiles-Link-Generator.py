import requests
import time
from discord_webhook import DiscordWebhook
from threading import Thread


def ID_Generator(lenght):
    import random
    str = []
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    num = int(lenght)
    for k in range(1, num+1):
        str.append(random.choice(chars))
    str = "".join(str)
    return str

def Generate():
    Name=""
    Full=""
    Size=""
    Temp=""
    i=1
    while i!=0:
        Request = requests.get('https://api.anonfiles.com/v2/file/'+ID_Generator(10)+'/info')
        print('I m Trying this : '+Request.url+' | Respons : '+str(Request.status_code))
        
        if(Request.status_code==200):
            Temp = Request.text.split(',')
            Name = Temp[5]
            Full = Temp[2]
            Full = Full.replace('\*','')
            Full = Full.replace("\"full\":\"","")
            Full = Full.replace('"}','')
            Size = Temp[4]
            webhook = DiscordWebhook(url='YOUR_DISCORD_WEBHOOK', content=Name+'\n'+Size+'\n'+Full+'\n')
            response = webhook.execute()


if __name__ == '__main__':

    file = open('config.txt','r')
    Config = file.readlines()    
    file.close()
    thds = Config[0].split('$')
    N = int(thds[1])  # Number of browsers to spawn
    thread_list = list()

    for i in range(N):
        t = Thread(name='Thread {}'.format(i), target=Generate,args=())
        t.start()
        print(t.name + ' started!')
        thread_list.append(t)
    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()
