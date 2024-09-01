import pytest
from pages.login_page import LoginPage
from pages.product_selector import ProductSelectorPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_successful_product_checkout(page, username, password):
    login_page = LoginPage(page) 
    product_selector_page = ProductSelectorPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()

    login_page.login(username=username, password=password)
    
    assert login_page.is_login_successful(), "Login was not successful"

    product_selector_page.productSelectorFlow()

    badge_number = product_selector_page.get_badge_number()
    assert badge_number == '2', f"Expected badge number to be 2, but got {badge_number}"
    print(badge_number)

    assert product_selector_page.successful_navigate_to_checkout().is_visible(), "Failed to navigate to checkout"

    checkout_page.checkoutpage_flow("Stefan", "Radev", "1309")
    
    assert checkout_page.istheorderfinished, "Error"

    
