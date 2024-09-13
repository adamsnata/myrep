import time

import pytest
import allure
from allure_commons.types import Severity
from lamoda_tests.web.search_filter_and_cart import \
    SearchByFilterAndAddCart

search_page = SearchByFilterAndAddCart()

@allure.parent_suite('Web')
@allure.label('owner', 'ischenkoalex')
@allure.tag('Lamoda')
@allure.title('Search with filter and add Cart')
@allure.severity(Severity.MINOR)
def test_search_with_filter_and_cart():
    search_page.open()
    time.sleep(5)
    search_page.search_and_input_searchbar('Nike Air Max')
    time.sleep(5)
    search_page.add_filter("WMNS AIR MAX 270")
    time.sleep(5)
    search_page.choose_product()
    time.sleep(5)
    search_page.close_pop_up()
    time.sleep(5)
    search_page.choose_size('6 US')
    time.sleep(5)
    search_page.add_to_cart()
    time.sleep(5)
    search_page.should_product()

