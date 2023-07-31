# client to connect to linux server with speechbrain installed
import socket
import numpy as np
from scipy.io.wavfile import read

server_address = "127.0.0.1" # Localhost
server_port = 12345 # Port used by the server

# send a numpy array to server, currently not expecting response
def send_nparray_no_response(array):
    # Serialize the NumPy array using numpy.tobytes
    serialized_array = array.tobytes()
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_address, server_port))
        client_socket.sendall(len(serialized_array).to_bytes(4, byteorder='big'))
        client_socket.sendall(serialized_array)
        print("NumPy array sent successfully.")

        # # Receive the integer response from the server
        # # response_data = client_socket.recv(4) # Receiving 4-byte int
        # response = int.from_bytes(response_data, byteorder='big')
        # print("Received integer response from the server:", response)
    except Exception as e:
        print("Error occurred while sending data.")
        print(e)

    client_socket.close()

# send a string to server
def send_string(message):
    # Convert the string to bytes using utf-8 encoding
    message_bytes = message.encode('utf-8')

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))

        # Send the message length before sending the actual message
        client_socket.sendall(len(message_bytes).to_bytes(4, byteorder='big'))
        client_socket.sendall(message_bytes)
        print("String sent successfully.")

    except Exception as e:
        print("Error occurred while sending data.")
        print(e)

    client_socket.close()

# send a numpy array to server and get the response back for who the speaker is indetified to be
def send_nparray_for_identification(array):
    # Serialize the NumPy array using numpy.tobytes
    serialized_array = array.tobytes()
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_address, server_port))
        client_socket.sendall(len(serialized_array).to_bytes(4, byteorder='big'))
        client_socket.sendall(serialized_array)
        print("NumPy array sent successfully.")

        # # Receive the integer response from the server
        # response_data = client_socket.recv(4) # Receiving 4-byte int
        # response = int.from_bytes(response_data, byteorder='big')
        # print("Received integer response from the server:", response)

        # Receive the message length
        response_length_bytes = client_socket.recv(4)
        message_length = int.from_bytes(response_length_bytes, byteorder='big')

        data = b""
        while len(data) < message_length:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            data += chunk

        # Convert the received bytes back to a string using utf-8 decoding
        received_message = data.decode('utf-8')
        return received_message

    except Exception as e:
        print("Error occurred while sending data.")
        print(e)

    client_socket.close()

# a = read("./speaker_voice_sample/z.wav")
# numpy_array_to_send = np.array(a[1],dtype=float)
# send_nparray_no_response(numpy_array_to_send)
# send_string('hello')

# arr = np.load('./testing_stuff/numpy_sync_testing.npy')
# print(arr)
# send_nparray_no_response(arr)
# send_string('./numpy_sync_testing.npy')

