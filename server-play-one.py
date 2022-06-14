# Welcome to Pyshone

# This code is for the server
# Lets import the libraries
import socket, pickle, struct
import cv2 as cv

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

cap = 'MyOutputVid_264_MPEG-4.avi'

# Socket Accept
while True:
        client_socket,addr = server_socket.accept()
        print('GOT CONNECTION FROM:', addr)
        if client_socket:
            cap = cv.VideoCapture(cap)
            while (cap.isOpened()):
                img,frame = cap.read()
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a))+a
                client_socket.sendall(message)
                cv.imshow('TRANSMITTING VIDEO', frame)
                key = cv.waitKey(1) & 0xFF
                if key == ord('q'):
                    client_socket.close()

