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
	ffmpeg_extract_subclip("sara.mp4",startvalue,remain,targetname=str(datetime.datetime.now())+".mp4")
else :
	for i in range(parts):
		ffmpeg_extract_subclip("sara.mp4",startvalue,endvalue,targetname=str(datetime.datetime.now())+".mp4")
		startvalue +=30
		print (startvalue)
		endvalue +=30
		print(endvalue)
	if remain>1:
		ffmpeg_extract_subclip("sara.mp4",startvalue,startvalue+remain,targetname=str(datetime.datetime.now())+".mp4")
		print(remain)

		

		
