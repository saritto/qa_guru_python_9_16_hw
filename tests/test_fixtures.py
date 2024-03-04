"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


@pytest.mark.mobile
def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))
