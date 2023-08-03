import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class RequestDemoAvailability(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver and open the app's home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.tendable.com/")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        # Close the WebDriver after each test case
        self.driver.quit()

    def test_RequestDemo_on_HomePage(self):
        # Test case to check if Request a Demo link is available on Tendable Home Page
        request_demo_element = self.driver.find_element(By.XPATH, "//div[@class='button-links-panel']//a["
                                                                  "@class='button'][normalize-space()='Request a "
                                                                  "demo']")
        self.assertTrue(request_demo_element.is_displayed(), "Request Demo link is visible")
        print("Request Demo link is visible on Home Page")

    def test_RequestDemo_on_OurStory_Page(self):
        # Test case to check if Request a Demo link is available on Tendable Our Story Page
        our_story = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Story']")
        our_story.click()
        request_demo_element = self.driver.find_element(By.XPATH, "//div[@class='button-links-panel']//a["
                                                                  "@class='button'][normalize-space()='Request a "
                                                                  "demo']")
        self.assertTrue(request_demo_element.is_displayed(), "Request Demo link is visible")
        print("Request Demo link is visible on Our Story Page")

    def test_RequestDemo_on_OurSolution_Page(self):
        # Test case to check if Request a Demo link is available on Tendable Our Solution Page
        our_solution = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Solution']")
        our_solution.click()
        request_demo_element = self.driver.find_element(By.XPATH, "//div[@class='button-links-panel']//a["
                                                                  "@class='button'][normalize-space()='Request a "
                                                                  "demo']")
        self.assertTrue(request_demo_element.is_displayed(), "Request Demo link is visible")
        print("Request Demo link is visible on Our Solution Page")

    def test_RequestDemo_on_Why_Tendable_Page(self):
        # Test case to check if Request a Demo link is available on Tendable Our Solution Page
        why_tendable = self.driver.find_element(By.XPATH, "//a[normalize-space()='Why Tendable?']")
        why_tendable.click()
        request_demo_element = self.driver.find_element(By.XPATH, "//div[@class='button-links-panel']//a["
                                                                  "@class='button'][normalize-space()='Request a "
                                                                  "demo']")
        self.assertTrue(request_demo_element.is_displayed(), "Request Demo link is visible")
        print("Request Demo link is visible on Why Tendable Page")







