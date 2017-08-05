 -*- coding: utf-8 -*-

 License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
 Addon: LEDTV
 Author: 



import os            access operating system commands
import xbmc          the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon     pull addon specific information such as settings, id, fanart etc.
import xbmcplugin    contains functions required for creating directory structure style add-ons (plugins)

 The following are often used, we are not using them in this particular file so they are commented out

 import re            allows use of regex commands, if you're intending on scraping you'll need this
 import xbmcgui       gui based functions, contains things like creating dialog pop-up windows

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File



debug        = Addon_Setting(setting='debug')        Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id')  Grab our add-on id

 Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

 Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "PLRjomIk8urmEj_1boB4qG-sJfLLfbJqq2"
YOUTUBE_CHANNEL_ID_2 = "PLnDj4GODT_QpaemQB4395I9wRwCnZvx6x"
YOUTUBE_CHANNEL_ID_3 = "PLfb8E7lARImvzrAq0O6jyQcstw7aKZvLq"
YOUTUBE_CHANNEL_ID_4 = "PLlJDPmb6OexrDnAFNBNJez8zRe4EECDZY"
YOUTUBE_CHANNEL_ID_5 = "UCBDT-Kl4nHgEvpwYfLb315w"





----------------------------------------------------------------
 This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

 If debug mode is enabled show the koding tutorials
    if debug == 'true':
        Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )
    else:
        Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
    
# An example title/message we're going to send through to a popup dialog in the first Add_Dir item
    my_message= "{'title' : 'Support & Suggestions', 'msg' : \"If you come across any online content you'd like to get added please use the support thread at noobsandnerds.com and I'll be happy to look into it for you.\"}"

    Add_Dir(
        name="Support/Suggestions", url=my_message, mode="simple_dialog", folder=False,
        icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")
        
 Add some YT Playlists (see we're using BASE as the url)
    Add_Dir( 
        name="Popular Fly Fishing Videos", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://www.free-icons-download.net/images/fishing-icons-23810.png")

    Add_Dir( 
        name="Fly TV", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-ldvmtOEepRk/AAAAAAAAAAI/AAAAAAAAAAA/OOEsBMgcqQI/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Fishing videos from DALLMYD", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-HB9PwSeNSE8/AAAAAAAAAAI/AAAAAAAAAAA/LmADXY0mgbA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Sea Fishing videos from TAFishing", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://yt3.ggpht.com/-P2USlMtGNXo/AAAAAAAAAAI/AAAAAAAAAAA/sDV3FPYrotM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

Add some YT channels (see we're using BASE2 as the url for this one)
    Add_Dir( 
        name="Uncut Angling Channel", url=BASE2+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/-8Rt7LjDZrtU/AAAAAAAAAAI/AAAAAAAAAAA/-0-9PLOJWXM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'main_menu' route which opens the
    Main_Menu() function up at the top.
"""
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))