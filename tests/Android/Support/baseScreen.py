import re

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Android.Support.driverFactory import DRIVER_EXPLICIT_WAIT_TIMEOUT, DRIVER_SHORT_WAIT_TIMEOUT, \
    DRIVER_IMPLICIT_WAIT_TIMEOUT, DRIVER_MIDDLE_WAIT_TIMEOUT


class BaseScreen(object):
    """
    Base functionality for each application screen.
    """
    def __init__(self, test):
        self.test = test
        self.driver = test.driver

    def is_element_displayed(self, locator, long_wait=False, custom_wait=None):
        """
        Checks whether an element is displayed on the screen.
        :param locator: Locator of the element (BY, rule)
        :param long_wait: Wait for element longer than usually
        :param custom_wait: Custom time to wait
        :return:
        """

        try:
            self.driver.implicitly_wait(0)
            if custom_wait is not None:
                return WebDriverWait(self.driver, custom_wait).until(EC.visibility_of_element_located(locator))
            elif long_wait:
                WebDriverWait(self.driver, long_wait).until(EC.visibility_of_element_located(locator))
            else:
                WebDriverWait(self.driver, DRIVER_SHORT_WAIT_TIMEOUT).until(EC.visibility_of_element_located(locator))
            result = True
        except TimeoutException:
            result = False

        self.driver.implicitly_wait(DRIVER_IMPLICIT_WAIT_TIMEOUT)
        return result

    def is_element_not_displayed(self, locator, long_wait=False, custom_wait=None):
        """
        Checks whether an element is displayed on the screen.
        :param locator: Locator of the element (BY, rule)
        :param long_wait: Wait for element longer than usually
        :param custom_wait: Custom time to wait
        :return:
        """

        try:
            self.driver.implicitly_wait(0)
            if custom_wait:
                WebDriverWait(self.driver, custom_wait).until(EC.invisibility_of_element_located(locator))
            elif long_wait:
                WebDriverWait(self.driver, long_wait).until(EC.invisibility_of_element_located(locator))
            else:
                WebDriverWait(self.driver, DRIVER_SHORT_WAIT_TIMEOUT).until(EC.invisibility_of_element_located(locator))
            result = True
        except TimeoutException:
            result = False

        self.driver.implicitly_wait(DRIVER_IMPLICIT_WAIT_TIMEOUT)
        return result

    def find_element(self, locator, long_wait=False, custom_wait=None):
        """
        Performs searching of an element by given locator.
        :param locator: Locator of the element (BY, rule)
        :param long_wait: Wait for element longer than usually
        :param custom_wait: Customizeable wait time. Use for extremely slow/fast operations

        :return: Found element on the screen.
        """
        if long_wait:
            return self.driver.find_element(locator[0], locator[1])
        elif custom_wait is not None:
            try:
                return WebDriverWait(self.driver, custom_wait).until(EC.presence_of_element_located(locator))
            except TimeoutException:
                raise NoSuchElementException('Element not found on {} by {} {}'.format(self, *locator))
        else:
            try:
                return WebDriverWait(self.driver, DRIVER_SHORT_WAIT_TIMEOUT).until(
                    EC.presence_of_element_located(locator))
            except TimeoutException:
                raise NoSuchElementException('Element not found on {} by {} {}'.format(self, *locator))
