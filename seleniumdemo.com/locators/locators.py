from selenium.webdriver.common.by import By


class GenericLocators:
    body_tag = (By.TAG_NAME, "body")


class MyAccountMenuLocators:
    addresses_link = (By.LINK_TEXT, "Addresses")


class BillingAddressLocators:
    edit_billing_address_a = (By.XPATH, "//h3[text()='Billing address']/following-sibling::a")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    country_select = (By.ID, "billing_country")
    address_input = (By.ID, "billing_address_1")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    save_address_button = (By.XPATH, "//button[@value='Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")
    allert_address_ul = (By.XPATH, "//ul[@class='woocommerce-error']")


class ShippingAddressLocators:
    edit_shipping_address_a = (By.XPATH, "//h3[text()='Shipping address']/following-sibling::a")
    first_name_input = (By.ID, "shipping_first_name")
    last_name_input = (By.ID, "shipping_last_name")
    country_select = (By.ID, "shipping_country")
    address_input = (By.ID, "shipping_address_1")
    postcode_input = (By.ID, "shipping_postcode")
    city_input = (By.ID, "shipping_city")
    phone_input = (By.ID, "shipping_phone")
    save_address_button = (By.XPATH, "//button[@value='Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")
    allert_address_ul = (By.XPATH, "//ul[@class='woocommerce-error']")


class MyAccountPageLocators:
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    logout_link = (By.LINK_TEXT, "Logout")
