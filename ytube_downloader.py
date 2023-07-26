from pytube import YouTube
import re
def user_selection():
	url=input("\033[1;32;40m Enter Youtube URL :\n")
	print ("\n1. Video\n2. MP3\n")
	select=int(input("Choose Your Download:\n"))
	if select==1:
		video=YouTube(url)
		print (video.title)
		list_video=video.streams.filter(progressive=True)
		for i in range(len(list_video)):
			print (i,".",list_video[i])
		print ("\n")
		sel_res=int(input("Choose Your Video:\n"))
		if sel_res:
			down_video=list_video.fmt_streams[sel_res]
			extension=str(down_video)
			ext=re.search("video/(\w*)",extension)
			ext1=ext.groups()[0]
			try:
				down_video.download(filename=video.title+"."+ext1)
				print ("Download Complete...")
			except:
				print ("Download Error")
		elif sel_res==0:
                        down_video=list_video.fmt_streams[0]
                        extension=str(down_video)
                        ext=re.search("video/(\w*)",extension)
                        ext1=ext.groups()[0]
                        try:
                                down_video.download(filename=video.title+"."+ext1)
                                print ("Download Complete...")
                        except:
                                print ("Download Error")
		else:
			print ("Please input your number choosen")
	elif select==2:
		music=YouTube(url)
		print (music.title)
		list_music=music.streams.filter(only_audio=True)
		for j in range(len(list_music)):
			print (j,".",list_music[j])
		print ("\n")
		sel_msc=int(input("Choose Your Audio file:\n"))
		if sel_msc:
			down_music=list_music.fmt_streams[sel_msc]
			msc_ext=str(down_music)
			audio=re.search("audio/(\w*)",msc_ext)
			audio1=audio.groups()[0]
			try:
				down_music.download(filename=music.title+".mp3")
				print ("Download Complete...")
			except:
				print ("Download Error")
		elif sel_msc==0:
                        down_music=list_music.fmt_streams[0]
                        msc_ext=str(down_music)
                        audio=re.search("audio/(\w*)",msc_ext)
                        audio1=audio.groups()[0]
                        try:
                                down_music.download(filename=music.title+".mp3")
                                print ("Download Complete...")
                        except:
                                print ("Download Error")
		else:
			print ("Please input your number choosen")
	else:
		print ("Correct Your Input NUMBER !!!")
user_selection()
