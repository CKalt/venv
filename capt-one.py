import cv2 as cv

cameraCapture = cv.VideoCapture(0)
fps = 30 
size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))

output_file_name = 'MyOutputVid_264_MPEG-4.avi'

# 264 MPEG-4
fourcc = cv.VideoWriter_fourcc(*'XVID')

videoWriter = cv.VideoWriter(
             output_file_name,
             fourcc,
             fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 *fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1





