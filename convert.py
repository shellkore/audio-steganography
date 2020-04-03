from os import path
from pydub import AudioSegment

# files                                                                         
src = "ignite.mp3"
dst = "ign1.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")