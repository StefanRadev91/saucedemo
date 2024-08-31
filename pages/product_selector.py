from playwright.sync_api import Page 

class ProductSelectorPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_one = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.item_two = page.locator("#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)")
        self.shopping_card = page.locator("#shopping_cart_container > a")
        self.checkout_button = page.locator("#checkout")

    def productSelectorFlow(self):
        self.item_one.click()
        self.item_two.click()
        self.shopping_card.click()
        self.checkout_button.click()

    def successful_navigate_to_checkout(self):
        return self.page.locator("#header_container > div.header_secondary_container > span")

        
