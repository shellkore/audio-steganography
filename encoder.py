import time
import wave

# song = wave.open("song.wav", mode='rb')
# # Read frames and convert to byte array
# frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# if __name__ == '__main__':
# 	print(time.time())

# song = wave.open("ign1.wav", mode='rb')
song = wave.open("name.wav", mode='rb')
numOfFrames = song.getnframes()

songFrames = song.readframes(numOfFrames)

print(type(songFrames))
# print(songFrames)
print('*'*20)

frame_bytes = bytearray(list(songFrames))

print(type(frame_bytes))
print(len(frame_bytes))
# print(frame_bytes)

string='Shellkore is Cool!!'
# Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
# Convert text to bit array
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

# Replace LSB of each byte of the audio data by one bit from the text bit array
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
# Get the modified bytes
frame_modified = bytes(frame_bytes)

# Write bytes to a new wave audio file
with wave.open('output.wav', 'wb') as outfile:
    outfile.setparams(song.getparams())
    outfile.writeframes(frame_modified)
song.close()