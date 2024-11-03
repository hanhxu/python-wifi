# To conduct Wi-Fi testing using Python, you can use various 
# libraries and tools depending on what type of testing you 
# want to perform, such as signal strength, connection speed, 
# ping tests, and so on.
# 1. Checking Wi-Fi Signal Strength
# To check the signal strength of nearby networks or the connected 
# network, you can use the subprocess module to run system 
# commands like nmcli (Linux) or netsh (Windows) and parse the 
# results.
# 2. Wi-Fi Speed Test
# To check internet speed (both download and upload), you can use the 
# speedtest-cli package. This can test the actual speed of your Wi-Fi 
# connection by connecting to a speed test server.
# 3. Ping Test
# To test the latency and stability of your Wi-Fi network, you can 
# perform a ping test. This involves sending ICMP echo requests to a 
# server and measuring how long it takes to get a response.
# 4. Combining Different Wi-Fi Tests
# You can combine all these tests into a single script to get a comprehensive 
# overview of your Wi-Fi performance (signal strength, speed, and latency)

############################################################################################
# imports the speedtest library, which allows you to measure internet bandwidth            #
# (upload and download speeds) by connecting to various servers.                           #
# The subprocess module is used to run system commands from within Python. This            #
# can be useful for executing shell commands and capturing their output.                   #
# imports specific functions (ping and verbose_ping) from the ping3 library. These         #
# functions allow you to ping a server to check its availability and measure response time.#
############################################################################################

import speedtest
import subprocess
from ping3 import ping, verbose_ping

def get_wifi_signal_strength():
    #stdout=subprocess.PIPE, this tells Python to capture the output of the command
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE)
    #this method converts the byte output into a string format using UTF-8 encodingd
    output = result.stdout.decode('utf-8')
    
    if result.returncode != 0:
        print("Error executing command.")
    else:
        print(output)
        
    for line in output.split('\n'):
        if 'signal' in line.lower():  #convert line to lowercase for comparison
            signal_strength = line.split(':')[1].strip()
            return signal_strength
    return None                                       # If signal is not found

wifi_signal = get_wifi_signal_strength()
if wifi_signal is not None:
    print(f'WiFi Signal Strength: {wifi_signal}')
else:
    print("Signal strength not found.")
    
def test_signal_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000 #convert to Mbps
    upload_speed = st.upload() / 1_000_000 #convert to Mbps
    ping = st.results.ping
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    ping(f"Ping: {ping} ms")
test_signal_speed()
    