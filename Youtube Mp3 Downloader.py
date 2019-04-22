from win32gui import GetWindowText, GetForegroundWindow
import time
import webbrowser as wb
import urllib.request
import urllib.parse
import re
import youtube_dl

print("Open the youtube in 4 second and wait for 5-6 second at least")

time.sleep(4)
url = GetWindowText(GetForegroundWindow())
query_string = urllib.parse.urlencode( {"search_query": url } )
html_content = urllib.request.urlopen( "http://www.youtube.com/results?" + query_string )
search_results = re.findall( r'href=\"\/watch\?v=(.{11})', html_content.read().decode() )
urL = ("http://www.youtube.com/watch?v=" + search_results[0])
chrome_path=('C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe')
wb.register('chrome', None,wb.BackgroundBrowser(chrome_path))

options = options = {
    'format': 'bestaudio/best',
    'extractaudio': True,  # only keep the audio
    'audioformat': "mp3",  # convert to mp3
    'outtmpl': '%(title)s' + '.mp3',  # name the file the ID of the video
    'noplaylist': True,  # only download single song, not playlist
}  # save file as the YouTube ID
with youtube_dl.YoutubeDL( options ) as ydl:
        ydl.download( [urL] )