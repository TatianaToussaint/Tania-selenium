def pytest_addoption(parser):
    parser.addoption("--browser", default = "chrome")
    parser.addoption("--OS", default = "Windows 10")