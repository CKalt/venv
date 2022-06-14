# importing libraries
import cv2 as cv
import numpy as np
   
# Create a VideoCapture object and read from input file

vid = 'MyOutputVid_264_MPEG-4.avi'

cap = cv.VideoCapture(vid)
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
   
    # Display the resulting frame
    cv.imshow('Frame', frame)
   
    # Press Q on keyboard to  exit
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv.destroyAllWindows()
