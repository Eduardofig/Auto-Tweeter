import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#You can change your Chrome Webdriver here if your Chrome version is diferent than 85
PATH = ".\chromedriver.exe"
print("Welcome to Twitter Bot")
#You can change the variables here if you dont want to input them all the time
acc = int(input("Input the number of times you want to change the account/message >> "))
class TwitterUser:
    def __init__(self, login, senha, PATH):
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome(PATH)
    def entrar(self):
        try:
            self.driver.get("https://twitter.com")
            time.sleep(5)
            login = self.driver.find_element_by_name("session[username_or_email]")
            senha = self.driver.find_element_by_name("session[password]")
            login.send_keys(self.login)
            senha.send_keys(self.senha)
            senha.send_keys(Keys.RETURN)
            time.sleep(3)
            return
        except:
            self.driver.quit()
            time.sleep(3)
    def twittar(self,link,tweet,n_repeticoes):
                self.driver.get(link)
                time.sleep(10)
                for u in range(1,5):
                    self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    time.sleep(3)
                replys = self.driver.find_elements_by_css_selector('div[data-testid="reply"]')
                time.sleep(4)
                k = 1
                while k < n_repeticoes:
                    for elem in replys:
                        try:
                            elem.click()
                            time.sleep(7)
                            twite = self.driver.find_element_by_class_name('public-DraftEditor-content')
                            time.sleep(1)
                            twite.send_keys(tweet + ' num(' + str(k) + ')')
                            time.sleep(1)
                            self.driver.find_element_by_class_name('r-1fneopy').click()
                            time.sleep(4)
                            k +=1
                            print("tweet number " + str(k))
                        except:
                            time.sleep(3)
for t in range(0,acc):
    username = input("input twitter username >> ")
    password = input("input twitter password >> ")
    link = "https://twitter.com/" + input("input the target's username (without the @) >> ")
    message = input("input the message you in your replys >> ")
    n = int(input("input the number of times you want the bot to reply >> "))
    user1 = TwitterUser(username, password, PATH)
    user1.entrar()
    user1.twittar(link, message, n)


