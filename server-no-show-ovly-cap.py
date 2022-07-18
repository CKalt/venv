# Welcome to Pyshone

# This code is for the server
# Lets import the libraries
import socket, cv2, pickle, struct

# Socket Create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
port = 9999
socket_address = (host_ip, port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:", socket_address)

# Socket Accept
while True:
        client_socket,addr = server_socket.accept()
        print('GOT CONNECTION FROM:', addr)
        if client_socket:
            frame_number = 0
            vid = cv2.VideoCapture(0)
            # Find OpenCV version
            (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
            if int(major_ver) < 3:
                fps = vid.get(cv2.cv.CV_CAP_PROP_FPS)
                size = (int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
            else:
                fps = vid.get(cv2.CAP_PROP_FPS)
                size = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))

            # CAPTURE USING VIDEO WRITER 264 MPEG-4
            output_file_name = 'MyOutputVid_264_MPEG-4.avi'
            fourcc = cv2.VideoWriter_fourcc(*'XVID')

            videoWriter = cv2.VideoWriter(
                         output_file_name,
                         fourcc,
                         fps, size)

            while (vid.isOpened()):
                img,frame = vid.read()
                frame_number += 1
                text = "Sec: %2.1f" % (frame_number/fps)
                frame = cv2.putText(
                  img = frame,
                  text = text,
                  org = (10, 100),
                  fontFace = cv2.FONT_HERSHEY_DUPLEX,
                  fontScale = 3.0,
                  color = (125, 246, 55),
                  thickness = 3
                )
                videoWriter.write(frame)

                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a))+a
                client_socket.sendall(message)
#                cv2.imshow('TRANSMITTING VIDEO', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()

