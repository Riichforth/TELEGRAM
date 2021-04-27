import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
from tests.Android.Support.baseScreen import BaseScreen
from tests.Android.Support.baseTest import BaseTest


class HomeScreen(BaseTest, BaseScreen):

    def __str__(self):
        return "Home screen"

    screen_title = "Telegram"
    test_message = "Test message for telegram"
    telegram_logo = (By.XPATH, "//android.widget.TextView[@text='Telegram']")
    sended_message = (By.XPATH, "//*[contains(@content-desc,'Test message for telegram')]")
    message_field = (By.XPATH, "//android.widget.EditText")
    send_btn = (By.XPATH, "//android.view.View[@content-desc='Send']")
    delete_btn = (By.XPATH, "//android.widget.TextView[@text='Delete'] | //android.widget.TextView[@text='DELETE']")
    last_message = (By.XPATH, "(//android.view.ViewGroup[@content-desc])[last()]")

    def wait_for_load(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.telegram_logo),
                                             message="Logo isn't displayed!")

    def click_on_dialogue(self, dialogue):
        print("Clicking on {} dialogue".format(dialogue))
        dialogue = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{}]".format(dialogue))
        self.find_element(dialogue).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.message_field))

    def tap_on_message_field(self):
        print("Tap message field on {}".format(self))
        self.find_element(self.message_field).click()

    def tap_on_send_button(self):
        print("Tap message field on {}".format(self))
        self.find_element(self.send_btn).click()

    def fill_out_message_field(self, message):
        print("Fill out message field on {}".format(self))
        self.find_element(self.message_field).send_keys(message)

    def validate_sended_message(self):
        print("Validate sended message on {}".format(self))
        if self.find_element(self.last_message).get_attribute("content-desc").split("Sent")[0].strip() != self.test_message:
            warnings.warn(message="Sended message is different from displayed message")

    def delete_sended_message(self):
        print("Delete sended message on {}".format(self))
        self.find_element(self.last_message).click()
        self.find_element(self.delete_btn).click()
        time.sleep(2)
        self.find_element(self.delete_btn).click()
