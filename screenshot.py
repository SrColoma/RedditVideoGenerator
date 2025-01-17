import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Config
# screenshotDir = "Screenshots"
screenWidth = 400
screenHeight = 800

def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver, wait = __setupDriver(script.url)
    script.titleSCFile = __takeScreenshot(filePrefix, driver, wait,f"post-title-t3_{script.id}",script.id,type="post")
    # script.titleSCFile = __takeScreenshot(filePrefix, driver, wait)
    for commentFrame in script.frames:
        # commentFrame.screenShotFile = __takeScreenshot(filePrefix, driver, wait,f"t1_{commentFrame.commentId}",type="comment")
        commentFrame.screenShotFile = __takeScreenshot(filePrefix, driver, wait,f'//*[@thingid="t1_{commentFrame.commentId}"]',commentFrame.commentId,type="comment")
    driver.quit()

def __takeScreenshot(filePrefix, driver, wait, handle,id,type=""):
    method = By.XPATH if (type == "comment") else By.ID
    # method = By.CLASS_NAME if (handle == "Post") else By.ID
    # method = By.ID thingid
    search = wait.until(EC.presence_of_element_located((method, handle)))
    driver.execute_script("window.focus();")


    config = configparser.ConfigParser()
    config.read('config.ini')
    screenshotDir = config["General"]["TemporalDir"]
    fileName = f"{screenshotDir}\\{filePrefix}-{id}.png"
    fp = open(fileName, "wb")
    fp.write(search.screenshot_as_png)
    fp.close()
    return fileName

def __setupDriver(url: str):
    options = webdriver.ChromeOptions()
    options.headless = False
    options.enable_mobile = False
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    driver.set_window_size(width=screenWidth, height=screenHeight)
    driver.get(url)

    return driver, wait