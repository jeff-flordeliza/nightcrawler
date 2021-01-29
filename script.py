from selenium import webdriver
import time
import datetime
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of youtube video ids
videos = ['<your youtube video ids>']

# Shuffle videos list
random.shuffle(videos)

# How many times the video on the list will be played?
play = 10

# Loop how many times the shuffled videos list.
for _ in range(play):
    # process all the video on the list.
    for video in videos:
        # load browser driver.
        # note: you may use mozilla or any webdriver in this example we used chrome driver.
        driver = webdriver.Chrome("<path to chrome driver>")

        # go to selected video
        driver.get("https://www.youtube.com/watch?v=" + video)

        # Switch to youtube video iframe section
        driver.switch_to.frame(0)

        # Random from 3 - 6 secs on when the play button will execute (optional)
        wait_to_play = random.randint(3, 6)
        time.sleep(wait_to_play)

        # Wait the play button to display
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")))
        # Click the play button
        element.click()

        # Switch to main frame.
        driver.switch_to.parent_frame()

        # Obtain the length of the video
        eDuration = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='ytp-time-duration']")))
        duration = eDuration.text

        # Obtain the length of the video in seconds
        x = time.strptime(duration, '%M:%S')
        x1 = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

        # Display the video duration
        print('video duration: ' + str(x1))

        # Close the browser when the video ends.
        time.sleep(int(x1))
        driver.close()




