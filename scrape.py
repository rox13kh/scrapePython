from selenium import webdriver

def getHeroInfo():
    heroName = driver.find_element_by_class_name('module__title__link').text
    heroAbout = driver.find_element_by_class_name('js-about-item-abstr').text
    print("Name of hero: " + heroName + "\n" + "Bio: " + heroAbout + "\n")

#open Chrome
driver = webdriver.Chrome()

#go to duckduckgo
driver.get('https://duckduckgo.com')

arr = ['doctor strange', 'captain america', 'captain marvel',
       'black panther', 'scarlet witch', 'starlord', 'thor marvel',
       'thanos', 'ant man', 'gamora']

driver.find_element_by_id('search_form_input_homepage').send_keys(arr[0])
driver.find_element_by_id('search_button_homepage').click()

getHeroInfo()

for x in range(1, len(arr)):
    driver.find_element_by_id('search_form_input').clear()
    driver.find_element_by_id('search_form_input').send_keys(arr[x])
    driver.find_element_by_id('search_button').click()
    getHeroInfo()

driver.quit()
#driver.find_element_by_xpath('//*[@id="duckbar_static"]/li[2]/a').click()
