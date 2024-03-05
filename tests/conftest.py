import pytest
from selene import browser


@pytest.fixture(params=[(1820, 1080), (1280, 720)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(480, 800), (300, 500)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (1280, 720), (480, 800), (300, 500)])
def is_desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > height:
        return True
    else:
        return False
