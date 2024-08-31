import pytest
from pages.login_page import LoginPage
from pages.product_selector import ProductSelectorPage

@pytest.mark.parametrize("username, password, should_succeed", [("standard_user", "secret_sauce", True), ("standard_user2", "secret_sauce", False)])
def test_successful_login(page, username, password, should_succeed):
    login_page = LoginPage(page)
    product_selector_page = ProductSelectorPage(page)

    login_page.navigate()

    login_page.login(username=username, password=password)
    if should_succeed:
        assert login_page.is_login_successful(), "Login was not successful"

        product_selector_page.productSelectorFlow()
        
        assert product_selector_page.successful_navigate_to_checkout().is_visible(), "Failed to navigate to checkout"
    else:
        assert not login_page.is_login_successful(), "Login should have failed, but it was successful"