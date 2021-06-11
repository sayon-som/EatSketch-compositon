#		python code
#		script_name: demo
#
#		author: Sayon Som
#		description: Composing a tune with effects.
#
#set up
from earsketch import *

init()
setTempo(120)#setting tempo ranging from 45 to 220
#music section
chord=RD_UK_HOUSE__5THCHORD_2
NextChord=HIPHOP_BASSSUB_001
beat=RD_UK_HOUSE_MAINBEAT_3
chord_2=HIPHOP_DUSTYMOOG_001
fitMedia(chord, 1, 1, 16)#starting from major 1 to major 16

setEffect(1,VOLUME,GAIN,-60,1,5,12)#adding effect from -60db to 5db
setEffect(1,VOLUME,GAIN,5,12,-60,16)#adding effect from 5db to again -60db
fitMedia(NextChord, 2, 1, 12)
#adding effect
setEffect(2,DELAY,DELAY_TIME,500)#ADDING DELAY

fitMedia(beat,3,1,8)
fitMedia(chord_2,4,1,5)
setEffect(3,REVERB,REVERB_TIME,200)#ADDING REVERB
#termination
finish()
