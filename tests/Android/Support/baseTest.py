import time
import unittest
from tests.Android.Support.driverFactory import instance as driver_instance
from tests.Android.Support import APP_ID


class BaseTest(unittest.TestCase):
    """
    Base configuration for Appium tests.
    """
    driver = driver_instance()

    def maximize_app(self):
        self.driver.activate_app(APP_ID)

    def tearDown(self):
        """
        Closes current Appium driver connection.
        """
        print("Close Appium driver...")
        if self.driver is not None:
            self.driver.quit()
        print("Appium driver closed.")
        print("===================================== Script execution finished ===================================== ")
        time.sleep(5)
