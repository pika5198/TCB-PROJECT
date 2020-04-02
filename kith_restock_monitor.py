import requests 
import json        
import jsonpath 
import re
import time
from discord import Webhook, RequestsWebhookAdapter, Embed

#KITH_MONITOR
last_data = set([])
product_url = "https://kith.com/products/aaef2229"
#tcb-ticket-webhook
whook_url = "https://ptb.discordapp.com/api/webhooks/694568207301869649/jNOfZmsnSxYSkK9RbW2cMpU_24hyyy5ZfIroWSw3RP29ZJ9Si0Ej3629DqfbwnKHfD-j"
def get_stock():
    global last_data
    headers = {
    'authority': 'kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'if-none-match': 'cacheable:78ee6411e4ad03f1b2edc31982c32e6d',
    }
    response = requests.get(product_url+".json", headers=headers)
    j = json.loads(response.text)
    size = j["product"]["tags"]
    a = re.compile(r'(?<=productsize-)\d+')
    src = j["product"]["images"]
    instock = a.findall(size)
    instock = set(map(int, instock))
    src = j["product"]["images"]
    title = j["product"]["title"]
    pic = []
    for i in src:
        pic.append(i['src'])
    return instock,title,pic

instock,title,pic=get_stock()

def send_weebhook(status,instock,pic,title):
    webhook = Webhook.from_url(whook_url, adapter=RequestsWebhookAdapter())    
    colors = 7329140
    embed = Embed(title=title, url=product_url,color=colors)
    embed.set_thumbnail(url=pic[1])
    embed.add_field(name=status, value=instock, inline=False) 
    embed.set_footer(text='@slom',icon_url='https://lh3.googleusercontent.com/proxy/DJ8iAOUFxJmqjBJjI8npKX_h1Ua0EnuUJRmqbonaiGR5WSl09186rnULj-z7imftnJDakqodY4BFM8hgASYkhvYFhg')
    webhook.send(content='KITH.com',embed=embed)
    
while True:
    instock = set(map(int, instock))
    if len(instock) == 0:
        print("Out of stock")
        time.sleep(10)
    elif len(last_data) == 0:
        send_weebhook('现有库存',sorted(list(instock)),pic,title)
        last_data = instock
    elif instock == last_data:
        print("没有变化")
        time.sleep(10)
    elif len(instock - last_data) > 0:
        send_weebhook('补货了',sorted(list(instock)),pic,title)
        last_data = instock
        time.sleep(2)
    elif len(last_data - instock) > 0:
        print("下货了", sorted(list(instock)))
        last_data = instock
        time.sleep(1) 
    else:
        # 两次的交集
        mix_data = instock & last_data
        if len(instock - mix_data) > 0:
            send_weebhook('补新货了',sorted(list(instock - mix_data)),pic,title)
        if len(last_data - mix_data) > 0:
            send_weebhook('补新货了',sorted(list(instock - mix_data)),pic,title)
            time.sleep(2)
    last_data=instock


