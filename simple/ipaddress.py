import requests
import json
import pre_requests
import os
import netifaces as ni
from pydub import AudioSegment
from pydub.playback import play

URL = "https://ttsmp3.com/makemp3_new.php"

def run():
    try:
        ni.ifaddresses('wlan0')
        data = pre_requests.data_ip
        ip = str(ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'])
        data['msg'] = data['msg'].format(ip=ip.replace(".","..."))
        response = requests.post(url=URL, data=data)
        response_data = json.loads(response.text)
        url = response_data['URL']
        mp3 = requests.get(url)
        open('x.mp3', 'wb').write(mp3.content)
        sound = AudioSegment.from_mp3('x.mp3')
        play(sound)
        os.remove('x.mp3')
    except:
        sound = AudioSegment.from_mp3('resources/responses/failure/i-cant-do-that.mp3')
        play(sound)
        
if __name__ == '__main__':
    run()
