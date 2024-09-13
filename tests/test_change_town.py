import time

import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.change_town import ChangeTown

change_town = ChangeTown()
@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Change Town')
@allure.severity(Severity.MINOR)
def test_change_town():

    change_town.open()
    time.sleep(5)
    change_town.click_geo()
    time.sleep(5)
    # change_town.close_pop_up()
    change_town.choose_town('Казань')
    time.sleep(5)
    change_town.choose_button()
    time.sleep(5)
    change_town.should_town('Казань')
