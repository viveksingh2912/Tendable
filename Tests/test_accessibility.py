import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TendableHomePageAccessibilityTest(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver and open the app's home page
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.tendable.com/")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        # Close the WebDriver after each test case
        self.driver.quit()

    def test_logo_visibility(self):
        # Test case to check if the Home Page Logo "Tendable" is visible
        logo_element = self.driver.find_element(By.CSS_SELECTOR, ".logo")
        self.assertTrue(logo_element.is_displayed(), "Logo element is visible")
        print("Tendable logo is visible")

    def test_logo_clickable(self):
        # Test case to check if the Home Page Logo "Tendable" is clickable
        logo_element = self.driver.find_element(By.CSS_SELECTOR, ".logo")
        logo_element.click()
        print("Tendable logo is Clickable")

    def test_OurStory_visibility(self):
        # Test case to check if the "Our Story" link is visible
        our_story = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Story']")
        self.assertTrue(our_story.is_displayed(), "Our Story link is visible")
        print("Our Story link is visible")

    def test_OurStory_clickable(self):
        # Test case to check if the "Our Story" link is Clickable
        our_story = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Story']")
        our_story.click()
        print("Our Story link is Clickable")

    def test_OurSolution_visibility(self):
        # Test case to check if the "Our Solution" link is visible
        our_solution = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Solution']")
        self.assertTrue(our_solution.is_displayed(), "Our Solution link is visible.")
        print("OurSolution link is visible")

    def test_OurSolution_clickable(self):
        # Test case to check if the "Our Story" link is Clickable
        our_solution = self.driver.find_element(By.XPATH, "//a[normalize-space()='Our Solution']")
        our_solution.click()
        print("OurSolution link is Clickable")

    def test_WhyTendable_visibility(self):
        # Test case to check if the "Why Tendable" link is visible
        why_tendable = self.driver.find_element(By.XPATH, "//a[normalize-space()='Why Tendable?']")
        self.assertTrue(why_tendable.is_displayed(), "why tendable link is visible.")
        print("Why Tendable link is visible")

    def test_WhyTendable_clickable(self):
        # Test case to check if the "Our Story" link is Clickable
        why_tendable = self.driver.find_element(By.XPATH, "//a[normalize-space()='Why Tendable?']")
        why_tendable.click()
        print("Why Tendable link is Clickable")


if __name__ == "__main__":
    unittest.main()
