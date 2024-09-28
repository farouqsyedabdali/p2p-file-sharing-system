#this file makes sure there is a reliable communication between the nodes

class NetworkManager:

    """ 
    ip: address (ip address) of the neighbor
    port: mailbox of the neighbor
    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    
        