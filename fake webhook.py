
from threading import Timer
import datetime
import time
import json
from discord import Webhook, RequestsWebhookAdapter, Embed
import fake_webhook_inf


# storename = input('storename is:')
# size=input('size is:')
# profilename=input('profilename:')
def CyberWhook():
    webhook = Webhook.from_url(fake_webhook_inf.webhook_url(), adapter=RequestsWebhookAdapter())    
    colors = 7329140
    embed = Embed(title="Successfully checked out!", description=fake_webhook_inf.product_name(), color=colors)
    embed.add_field(name="store", value=fake_webhook_inf.store_name(), inline=True) 
    embed.add_field(name="Size", value=fake_webhook_inf.Size(), inline=True) 
    embed.add_field(name="profile", value="||{}||".format(fake_webhook_inf.profile()), inline=True)
    embed.add_field(name="Order", value="||{}||".format(fake_webhook_inf.Order()), inline=True)
    embed.add_field(name="Mode", value=fake_webhook_inf.Mode(), inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png?width=677&height=677")
    embed.set_footer(text='CyberAIO',icon_url="https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png?width=677&height=677")
    webhook.send(embed=embed,username=fake_webhook_inf.your_discord_name(),avatar_url=fake_webhook_inf.your_discord_avatar())

def  BalkoWhook():
    webhook = Webhook.from_url(fake_webhook_inf.webhook_url(), adapter=RequestsWebhookAdapter())
    colors = 3881787
    
    embed = Embed(title="Success - {}.com".format(fake_webhook_inf.store_name()), color=colors)
    embed.add_field(name="Size", value=fake_webhook_inf.Size(), inline=True)
    embed.add_field(name="product", value=fake_webhook_inf.product_name(), inline=True)
    embed.add_field(name="Delay", value=fake_webhook_inf.Delay(), inline=True)\
        .add_field(name="Proxies", value=fake_webhook_inf.Proxies(), inline=False)\
        .add_field(name="Tasks", value=fake_webhook_inf.Tasks(), inline=True)
    embed.set_thumbnail(url=fake_webhook_inf.product_picture())
    embed.set_footer(text='Blakobot',icon_url="https://pbs.twimg.com/profile_images/1177062169231405056/9whojPiW_400x400.jpg")
    webhook.send(embed=embed,username=fake_webhook_inf.your_discord_name(),avatar_url=fake_webhook_inf.your_discord_avatar())

def TKSWhook():
    webhook = Webhook.from_url(fake_webhook_inf.webhook_url(), adapter=RequestsWebhookAdapter())
    colors = 8278150
    time = datetime.datetime.now()
    embed = Embed(title="You cooked", color=colors)
    embed.add_field(name="Website", value=fake_webhook_inf.store_name(), inline=True)
    embed.add_field(name="product", value=fake_webhook_inf.product_name(), inline=True)
    embed.add_field(name="Size", value='||{}||'.format(fake_webhook_inf.Size()), inline=True) 
    embed.add_field(name="Price", value=fake_webhook_inf.price(), inline=True)
    embed.add_field(name="Link", value="www.{}.com".format(fake_webhook_inf.store_name()), inline=True)
    embed.add_field(name="profile", value="||{}||".format(fake_webhook_inf.profile()), inline=True)
    embed.add_field(name="proxy", value="||127.0.0.1:3128||", inline=True)
    embed.add_field(name="Time stamp", value=time, inline=True)

    embed.set_thumbnail(url="https://d6vlq12fn2gvh.cloudfront.net/uploads/item_image/image/1303/Adidas-Yeezy-Boost-350-V2-Citrin.png")
    webhook.send(content='KickStation just cooked',embed=embed,username=fake_webhook_inf.your_discord_name(),avatar_url=fake_webhook_inf.your_discord_avatar())

selcet = input('which bot u wanna test?(cyber,blako,tks):')
if selcet == 'cyber':
    CyberWhook()
elif selcet == 'blako':
    BalkoWhook()
elif selcet == 'tks':
    TKSWhook()
else:
    print('输入有误请重新选择。')

