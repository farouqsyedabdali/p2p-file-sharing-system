import socket

class P2PNode:

    # A class to represent a P2P node.
    
    def __init__(self, node_id, ip, port):

        """
        node_id: name of the neighbor
        ip: address (ip address) of the neighbor
        port: mailbox of the neighbor
        peers: list of neighbors

        """

        self.node_id = node_id
        self.ip = ip
        self.port = port
        self.peers = []

    def upload_file_chunk(self, file_chunk):

        """
        Uploads the file chunk to the peer.

        Neighbor is saying "Here is the part of the book you wanted"
        """

        pass

    def download_file_chunk(self, peer):

        """
        Downloads the file chunk from the peer.

        You are saying "Can you share the part of the book with me?"
        """
        pass

    def add_peer(self, peer_ip, peer_port):
        # Adds neighbor contact information to the list of neighbors.
        self.peers.append((peer_ip, peer_port))

    def connect_to_peer(self, peer_ip, peer_port):
        """
        Establish a connenction with neighbor to start exchanging book pages (file chunks).
        
        """

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((peer_ip, peer_port))
            print(f"Connected to {peer_ip} on port {peer_port}")