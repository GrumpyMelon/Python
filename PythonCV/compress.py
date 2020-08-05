
from subprocess import call

video_name = './video/10_frame_video'

command = "ffmpeg -i %s.mp4 %s_c.mp4" % (video_name, video_name)
test = command.split()
print(test)
call(test)
