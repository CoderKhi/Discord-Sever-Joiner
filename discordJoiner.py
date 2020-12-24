import os
try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    os.system('pip3 install selenium')
    from selenium import webdriver
    
from selenium.webdriver.common.keys import Keys
from random import choice
from time import sleep
try:
    from pyautogui import click, write, alert, press
except:
    os.system("pip install pyautogui")
    os.system("pip3 install pyautogui")
    from pyautogui import click, write, alert, press
    
    
Controller1 = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

Controller1.get('https:discord.com/register');


class Controller1Master():
    def __init__(self, server):
        self.server = server
        self.delays = [5, 3, 12]
        self.accountUsernames = \
            ['joineraccount1', 'joineraccount2', 'joineraccount3', 'joineraccount4',
             'joineraccount5', 'joineraccount6', 'joineraccount7', 'joineraccount8',
             'joineraccount9', 'joineraccount10', 'joineraccount11', 'joineraccount12',
             'joineraccount21',
             'joineraccount22',
             'joineraccount23',
             'joineraccount24',
             'joineraccount25',
             'joineraccount26',
             'joineraccount27',
             'joineraccount28',
             'joineraccount29',
             'joineraccount30',
             'joineraccount31',
             'joineraccount32',
             'joineraccount33',
             'joineraccount34',
             'joineraccount35',
             'joineraccount36',
             'joineraccount37',
             'joineraccount38',
             'joineraccount39',
             'joineraccount40',
             'joineraccount41',
             'joineraccount42',
             'joineraccount43',
             'joineraccount44',
             'joineraccount45',
             'joineraccount46',
             'joineraccount47',
             'joineraccount48',
             'joineraccount49',
             'joineraccount50',
             'joineraccount51',
             'joineraccount52',
             'joineraccount53',
             'joineraccount54',
             'joineraccount55',
             'joineraccount56',
             'joineraccount57',
             'joineraccount58',
             'joineraccount59',
             'joineraccount60',
             'joineraccount61',
             'joineraccount62',
             'joineraccount63',
             'joineraccount64',
             'joineraccount65',
             'joineraccount66',
             'joineraccount67',
             'joineraccount68',
             'joineraccount69',
             'joineraccount70',
             'joineraccount71',
             'joineraccount72',
             'joineraccount73',
             'joineraccount74',
             'joineraccount75',
             'joineraccount76',
             'joineraccount77',
             'joineraccount78',
             'joineraccount79',
             'joineraccount80',
             'joineraccount81',
             'joineraccount82',
             'joineraccount83',
             'joineraccount84',
             'joineraccount85',
             'joineraccount86',
             'joineraccount87',
             'joineraccount88',
             'joineraccount89',
             'joineraccount90',
             'joineraccount91',
             'joineraccount92',
             'joineraccount93',
             'joineraccount94',
             'joineraccount95',
             'joineraccount96',
             'joineraccount97',
             'joineraccount98',
             'joineraccount99',
             'joineraccount100'
             ]

        self.accountPasswords = ['joineraccountpassword']

        self.usernameGen = choice(self.accountUsernames)

        for i in range(100):

            emailOrPhone = Controller1.find_element_by_name('email');
            emailOrPhone.send_keys(self.usernameGen + "@gmail.com")
            username = Controller1.find_element_by_name("username")
            username.send_keys(self.usernameGen)
            password = Controller1.find_element_by_name('password')
            password.send_keys(self.accountPasswords[0])
            monthSelection = click(597, 526)
            write('April')
            press('enter')
            write("4")
            press('enter')
            write("2000")
            press('enter')

            loginButton = Controller1.find_element_by_xpath(
                "/html/body/div/div[2]/div/div[2]/div/form/div/div[2]/div[5]/button")
            loginButton.click()
            print("Acocunt created. Info:"
                  f"{self.usernameGen}:{self.accountPasswords[0]}")
            sleep(3)
            Controller1.get(self.server)
            sleep(5)
            try:
                joinButton = Controller1.find_element_by_xpath(
                    '/html/body/div/div[2]/div/div[2]/div/section/div/button')
                joinButton.click()
                Controller1.implicitly_wait(2)
                continueToDiscord = Controller1.find_element_by_xpath(
                    '/html/body/div/div[2]/div/div/div/section/div/button')
                continueToDiscord.click()
            except ValueError:
                pass
            Controller1.implicitly_wait(19)
            settings = Controller1.find_element_by_xpath(
                '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[3]/button[3]')
            Controller1.execute_script("arguments[0].click();", settings);
            logoutButton = Controller1.find_element_by_xpath(
                '/html/body/div/div[2]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[24]')
            Controller1.execute_script("arguments[0].click();", logoutButton)
            Confirm = Controller1.find_element_by_xpath('/html/body/div/div[6]/div[2]/div/div/div[3]/button[1]')
            Controller1.execute_script("arguments[0].click();", Confirm)
            sleep(3)
            Controller1.get('https://discord.com/register')


Init1 = Controller1Master('https://discord.gg/python')
