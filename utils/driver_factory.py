from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(config):
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
        elif config["browser"] == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = webdriver.Edge(options=options)

        return driver
