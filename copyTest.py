import cv2
videoCapture = cv2.VideoCapture('/home/chris/projects/opencv/opencv-4.5.5/samples/data/Megamind.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    print("frame\n")
    success, frame = videoCapture.read()
exit()
