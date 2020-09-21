from playsound import playsound
from subprocess import call
import win32api as win32
import win32con
import win32com.client
from time import sleep
from tweepy import OAuthHandler, API, parsers
from os import system
from pprint import pprint

def printAllScreen():
    i = 0
    while True:
        try:
            device = win32.EnumDisplayDevices(None,i);
            print("[%d] %s (%s)"%(i,device.DeviceString,device.DeviceName));
            i = i+1;
        except:
            break;
    return i

def play_me_a_song():
    playsound('audio.mp3')

def calc():
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Run("calc.exe")
    shell.AppActivate("calc.exe")
    sleep(2)
    shell.SendKeys("107123")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(1)
    shell.SendKeys("*3")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(1)
    shell.SendKeys("-462.5")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(1)
    shell.SendKeys("*4")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(1)
    shell.SendKeys("{+}45876")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(1)
    shell.SendKeys("*4")
    sleep(1)
    shell.SendKeys("{ENTER}")
    sleep(5)
    screen_count = printAllScreen()
    try:
        for x in range(0, screen_count):
            device = win32.EnumDisplayDevices(None, x);
            print("Rotate device %s (%s)" % (device.DeviceString, device.DeviceName));
            dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
            dm.DisplayOrientation = win32con.DMDO_180
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
            dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
            win32.ChangeDisplaySettingsEx(device.DeviceName, dm)
    except:
        pass
    sleep(5)
    try:
        for x in range(0, screen_count):
            device = win32.EnumDisplayDevices(None, x);
            print("Rotate device %s (%s)" % (device.DeviceString, device.DeviceName));
            dm = win32.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
            dm.DisplayOrientation = win32con.DMDO_DEFAULT
            dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
            dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
            win32.ChangeDisplaySettingsEx(device.DeviceName, dm)
    except:
        pass
    sleep(1)
    system('TASKKILL /F /IM calculator.exe')


def poller():
    User = "TheRealFrankFo1"
    tweets = api.user_timeline(User,count=1)[0]
    return tweets

def command_check(tweets):
    for i in range(0,len(tweets['entities']['hashtags'])):
        pprint(tweets['entities']['hashtags'][i]['text'])
        hashtag = tweets['entities']['hashtags'][i]['text']
        if hashtag == "WouldYouKindly":
            pprint("I WILL OBEY YOUR COMMAND")
            pprint(tweets['text'].split("#WouldYouKindly ")[1])
            command = tweets['text'].split("#WouldYouKindly ")[1]
            if command == "do some maths":
                calc()
            elif command == "play me a song":
                play_me_a_song()



API_Key =
API_Secret =
Access_Token =
Access_Token_secret =
auth = OAuthHandler(API_Key, API_Secret)
auth.set_access_token(Access_Token, Access_Token_secret)
api = API(auth, parser=parsers.JSONParser())

tweet_list = []
while True:
    tweets = poller()
    if tweets['id'] not in tweet_list:
        command_check(tweets)
        tweet_list.append(tweets['id'])
    sleep(30)
