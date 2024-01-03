from huesdk import Hue
import requests
import time

ip = '192.168.0.77'
username = 'MCFN3hMs1dzZljFXa8Vc7erk4ggEZXq9G9Ycf4nw'

def CreateUserName():
    print('Press the button on your bridge')
    input("Press Enter to continue...")
    username = Hue.connect(bridge_ip=HUE_IP)
    return username

def GetBridgeIP():
    URL = "https://discovery.meethue.com"
    return requests.get(url = URL).json()[0]['internalipaddress']

hue = Hue(bridge_ip=ip, username=username)

group = hue.get_group(name="Kontor")
group.off()
while True:
    group.on(transition=1)
    time.sleep(0.1)
    group.set_brightness(254)
    input("Press for OFF")
    group.off(transition=1)
    input("Press for ON")
