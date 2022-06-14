import cv2

cameraCapture = cv2.VideoCapture(0)
fps = 30 
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter2 = cv2.VideoWriter(
            'MyOutputVid_MPEG-1.mpg', cv2.VideoWriter_fourcc('P','I','M','1'),
            fps, size)


success, frame = cameraCapture.read()
numFramesRemaining = 10 *fps - 1
while success and numFramesRemaining > 0:
    videoWriter1.write(frame)
    videoWriter2.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1





