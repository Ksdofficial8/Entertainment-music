from ISTKHARXMUSIC.core.bot import ISTKHAR
from ISTKHARXMUSIC.core.dir import dirr
from ISTKHARXMUSIC.core.git import git
from ISTKHARXMUSIC.core.userbot import Userbot
from ISTKHARXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
