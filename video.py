import moviepy.editor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import datetime
import easygui
#from tkinter.filedialog import askopenfilename

videopath=easygui.fileopenbox()
video=moviepy.editor.VideoFileClip(videopath)
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
	

		

		
