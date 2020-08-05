# -*- coding:utf8 -*-
import cv2
import numpy as np
import os
import shutil

video = cv2.VideoCapture('./video/4.mp4')
width = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = (int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = video.get(cv2.CAP_PROP_FPS)

videoWriter = cv2.VideoWriter('./video/1_frame_video.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), fps, (width, height))

img = cv2.imread('./video/1.jpg')
imageFrame = cv2.resize(img, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)

# for i in range(0, 10):
videoWriter.write(imageFrame)


success, frame = video.read()

while success:
    frame = cv2.resize(frame, (int(width), int(height)), interpolation=cv2.INTER_CUBIC)
    videoWriter.write(frame)
    success, frame = video.read()    

videoWriter.release()

exit(0)

filename = '2.mp4'
count=6
    
# 保存图片的路径
savedpath = './video/'
# 开始读视频
videoCapture = cv2.VideoCapture(filename)
i = 0
j = 0
while True:
    success, frame = videoCapture.read()

    i += 1
    if not success:
        print('video read fail')
        break
    if (i % count == 0 and j < 6):
        # 保存图片
        j += 1
        savedname = filename.split('.')[0] + '_' + str(j) + '_' + str(i) + '.jpg'
        cv2.imwrite(savedpath + savedname, frame)
        print('image of %s is saved' % (savedname))
    

