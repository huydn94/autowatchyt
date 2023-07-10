import os
import platform
import subprocess

def ping(host):
    """
    Perform a ping to the specified host and return True if successful, False otherwise.
    """
    # Determine the operating system
    command = ['ping', '-n', '1', '-w', '1000', host]


    # Execute the ping command
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

# Example usage
host = "8.8.8.8"
result = ping(host)

if result:
    print(f"Ping to {host} successful.")
else:
    print(f"Ping to {host} failed.")