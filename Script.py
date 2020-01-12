from selenium import webdriver  
from selenium.webdriver.common.keys import Keys 
import time
import random

class InstaLikeBot:
    def __init__(self,username,password):   #Constructor for InstaLikeBot class
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox() #object for handling firefox browser
    

    def login(self):  
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        
        time.sleep(5)
        email=bot.find_element_by_name('username')
        password=bot.find_element_by_name('password')
        
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        
    def like_post(self,hashtag):
        count=0
        bot = self.bot

        #if you want to search hashtag use the first line bellow ->
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')

        #if you want to search people username use bellow line ->
        bot.get('http://www.instagram.com/'+hashtag+'/')

        #when using one of this above link comment the other one to make it work 

        time.sleep(4)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(random.randrange(3,5))
            posts = bot.find_elements_by_class_name('v1Nh3')
            links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in posts]
            #we get links in the format of instagram.com/p/id
           
            for link in links:
                count=count+1
                if(count<25):
                    bot.get(link)
                    try:
                        
                    
                        div=bot.find_elements_by_class_name('dCJp8')
                        time.sleep(random.randrange(1,3))
                        
                        #clicking heart to like image
                        lov = [el.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click() for el in div]
                        
                        time.sleep(random.randrange(4,9))
                    except Exception as ex:
                        time.sleep(30)
                else:
                    bot.close()    
                    
#declaring object for InstaLikeBot class and invoking the constructor,login function,like_post function using the object 
# In InstaLikeBot() here provide your instagram Email or username and Password
# In like_post() provide the hashtag for which likes must me provided   
                
obj = InstaLikeBot('<YOUR USERNAME>','<YOUR PASSWORD>')
obj.login()
obj.like_post('<ENTER HASHTAG/USERNAME>')