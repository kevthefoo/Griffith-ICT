import time, subprocess, config, json, re
from selenium.webdriver.common.by import By
from selenium import webdriver

# Load the environment variables from the .env file (For local enviroment)
from dotenv import load_dotenv
load_dotenv()


chrome_path = config.chrome_browser_path
user_profile_path = config.user_profile_path

# Launch Chrome in debug mode
subprocess.Popen([chrome_path, '--remote-debugging-port=9222', f'--user-data-dir={user_profile_path}'])

# --------------------------------------Initialize Selenium--------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# --------------------------------------Go To The Target URL--------------------------------------

inspect_url = "https://lms.griffith.edu.au/courses/24045/assignments/94932"
if driver.current_url == inspect_url:
    pass
else:
    driver.get(inspect_url)

driver.maximize_window()
time.sleep(5)

# --------------------------------------Start Scraping--------------------------------------
with open('./z.json', 'r') as f:
    data = json.load(f)
    print(f"There are {len(data)} questions in the bank!\n")

try:
    ifame = driver.find_element(By.CLASS_NAME, "tool_launch")
except:
    pass
else:
    driver.switch_to.frame(ifame)

question_objects = driver.find_elements(By.CLASS_NAME, "css-gphj19")
print(f"{len(question_objects)} questions are founded!\n")

new_question = 0
for _ in question_objects:
    question = _.find_element(By.CLASS_NAME, "user_content")
    blank_content = question.find_element(By.TAG_NAME, "span").text
    question_content = question.text.replace(
        blank_content, '_____').replace('\n', ' ')

    correct_answer = blank_content.split(':')[-1]
    correct_answer = re.sub(r'\s+', ' ', correct_answer).strip().replace('\n', ' ')

    if question_content not in data:
        data[question_content] = {
            "question": question_content,
            "answer": correct_answer
        }
        new_question += 1

if new_question > 0:
    with open('./z.json', 'w') as f:
        json.dump(data, f)
    print(f"{new_question} new questions are founded!\n")
else:
    print(f"No new question is founded!\n")
