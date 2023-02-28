
import os
import simpleaudio as sa
from pydub import AudioSegment
from pydub.playback import play

# addVelocity
#   => input: audio sample
#   => output: audio file containing that sample at decreasing volumes separated by silence
#
# motivation
#   => allow velocity sensitive performance on non-velocity sensitive hardware
#   => output audio file can be imported to hardware and "sliced" across keys/pads
#   => each key/pad corresponds to one occurence of the sample within the aggregated velocity file
#   => playing across keys/pads allows for performance with velocity
#   => originally written to prep samples for a 1010Music BlackBox
# 
# to use:
#   1. prepare a source directory of audio samples
#   2. choose a destination directory for the processed samples
#   3. add directories below and run script
#   4. adjust amplification value (vol) to your needs

#AudioSegment.avconv = "/usr/local/Cellar/libav/12.3_7/bin/avconv.exe"

#source = "/Users/etaote/Documents/00_Music/Samples/00_Drums/Roland_TR626/Roland TR-626/"

source = "" # e.g. "/Useers/my_user/Samples/Roland_CR8000/"

destination = "" # e.g. "/Users/my_user/PreppedSamples/Roland_CR80000/"

print(os.listdir(source))
      
for filename in os.listdir(source):
    secondOfSilence = AudioSegment.silent(500) # inter
    sample = AudioSegment.from_wav(source + filename)

    itr = 1
    ruler = []
    for itr in range(16):

        vol = 11 - 1.9 * itr
        sampleWithVol = sample + vol
        ruler.append(sampleWithVol)
        ruler.append(secondOfSilence)
        
    result = secondOfSilence
    for i in range(0, len(ruler)):

        result = result + ruler[i]


    saveAs = "zz " + filename[0:len(filename) - 4] + " vel.wav"
    result.export(destination + saveAs, format = "wav")
    print(saveAs + " was exported!")
