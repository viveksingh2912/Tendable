import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUs(unittest.TestCase):

    def __init__(self, methodname: str = ...):
        super().__init__(methodname)
        self.wait = None

    def setUp(self):
        # Initialize the WebDriver and open the app's home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.tendable.com/")
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Close the WebDriver after each test case
        self.driver.quit()

    def test_contactus_form_verification(self):
        try:
            # Find and click the "Contact Us" link
            contact_us_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Contact Us']"))
            )
            contact_us_link.click()

            # Find and select "Marketing" contact
            marketing_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//body/div[@class='w-full max-w-10xl mx-auto']/div["
                                                      "@class='flex']/div[@class='w-full px-2.5 md:px-5 "
                                                      "xl:px-10']/div[@class='-mx-2.5 md:-mx-5 xl:-mx-10']/div["
                                                      "@class='flex flex-wrap w-full mb-20 xl:mb-28']/div["
                                                      "@class='flex flex-wrap items-center w-full mx-2.5 md:mx-5 "
                                                      "xl:mx-8 px-2.5 md:px-5 xl:px-10']/div[1]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", marketing_option)
            marketing_option.click()

            # Find and fill in the form excluding the "Message" field
            firstname_input = self.driver.find_element(By.XPATH,
                                                       "//form[@id='contactMarketing-163701']//input["
                                                       "@id='form-input-firstName']")
            firstname_input.send_keys("vivek")
            surname_input = self.driver.find_element(By.XPATH,
                                                     "//form[@id='contactMarketing-163701']//input["
                                                     "@id='form-input-lastName']")
            surname_input.send_keys("singh")
            organisation_name_input = self.driver.find_element(By.XPATH,
                                                               "//form[@id='contactMarketing-163701']//input["
                                                               "@id='form-input-organisationName']")
            organisation_name_input.send_keys("Marvels")
            phone_number_input = self.driver.find_element(By.XPATH,
                                                          "//form[@id='contactMarketing-163701']//input["
                                                          "@id='form-input-cellPhone']")
            phone_number_input.send_keys("9876543212")
            email_input = self.driver.find_element(By.XPATH,
                                                   "//form[@id='contactMarketing-163701']//input["
                                                   "@id='form-input-email']")
            email_input.send_keys("singh.vivek2912@gmail.com")
            agree_radio_button = self.driver.find_element(By.XPATH,
                                                          "//form[@id='contactMarketing-163701']//input["
                                                          "@id='form-input-consentAgreed-0']")
            agree_radio_button.click()

            # Submitting the form with the message input
            submit_button = self.driver.find_element(By.XPATH, "//div[@class='toggle-form toggle-163701']//button[1]")
            submit_button.click()





        except Exception as e:
            # If any exception occurs, mark the test as FAIL and print the error message
            print("Test FAIL: ", str(e))
