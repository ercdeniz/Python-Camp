from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
import os


def clear():  # konsolu temizlemek için bir fonksiyon
    if os.name == 'nt':
        os.system('cls')


# testlerimi bir class içerisinde topladım
class testSwagLabs:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

# bu fonksiyon kullanıcı adı ve parolanın boş geçilip giriş butonuna basılması durumunu test eder
    def emptyUsernamePasword(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****emptyUsernamePasword*****")
        btnLogin = self.driver.find_element(By.ID, "login-button")
        sleep(1)
        btnLogin.click()
        print("login button clicked")
        errMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errMessage.text == "Epic sadface: Username is required"
        print(f"test: {testResult}")
        sleep(3)

# bu fonksiyon parolanın boş geçilip giriş butonuna basılması durumunu test eder
    def emptyPasword(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****emptyPasword*****")
        inputUsername = self.driver.find_element(By.ID, "user-name")
        inputUsername.send_keys("user")
        print("username entered")
        sleep(1)
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()
        print("login button clicked")
        sleep(1)
        errMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errMessage.text == "Epic sadface: Password is required"
        print(f"test: {testResult}")
        sleep(3)

# bu fonksiyon kilitli kullanıcı ismi ve parolası yazılıp giriş butonuna basılması durumunu test eder
    def lockedUser(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****lockedUser*****")
        inputUsername = self.driver.find_element(By.ID, "user-name")
        inputUsername.send_keys("locked_out_user")
        print("username entered")
        sleep(1)
        inputPassword = self.driver.find_element(By.ID, "password")
        inputPassword.send_keys("secret_sauce")
        print("password entered")
        sleep(1)
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()
        print("login button clicked")
        sleep(1)
        errMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"test: {testResult}")
        sleep(3)

    def iconX(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****iconX*****")
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()
        print("login button clicked")
        sleep(1)
        # burada x ikonlarını bulup kaç tane olduğnu buldum
        icons = self.driver.find_elements(By.CLASS_NAME, "error_icon")
        numOfIcon = len(icons)
        # şimdilik false olan bir testResult oluşturdum
        testResult = False
        sleep(2)

        # iki adet x ikonu varsa true yoksa false dönecek
        if (numOfIcon == 2):
            testResult = True
            print(f"x icons are appear, test: {testResult}")
        else:
            print(f"x icons are not found, test: {testResult}")

        sleep(2)
        icons.clear()  # bundan sonraki kısımda x ikonlarının sayısı 0 olmalı ondan dolayı clear ile temizledik
        # tekrar aynı işlemi yapma sebebim numOfIcone değişkeninin de sıfırlanmasıydı
        numOfIcon = len(icons)
        testResult = False
        # else içerisinde tekrar false atamamak için burada false atadım yanı result sonucum default olarak false olacak
        errMessageClose = self.driver.find_element(
            By.CLASS_NAME, "error-button")
        errMessageClose.click()
        print("error button clicked")
        sleep(2)
        # eğer hiç x iconu yoksa true yoksa false dönecek
        if (numOfIcon == 0):
            testResult = True
            print(f"x icons are not found, test: {testResult}")
        else:
            print(f"x icons are appear, test: {testResult}")
        sleep(3)

    def standardUser(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****standardUser*****")
        inputUsername = self.driver.find_element(By.ID, "user-name")
        inputUsername.send_keys("standard_user")
        print("username entered")
        sleep(1)
        inputPassword = self.driver.find_element(By.ID, "password")
        inputPassword.send_keys("secret_sauce")
        print("password entered")
        sleep(1)
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()
        print("login button clicked")
        sleep(1)
        currentURL = self.driver.current_url
        testResult = False
        sleep(1)
        if (currentURL.endswith("/inventory.html")):
            testResult = True
            print(f"test: {testResult}")
        else:
            print(f"test: {testResult}")
        sleep(3)

    def numberOfProduct(self):
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        clear()
        print("*****numberOfProduct*****")
        inputUsername = self.driver.find_element(By.ID, "user-name")
        inputUsername.send_keys("standard_user")
        print("username entered")
        sleep(1)
        inputPassword = self.driver.find_element(By.ID, "password")
        inputPassword.send_keys("secret_sauce")
        print("password entered")
        sleep(1)
        btnLogin = self.driver.find_element(By.ID, "login-button")
        btnLogin.click()
        print("login button clicked")
        sleep(1)
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        testResult = False
        sleep(2)
        if (len(products) == 6):
            testResult = True
            print(f"number of product: {len(products)}")
            print(f"test: {testResult}")
        else:
            print(f"number of product: {len(products)}")
            print(f"test: {testResult}")
        sleep(3)

    def allTest(self):
        self.emptyUsernamePasword()
        self.emptyPasword()
        self.lockedUser()
        self.iconX()
        self.standardUser()
        self.numberOfProduct()


def selectionMenu():
    clear()
    secim = input('''
    1-->> emptyUsernamePasword
    2-->> emptyPasword
    3-->> lockedUser
    4-->> iconX
    5-->> standardUser
    6-->> numberOfProduct
    7-->> all function
    test to be performed-->>: ''')

    if (secim == "1"):
        test.emptyUsernamePasword()

    elif (secim == "2"):
        test.emptyPasword()
    elif (secim == "3"):
        test.lockedUser()

    elif (secim == "4"):
        test.iconX()

    elif (secim == "5"):
        test.standardUser()

    elif (secim == "6"):
        # print("6")
        test.numberOfProduct()

    elif (secim == "7"):
        test.allTest()

    else:
        print("incorrect selection")


test = testSwagLabs()
selectionMenu()
