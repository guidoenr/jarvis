import requests
import json
from pydub import AudioSegment
from pydub.playback import play


URL = "https://ttsmp3.com/makemp3_new.php"

data = {
    'msg': 'The current time in {} is {}',
    'lang': 'Brian',
    'source': 'ttsmp3'
}



if __name__ == '__main__':
    data['msg'] = data['msg'].format("united states", "21:30")
    response = requests.post(url=URL, data=data)
    response_data = json.loads(response.text)
    url = response_data['URL']
    mp3 = requests.get(url)
    open('x.mp3', 'wb').write(mp3.content)
    sound = AudioSegment.from_mp3('x.mp3')
    play(sound)
