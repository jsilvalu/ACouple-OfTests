#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestClass:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.cheesecake.com/")
        yield
        self.driver.close()
        self.driver.quit()
        print("\n-----TEST DONE-----")

    @pytest.mark.parametrize("subtype", get_json_subtypes_list("car_accident_3_party"))
    @pytest.mark.skipif(True, reason="Test skipped by user")
    def test_car_accident_3_party(self, subtype):
        driver = self.driver
        driver.find
