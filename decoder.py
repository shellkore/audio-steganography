import wave
def decode(inputFile = "output.wav"):
	song = wave.open(inputFile, mode='rb')
	# Convert audio to byte array
	frame_bytes = bytearray(list(song.readframes(song.getnframes())))

	# Extract the LSB of each byte
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	# Convert byte array back to string
	string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
	# Cut off at the filler characters
	decodedMsg = string.split("###")[0]

	# Print the extracted text
	# print("Sucessfully decoded: "+decoded)
	return decodedMsg
	song.close()

def main():
	finalMsg = decode()
	print(finalMsg)


if __name__ == '__main__':
	main()