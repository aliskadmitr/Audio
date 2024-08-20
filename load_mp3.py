from pydub import AudioSegment

audio = AudioSegment.from_wav("example.wav")

audio += 6
audio *= 2
audio = audio.fade_in(2000)

audio.export("mushup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mushup.mp3")
print("done")
