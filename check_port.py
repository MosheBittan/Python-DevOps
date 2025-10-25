import socket

def check_port(host, port,timeout=5):
    """Checks if a TCP port is open on a given host.

    Args:
        host (str): Hostname or IP address
        port (int): TCP port number.
        timeout (int, option): Connection timeout in seconds. Defaults to 5.

    Returns:
        bool: True if the port is open, False otherwise
    """

    try:
        with socket.create_connection((host,port), timeout):
            return True
    except Exception:
        return False
    
# Port 443 open , should return True    
print(check_port("www.google.com",443))

# Port 22 / 55 is not open, should return False
print(check_port("www.google.com",22))
print(check_port("www.google.com",55))

# Host does not exist, should return False
print(check_port("www.googleasdfasdfasfdasdf.com",22))
