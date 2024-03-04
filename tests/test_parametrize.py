"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(1024, 768), (1920, 1080)], indirect=True)
def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(480, 800), (375, 812)], indirect=True)
def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url('https://github.com/login'))
