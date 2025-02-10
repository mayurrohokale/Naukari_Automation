from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os
import openai


load_dotenv()

USERNAME = os.getenv("user_name")
PASSWORD = os.getenv("password")

# Define Conditions
preferred_locations = ['Remote', 'Pune']
preferred_skills = ['React', 'Angular', 'frontend', 'css', 'CSS', 'HTML', 'Javascript', 'TypeScript', 'React.js', 
                    'TailwindCSS', 'Bootstrap', 'Java', 'C++', 'Node.js', 'Backend', 'Full Stack Developer', 
                    'Developer', 'Front end', 'MySQL', 'MongoDB', 'Database', 'Java Developer', 'Frontend', 
                    'SQL', 'Software Developer', 'API']
preferred_experience = ['fresher', '0-1 years', '0-2 years', '0-3 years']

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
driver.implicitly_wait(5)  # Wait for elements to load

driver.find_element(By.ID, "usernameField").send_keys(USERNAME)
time.sleep(3)
driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)

# Click Login Button with Explicit Wait
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))).click()
time.sleep(5)  # Allow login process

# Define tabs to iterate
tabs = {
    "Profile": "profile",
    "Applies": "apply",
    "Preferences": "preference",
    "Similar Jobs": "similar_jobs"
}

driver.find_element(By.CLASS_NAME, "nI-gNb-menuItems__anchorDropdown").click()
print("✅ Successfully clicked on the Jobs tab!")

for tab_name, tab_id in tabs.items():
    try:
        driver.find_element(By.ID, tab_id).click()
        print(f"✅ Clicked on {tab_name} Tab")
        time.sleep(2)

        job_list_containers = driver.find_elements(By.CLASS_NAME, "list")

        for job_list in job_list_containers:
            job_listings = job_list.find_elements(By.TAG_NAME, "article")
            time.sleep(2)
            for job in job_listings:
                try:
                    job_title = job.find_element(By.CSS_SELECTOR, "p.title").text.strip()
                    location_element = job.find_element(By.CSS_SELECTOR, "li.placeHolderLi.location span")
                    location = location_element.text.strip()
                    skills_elements = job.find_elements(By.CSS_SELECTOR, "ul.tags li")
                    skills = [skill.text.strip() for skill in skills_elements]

                    if location in preferred_locations and any(skill in preferred_skills for skill in skills):
                        print(f"✅ Applying for job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")

                        # Click job title to open details
                        job.find_element(By.CSS_SELECTOR, "p.title").click()
                        time.sleep(4)

                        # Switch to new tab
                        driver.switch_to.window(driver.window_handles[-1])

                        time.sleep(2)

                        # Click "Apply Now" button if available
                        try:
                            apply_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Apply') or contains(text(), 'I am interested')]")
                            apply_button.click()
                            time.sleep(2)
                            driver.switch_to.window(driver.window_handles[-1])
                            response = driver.find_element(By.ID, "apply-message")
                            if response:
                                print(f"✅ Successfully applied for job: {job_title} | Location: {location}")
                            else:
                                # return uRL
                                print("Failed!!!!!")
                            time.sleep(2)
                            print("🟢 Applied successfully!")
                        except Exception:
                            print("⚠️ Apply button not found or already applied.")

                        # Close job tab and return to main tab
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

                    else:
                        print(f"❌ Skipping job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")

                except Exception as e:
                    print(f"❌ Error processing job: {e}")

    except Exception as e:
        print(f"⚠️ Could not open {tab_name} Tab: {e}")

print("------------------- Execution Completed Successfully ------------")

input("Press Enter to close the browser...")
driver.quit()  # Closes the browser when Enter is pressed
