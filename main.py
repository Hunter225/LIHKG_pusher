from selenium import webdriver
import json
import time
import random

with open("config/config.config") as config_file:
    config = json.load(config_file)

EMAIL = config['email']
PASSWORD = config['password']
CHROME_DRIVER = config['chrome_driver_path']
PHANTOM_DRIVER = config['phantom_driver_path']

threads = []
with open("threads.txt", "r") as threads_file:
    threads = threads_file.read().split("\n")

replies = []
with open("reply.txt", "r") as replies_file:
    replies = replies_file.read().split("\n")

def reply_a_post(account, password, thread_id, reply_text, driver = "chrome"):
    url = "https://lihkg.com/thread/" + thread_id + "/page/1"
    if driver == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("--window-size=1280,800")
        browser = webdriver.Chrome(executable_path=CHROME_DRIVER, chrome_options=options)
    browser.get(url)
    browser.find_element_by_css_selector(".i-plus").click()
    browser.find_element_by_name("email").send_keys(account)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_css_selector(".\_2c5AwJ_0ePFIYub8OFE97J > a:nth-child(2)").click()
    time.sleep(1)
    browser.find_element_by_css_selector(".i-reply:nth-child(1)").click()
    browser.find_element_by_css_selector(".ProseMirror").send_keys(reply_text)
    time.sleep(1)
    browser.find_element_by_css_selector(".\_2BgwSCCa9NCxtCSt5-52rl > a:nth-child(2)").click()
    time.sleep(1)
    browser.quit()
    return 0

def random_select_reply(reply_list):
    reply = random.choice(reply_list)
    return reply

def main():
    while True:
        for id in threads:
            reply = random_select_reply(replies)
            reply_a_post(EMAIL, PASSWORD, id, reply)
            print("pushing thread " + id + " successfully")
            print("reply: " + reply)
            time.sleep(3)


if __name__ == "__main__":
    main()
