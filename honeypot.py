import socket
import logging
import pyfiglet

# Display a banner
print(pyfiglet.figlet_format("BuzzPot"))

# Configure logging
logging.basicConfig(filename="honeypot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Define the Honeypot server
def start_honeypot(host="127.0.0.1", port=8080):
    honeypot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    honeypot_socket.bind((host, port))
    honeypot_socket.listen(5)

    print(f"🐝 Honeypot running on {host}:{port}...")

    while True:
        client_socket, client_address = honeypot_socket.accept()
        logging.info(f"🔴 Intrusion detected from IP: {client_address[0]}")

        # Fake response to trick attackers
        client_socket.send(b"Access Denied! Logged.\n")
        client_socket.close()

# Run the honeypot
if __name__ == "__main__":
    start_honeypot()
