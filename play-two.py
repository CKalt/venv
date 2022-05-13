# importing libraries
import cv2
import numpy as np
   
# Create a VideoCapture object and read from input file

vid = 'MyOutputVid_YUV.avi'
vid2 = 'MyOutputVid_MPEG-1.avi'

cap = cv2.VideoCapture(vid)
cap2 = cv2.VideoCapture(vid2)

# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# With webcam get(CV_CAP_PROP_FPS) does not work.
if int(major_ver) < 3:
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    fps2 = cap2.get(cv2.cv.CV_CAP_PROP_FPS)
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps2 = cap2.get(cv2.CAP_PROP_FPS)
    
print("fps = %2s" % fps)
print("fps2 = %2s" % fps2)
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
  
frame_number = 0
while(cap.isOpened() and cap2.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  ret2, frame2 = cap2.read()


  frame_number += 1

  if ret == True and ret2 == True:
    # Add text to both frames (fp
    text = "Sec: %2.1f" % (frame_number/fps)
    text2 = "Sec: %2.1f" % (frame_number/fps2)

    frame = cv2.putText(
      img = frame,
      text = text,
      org = (10, 100),
      fontFace = cv2.FONT_HERSHEY_DUPLEX,
      fontScale = 3.0,
      color = (125, 246, 55),
      thickness = 3
    )
    frame2 = cv2.putText(
      img = frame2,
      text = text2,
      org = (10, 100),
      fontFace = cv2.FONT_HERSHEY_DUPLEX,
      fontScale = 3.0,
      color = (125, 246, 55),
      thickness = 3
    )

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    cv2.imshow('Frame2', frame2)
   
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
cap2.release()
   
# Closes all the frames
cv2.destroyAllWindows()
