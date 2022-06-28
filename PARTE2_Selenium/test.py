#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class TestClass:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.cheesecake.com/")
        yield
        self.driver.close()
        self.driver.quit()
        print("\n-----TEST DONE-----")

    @pytest.mark.skipif(False, reason="Test skipped by user")
    def test1(self):
        driver = self.driver
        driver.find_element(By.ID, "ctl00_Header1_ctl00_KeywordField").send_keys("strawberry")
        driver.find_element(By.ID, "ctl00_Header1_ctl00_btnSearch").click()
        product_list = driver.find_element(By.CSS_SELECTOR, ".productgrid.table").find_elements(By.CLASS_NAME, "SingleProductDisplayPanel")
        assert len(product_list) == 9

        price4_element = product_list[3].find_element(By.ID, "ctl00_MainContentHolder_ProductGridDisplay_rpProductGrid_ctl04_SingleProductDisplay_PriceLabel").text
        assert price4_element == "$44.99"
