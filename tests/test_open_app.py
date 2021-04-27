from tests.Android.Screens.homeScreen import HomeScreen
from tests.Android.Support.baseScreen import BaseScreen
from tests.Android.Support.baseTest import BaseTest


class TestOpenApplication(BaseTest, BaseScreen):

    def test_2404_send_message(self):
        home_screen = HomeScreen()
        home_screen.wait_for_load()

        home_screen.click_on_dialogue("1")
        home_screen.tap_on_message_field()

        home_screen.fill_out_message_field(home_screen.test_message)

        home_screen.tap_on_send_button()

        home_screen.validate_sended_message()
        home_screen.delete_sended_message()

        self.assertTrue(self.is_element_not_displayed(home_screen.sended_message))
