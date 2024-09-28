from p2p_node import P2PNode
from network_manager import NetworkManager
from file_chunker import FileChunker
import threading

if __name__ == "__main__":

    ip = "127.0.0.1"


    # Node 1 Variables
    node1_id = "node1"
    port1 = 5000

    # Node 2 Variables
    node2_id = "node2"
    port2 = 5001
    
    #Node3 Variables
    node3_id = "node3"
    port3 = 5002

    #Node4 Variables
    node4_id = "node4"
    port4 = 5003
    

    # Node 1 Network Setup
    node1 = P2PNode(node1_id, ip, port1)
    network1 = NetworkManager(ip, port1)

    # Node 2 Network Setup
    node2 = P2PNode(node2_id, ip, port2)
    network2 = NetworkManager(ip, port2)

    #Node 3 Network Setup
    node3 = P2PNode(node3_id, ip, port3)
    network3 = NetworkManager(ip, port3)

    #Node 4 Network Setup
    node4 = P2PNode(node4_id, ip, port4)
    network4 = NetworkManager(ip, port4)



    server_thread = threading.Thread(target=network1.start_server, args=(node1, network1))
    server_thread.daemon = True
    server_thread.start()

    node1.add_peer("127.0.0.1", 5001)

    chunker = FileChunker("book.txt")
    chunks = chunker.file_chunker()

    for chunk in chunks:
        for peer_ip, peer_port in node1.peers:
            node1.upload_file_chunk(peer_ip, peer_port, chunk)

    server_thread.join()

