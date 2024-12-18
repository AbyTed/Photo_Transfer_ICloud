from selenium import webdriver, By 

from .constants import ICLOUDWEBSITE

class Bot():
    
    def __init__(self, webdriver, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        
    
    def login_into_apple(self) -> None:
        
        
        self.driver.get(ICLOUDWEBSITE)
        
        text_box = self.driver.find_element(by=By.ID, value="account_name_text_field")
        text_box.send_keys(self.username)

