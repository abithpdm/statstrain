import moviepy.editor
#moviepy editor to import trim feature
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#module to get system time
import datetime
#easygui is a module to get gui for selcting files
import easygui
#from tkinter.filedialog import askopenfilename

#get the file user wanted to trim
videopath=easygui.fileopenbox()
#get the path of the selected video file
video=moviepy.editor.VideoFileClip(videopath)

#get the total duration of the video
duration=int(video.duration)
#get the total parts to be made to status
parts=duration/30
#not every part contain exact 30 minutes , so get the remaining time
remain=duration%30

#initial value of the starting point
startvalue=0
#initial end value
endvalue=30

#check whether the video is totally under 30 seconds
if parts<1 and remain >1:
	#using ffmpeg_extract_subclip we cut the video
	ffmpeg_extract_subclip(videopath,startvalue,remain,targetname=str(datetime.datetime.now())+".mp4")
	#the aattributes are : video file , starting time , ending time
else :
	for i in range(parts):
		ffmpeg_extract_subclip(videopath,startvalue,endvalue,targetname=str(datetime.datetime.now())+".mp4")
		startvalue +=30
		endvalue +=30
	if remain>1:
		ffmpeg_extract_subclip(videopath,startvalue,startvalue+remain,targetname=str(datetime.datetime.now())+".mp4")
