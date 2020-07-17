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
parts=duration/30
remain=duration%30
startvalue=0
endvalue=30
if parts<1 and remain >1:
	ffmpeg_extract_subclip(videopath,startvalue,remain,targetname=str(datetime.datetime.now())+".mp4")
else :
	for i in range(parts):
		ffmpeg_extract_subclip(videopath,startvalue,endvalue,targetname=str(datetime.datetime.now())+".mp4")
		startvalue +=30
		endvalue +=30
	if remain>1:
		ffmpeg_extract_subclip(videopath,startvalue,startvalue+remain,targetname=str(datetime.datetime.now())+".mp4")
