from time import sleep

from pydub import AudioSegment
from pydub.playback import play
import threading


if __name__ == '__main__':
    mp3File = 'resources/responses/success/right-away-boss.mp3'
    sound = AudioSegment.from_mp3(mp3File)
    thread = threading.Thread(target=play, args=(sound,))
    thread.start()
    print(1)
    sleep(2)
    print(2)
    sleep(3)