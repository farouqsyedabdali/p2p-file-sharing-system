#this file makes sure there is a reliable communication between the nodes
import socket

class NetworkManager:

    def __init__(self, ip, port):
        """ 
        ip: address (ip address) of the neighbor
        port: mailbox of the neighbor
        """
        self.ip = ip
        self.port = port

    def start_server(self, node):
        """
        Start the server to listen for incoming connections.
        Like setting up a mailbox to recieve the book pages.
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip, self.port))
        server.listen(5)
        print(f"Server started on {self.ip}:{self.port}")

        while True:
            conn, addr = server.accept() # Accepts incoming connections
            print(f"Accepted connection from {addr}")
            chunk = node.download_file_chunk(conn)

            if chunk:
                print(f"Received chunk: {chunk}")
            
            conn.close()
        
    def send_chunk(self, chunk, peer_ip, peer_port):
        """
        Connects to the peer and sends the chunk.
        Like sending a book page to a neighbor.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((peer_ip, peer_port)) # Connects to the neighbor's mailbox
            s.sendall(chunk) # Sends the chunk to the neighbor
            
        