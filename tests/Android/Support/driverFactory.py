import json
from copy import deepcopy
from selenium import webdriver
from appium import webdriver
from appium.webdriver.webdriver import Command, RemoteCommand

DRIVER_IMPLICIT_WAIT_TIMEOUT = 20 # 10
DRIVER_EXPLICIT_WAIT_TIMEOUT = 30 # 15
DRIVER_SHORT_WAIT_TIMEOUT = 6 # 2
DRIVER_MIDDLE_WAIT_TIMEOUT = 12 # 6


try:
    config = json.load(open('{}/config.json'.format('/'.join(__file__.replace('\\', '/').split('/')[:-4]))))
except FileNotFoundError:
    config = None


class AWSDriver(webdriver.Remote):
    def execute(self, driver_command, params=None):
        if driver_command in (Command.GET_ALL_SESSIONS, RemoteCommand.NEW_SESSION):
            return webdriver.Remote.execute(self, driver_command, params)
        if not self.all_sessions:
            caps = self.capabilities
            caps['autoLaunch'] = False
            webdriver.Remote.start_session(self, caps)
        return super().execute(driver_command, params)


def get_capabilities():
    try:
        desired_caps = deepcopy(config['capabilities'])
    except TypeError:
        desired_caps = {
            "automationName": "UiAutomator2",
            "newCommandTimeout": 300,
            "noReset": False,
            "autoAcceptAlerts": True,
            "unicodeKeyboard": True
        }
    return desired_caps


def instance():
    """
    :return: An instance of Appium driver with default capabilities.
    """

    desired_caps = get_capabilities()
    driver = AWSDriver('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver

