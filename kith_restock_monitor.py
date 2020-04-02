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
    embed.set_author(name='@slom')
    embed.set_footer(text='@slom',icon_url='data:image/jpeg;base64,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')
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
        time.sleep(3)
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


