from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def is_login_successful(self):
        return self.page.locator("#header_container > div.primary_header > div.header_label > div").is_visible()
    
    def is_login_unsuccessful(self):
        return self.page.locator("#login_button_container > div > form > div.error-message-container.error > h3")