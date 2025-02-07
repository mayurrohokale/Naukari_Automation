from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("user_name")
PASSWORD = os.getenv("password")

# Define Conditions
preferred_locations = ['Remote', 'Pune']
preferred_skills = ['React', 'Angular', 'frontend', 'css','CSS', 'HTML', 'Javascript', 'TypeScript', 'React.js', 'TailwindCSS', 'Bootstrap', 'Java', 'C++', 'Node.js', 'Backend','Full Stack Developer', 'Developer', 'Front end', 'MySQL', 'MongoDB', 'Database'
                    ,'Java Developer', 'Frontend','SQL', 'software Developer','API']
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

# Navigate to Jobs Tab
driver.find_element(By.CLASS_NAME, "nI-gNb-menuItems__anchorDropdown").click()
print("✅ Successfully clicked on the Jobs tab!")

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
                    print("🟢 Applied successfully!")
                except Exception as e:
                    print("⚠️ Apply button not found or already applied.")
                    print("Something Went Wrong!", e)
                # Close job tab and return to main tab
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            else:
                print(f"❌ Skipping job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")
        
        except Exception as e:
            print(f"❌ Error processing job: {e}")


time.sleep(2)
driver.find_element(By.ID, "apply").click()
print("✅ Clicked on Aplies Tab")
time.sleep(2)

Applies = driver.find_elements(By.CLASS_NAME, "list")

for job_list in Applies:
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
                    print("🟢 Applied successfully!")
                except Exception as e:
                    print("⚠️ Apply button not found or already applied.")
                    print("Something Went Wrong!", e)
                # Close job tab and return to main tab
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            else:
                print(f"❌ Skipping job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")
        
        except Exception as e:
            print(f"❌ Error processing job: {e}")

time.sleep(2)
time.sleep(2)
driver.find_element(By.ID, "preference").click()
print("✅ Clicked on Preferences Tab")
time.sleep(2)

# Find job listings
Preferences = driver.find_elements(By.CLASS_NAME, 'list')  # Use find_elements to get a list of elements

if not Preferences:
    print("⚠️ No job listings found!")
else:
    for job_list in Preferences:
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
                        print("🟢 Applied successfully!")
                    except Exception as e:
                        print("⚠️ Apply button not found or already applied.")
                        print("Something Went Wrong!", e)
                    # Close job tab and return to main tab
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                else:
                    print(f"❌ Skipping job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")
            
            except Exception as e:
                print(f"❌ Error processing job: {e}")



time.sleep(2)
driver.find_element(By.ID, "similar_jobs").click()
print("✅ Clicked on You Might Like Tab")
time.sleep(2)

Similar_Jobs = driver.find_elements(By.CLASS_NAME, 'list')

if not Similar_Jobs:
    print("⚠️ No job listings found!")
else:
    for job_list in Similar_Jobs:
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
                        print("🟢 Applied successfully!")
                    except Exception as e:
                        print("⚠️ Apply button not found or already applied.")
                        print("Something Went Wrong!", e)
                    # Close job tab and return to main tab
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                else:
                    print(f"❌ Skipping job: {job_title} | Location: {location} | Skills: {', '.join(skills)}")
            
            except Exception as e:
                print(f"❌ Error processing job: {e}")



print("-------------------Execution Completed successfully------------")


input("Press Enter to close the browser...")
driver.quit()  # Closes the browser when Enter is pressed


# Close browser

# driver.quit()
