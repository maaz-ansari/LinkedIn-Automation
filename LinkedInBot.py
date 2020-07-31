import selenium.webdriver
import time
import streamlit as st


def main():
    st.header("LinkedIn Automation")
    eid=st.text_input("Enter Your Email-ID", "")
    pwd=st.text_input("Enter Your Password", "")
    if st.button("Get Connections"):
        baseDataUrl = "https://www.linkedin.com/login"
        
        chrome_options = selenium.webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = selenium.webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        #driver = selenium.webdriver.Chrome(r"C:\Users\Maaz\Downloads\chromedriver_win32\chromedriver.exe")
        driver.get(baseDataUrl) 
        time.sleep(3)
        ID = driver.find_element_by_id('username')
        ID.send_keys(eid)
        passw = driver.find_element_by_id('password')
        passw.send_keys(pwd)
        driver.find_element_by_xpath('//button[@class = "btn__primary--large from__button--floating"]').click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//button[@class = "primary-action-new"]').click()
        except:
            pass
        driver.find_element_by_id('mynetwork-tab-icon').click()
        time.sleep(5)
        driver.find_element_by_xpath('//header[@class = "msg-overlay-bubble-header"]').click() #minimize the chatbox
        #print(len(driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]'))-1)
        maxs=len(driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]'))-1
        for i in range(0,10):
            element = driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]')[i]
            desired_y = (element.size['height'] / 2) + element.location['y']
            window_h = driver.execute_script('return window.innerHeight')
            window_y = driver.execute_script('return window.pageYOffset')
            current_y = (window_h / 2) + window_y
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            element.click()
        driver.refresh()
        time.sleep(3)
        #print(len(driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]'))-1)
        maxs=len(driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]'))-1
        for i in range(0,10):
            element = driver.find_elements_by_xpath('//button[@data-control-name= "people_connect"]')[i]
            desired_y = (element.size['height'] / 2) + element.location['y']
            window_h = driver.execute_script('return window.innerHeight')
            window_y = driver.execute_script('return window.pageYOffset')
            current_y = (window_h / 2) + window_y
            scroll_y_by = desired_y - current_y
            driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
            element.click()
        st.success('Done! To get more connections, kindly re-run.')
    st.subheader('Developed by: Maaz Ansari')
if __name__=='__main__':
     main()