from p2p_node import P2PNode
from network_manager import NetworkManager
from file_chunker import FileChunker
import threading

if __name__ == "__main__":

    local_ip = "10.196.26.109"
    local_port = 5000

    node_id = f"node_{local_ip}:{local_port}"
    node = P2PNode(node_id, local_ip, local_port)
    network = NetworkManager(local_ip, local_port)


    server_thread = threading.Thread(target=network.start_server, args=(node, network))
    server_thread.daemon = True
    server_thread.start()

    node.add_peer("10.196.72.11", 5001)

    chunker = FileChunker("book.txt")
    chunks = chunker.file_chunker()

    for chunk in chunks:
        for peer_ip, peer_port in node.peers:
            node.upload_file_chunk(peer_ip, peer_port, chunk)

    threading.Event().wait()

