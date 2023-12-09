from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input_xpath = "//input[@placeholder='Username']"
        self.password_input_xpath = "//input[@placeholder='Password']"
        self.login_button_xpath = "//button[normalize-space()='Login']"

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_input_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)

    def click_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


