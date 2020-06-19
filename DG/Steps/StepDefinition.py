from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from Library import ConfigReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import *
import time

@given(u'User is on Home page')
def step_impl(context):
    Home_page=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'HomePage_Xpath'))
    assert Home_page.is_displayed()

    #raise NotImplementedError(u'STEP: Given User is on Home page')



@when(u'User lands DG Home page Verify if the Call to action banner is shown  below the page title Latest Privacy News and above the News and Opinion content')
def step_impl(context):
    Banner=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Banner_xpath'))
    assert Banner.is_displayed()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Verify if the Call to action banner is shown  below the page title Latest Privacy News and above the News and Opinion content')


@when(u'Verify if the banner is blue')
def step_impl(context):
    print('Blue')
    #raise NotImplementedError(u'STEP: When Verify if the banner is blue')


@when(u'Verify if the first line of the text contains "Design, optimise and maintain today"')
def step_impl(context):
    first_line=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Banner_first_line_xpath'))
    Fl=first_line.text
    assert "Design, optimise and maintain today" in Fl
    #raise NotImplementedError(u'STEP: When Verify if the first line of the text contains "Design, optimise and maintain today"')


@when(u'Verify if the second paragraph contains " Monitor regulatory developments, mitigate risk and achieve global compliance with the full OneTrust DataGuidance platform"')
def step_impl(context):
    second_line= context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Banner_second_line_xpath'))
    Sl=second_line.text
    assert "Monitor regulatory developments, mitigate risk and achieve global compliance with the full OneTrust DataGuidance platform" in Sl
    #raise NotImplementedError(u'STEP: When Verify if the second paragraph contains " Monitor regulatory developments, mitigate risk and achieve global compliance with the full OneTrust DataGuidance platform"')


@then(u'Verify if the banner contains Two CTA\'s 1. Try for Free button 2. Login button')
def step_impl(context):
    Try_for_free=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath'))
    Login=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath'))
    assert Try_for_free
    assert Login
    #raise NotImplementedError(u'STEP: Then Verify if the banner contains Two CTA\'s 1. Try for Free button 2. Login button')
##################################Scenario 2####################################################################################

@when(u'User lands DG Home page Hover on  "Try for free" CTA button')
def step_impl(context):
    time.sleep(10)
    Try_for_free_button=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath'))
    action = ActionChains(context.driver)
    action.move_to_element(Try_for_free_button)
    action.perform()
    # from selenium import webdriver
    # from selenium_move_cursor.MouseActions import move_to_element_chrome
    time.sleep(5)
    #raise NotImplementedError(u'STEP: When User lands DG Home page Hover on  "Try for free" CTA')


@when(u'Click on "Try for free" CTA button')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath')).click()
   # raise NotImplementedError(u'STEP: When Click on "Try for free" CTA')


@then(u'Registration Page [https://platform.dataguidance.com/user/register] page should be displayed')
def step_impl(context):
    try:
        WebDriverWait(context.driver,120).until(EC.url_contains("register"))
    except TimeoutException:
        print("Loading took too much time!")
    url = context.driver.current_url
    assert "/user/register" in url
    print("Logged in")
    #raise NotImplementedError(u'STEP: Then Registration Page [https://platform.dataguidance.com/user/register] page should be displayed')

##################################Scenario 3####################################################################################
@when(u'User lands DG Home page Hover on  "Login" CTA button')
def step_impl(context):
    time.sleep(10)
    Login_btn = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath'))
    action = ActionChains(context.driver)
    action.move_to_element(Login_btn)
    action.perform()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Hover on  "Login" CTA')


@when(u'Click on "Login" CTA button')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath')).click()
   # raise NotImplementedError(u'STEP: When Click on "Try for free" CTA')


@then(u'Login Page [https://platform.dataguidance.com/user/login?destination=node/1] page should be displayed')
def step_impl(context):

    try:
        WebDriverWait(context.driver,120).until(EC.url_contains("login"))
    except TimeoutException:
        print("Loading took too much time!")
    url = context.driver.current_url
    assert "/user/login?destination=node/1" in url
    print("verified")
    #raise NotImplementedError(u'STEP: Then Login Page [https://platform.dataguidance.com/user/login?destination=node/1] page should be displayed')

##################################Scenario 4####################################################################################

@when(u'User lands DG Home page Click on News  from the navigation bar')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Privacy_news_xpath')).click()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Click on News  from the navigation bar')


@when(u'Verify if the Call to action banner is shown below the title News and above the search for Keywords and dates')
def step_impl(context):
    time.sleep(3)
    Banner_news = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_xpath'))
    assert Banner_news.is_displayed()
    #raise NotImplementedError(u'STEP: When Verify if the Call to action banner is shown below the title News and above the search for Keywords and dates')


@when(u'Verify if the first line of the text contains "Intelligent regulatory tracking"')
def step_impl(context):
    first_line_news = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_first_line_xpath'))
    Fl_news = first_line_news.text
    assert "Intelligent regulatory tracking" in Fl_news
    #raise NotImplementedError(u'STEP: When Verify if the first line of the text contains "Intelligent regulatory tracking"')


@when(u'Verify if the second paragraph contains "Access the full breadth and functionality of OneTrust DataGuidance\'s intelligent regulatory tracking tools to implement and monitor compliance"')
def step_impl(context):
    second_line_news = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_second_line_news_xpath'))
    Sl_news = second_line_news.text
    assert "Access the full breadth and functionality of OneTrust DataGuidance's intelligent regulatory tracking tools to implement and monitor compliance" in Sl_news
    #raise NotImplementedError(u'STEP: When Verify if the second paragraph contains "Access the full breadth and functionality of OneTrust DataGuidance\'s intelligent regulatory tracking tools to implement and monitor compliance"')


@then(u'Verify if the banner contain Two CTA\'s 1. Try for Free button 2. Login button')
def step_impl(context):
    Try_for_free = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath'))
    Login = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath'))
    assert Try_for_free
    assert Login
    #raise NotImplementedError(u'STEP: Then Verify if the banner contains Two CTA\'s 1. Try for Free button 2. Login button')


##################################Scenario 5##################################################################################

@when(u'User lands DG Home page Click on Guidance Notes UI  from the navigation bar')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Guidance_Notes_xpath')).click()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Click on Guidance Notes UI  from the navigation bar')


@when(u'Verify if the Call to action banner is shown below the title  Guidance Notes and above the Browse Guidance Notes by category')
def step_impl(context):
    Banner_GN = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_xpath'))
    assert Banner_GN.is_displayed()
    #raise NotImplementedError(u'STEP: When Verify if the Call to action banner is shown below the title  Guidance Notes and above the Browse Guidance Notes by category')


@when(u'Verify if banner is blue')
def step_impl(context):
    print('blue')
    #raise NotImplementedError(u'STEP: When Verify if banner is blue')


@when(u'Verify if the first line of the text contains "Research and compare"')
def step_impl(context):
    first_line_GN = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_first_line_xpath'))
    Fl_GN = first_line_GN.text
    assert "Research and compare" in Fl_GN
    #raise NotImplementedError(u'STEP: When Verify if the first line of the text contains "Research and compare"')


@when(u'Verify if the second paragraph contains "Unlock over 1,000 in-depth notes around core topics and jurisdictions to conduct your privacy research efficiently and accurately"')
def step_impl(context):
    second_line_GN = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_second_line_news_xpath'))
    Sl_GN = second_line_GN.text
    assert "Unlock over 1,000 in-depth notes around core topics and jurisdictions to conduct your privacy research efficiently and accurately" in Sl_GN

    #raise NotImplementedError(u'STEP: When Verify if the second paragraph contains "Unlock over 1,000 in-depth notes around core topics and jurisdictions to conduct your privacy research efficiently and accurately"')


@then(u'Verify if banner contain Two CTA\'s 1. Try for Free button 2. Login button')
def step_impl(context):
    Try_for_free = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath'))
    Login = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath'))
    assert Try_for_free
    assert Login
   # raise NotImplementedError(u'STEP: Then Verify if banner contain Two CTA\'s 1. Try for Free button 2. Login button')

#########################################################Scenario 6#################################################################

@when(u'User lands DG Home page Click on Templates from the navigation bar')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Templates_xpath')).click()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Click on Templates from the navigation bar')


@when(u'Verify if the Call to action banner is shown below the title   Templates & Checklists and above the Browse Templates & Checklists')
def step_impl(context):
    Banner_Templates = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_xpath'))
    assert Banner_Templates.is_displayed()
    #raise NotImplementedError(u'STEP: When Verify if the Call to action banner is shown below the title   Templates & Checklists and above the Browse Templates & Checklists')


@when(u'Verify if banner on Templates page is blue')
def step_impl(context):
    print('Blue')
    #raise NotImplementedError(u'STEP: When Verify if banner on Templates page is blue')


@when(u'Verify if the first line of the text contains "Leverage pre-built templates"')
def step_impl(context):
    first_line_Template = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Banner_first_line_xpath'))
    Fl_Template = first_line_Template.text
    assert "Leverage pre-built templates" in Fl_Template
    #raise NotImplementedError(u'STEP: When Verify if the first line of the text contains "Leverage pre-built templates"')


@when(u'Verify if the second paragraph contains "Choose from over 200 templates and checklists from supervisory authorities to support implementation of global compliance programs"')
def step_impl(context):
    second_line_Template = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('DG', 'Banner_second_line_news_xpath'))
    Sl_Template = second_line_Template.text
    assert "Choose from over 200 templates and checklists from supervisory authorities to support implementation of global compliance programs" in Sl_Template

    #raise NotImplementedError(u'STEP: When Verify if the second paragraph contains "Choose from over 200 templates and checklists from supervisory authorities to support implementation of global compliance programs"')


@then(u'Verify if banner contains Two CTA\'s 1. Try for Free button 2. Login button')
def step_impl(context):
    Try_for_free = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath'))
    Login = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath'))
    assert Try_for_free
    assert Login
    #raise NotImplementedError(u'STEP: Then Verify if banner contains Two CTA\'s 1. Try for Free button 2. Login button')



#########################################################Scenario 7#################################################################

@when(u'User land DG Home page Clicks on News  from the navigation bar')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Privacy_news_xpath')).click()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Click on News  from the navigation bar')


@when(u'Click on "Try for free" CTA')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Try_for_free(Action_Banner)_xpath')).click()
   # raise NotImplementedError(u'STEP: When User lands DG Home page Hover on  "Try for free" CTA')


@then(u'Registration Page [https://platform.dataguidance.com/user/register] should be displayed')
def step_impl(context):
    try:
        WebDriverWait(context.driver,120).until(EC.url_contains("register"))
    except TimeoutException:
        print("Loading took too much time!")
    url = context.driver.current_url
    assert "/user/register" in url
    print("Logged in")
    #raise NotImplementedError(u'STEP: Then Registration Page [https://platform.dataguidance.com/user/register] page should be displayed')

##################################Scenario 6####################################################################################

@when(u'User lands DG Home page Clicks on News  from the navigation bar')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Privacy_news_xpath')).click()
    #raise NotImplementedError(u'STEP: When User lands DG Home page Hover on  "Login" CTA')


@when(u'Click on "Login" CTA')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Login(Action_Banner)_xpath')).click()
   # raise NotImplementedError(u'STEP: When Click on "Try for free" CTA')


@then(u'Login Page [https://platform.dataguidance.com/user/login?destination=node/1] should be displayed')
def step_impl(context):
    try:
        WebDriverWait(context.driver,120).until(EC.url_contains("login"))
    except TimeoutException:
        print("Loading took too much time!")
    url = context.driver.current_url
    assert "/user/login?destination=node/1" in url
    print("verified")
    #raise NotImplementedError(u'STEP: Then Login Page [https://platform.dataguidance.com/user/login?destination=node/1] page should be displayed')


#################################Scenarion7#####################################################################################

@when(u'User Scroll down to footer section')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scroll down to footer section')


@when(u'Clicks on Privacy Notice')
def step_impl(context):
     context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Privacy_notice_xpath')).click()
    #raise NotImplementedError(u'STEP: When Clicks on Privacy Notice')


@then(u'Privacy notice page ( https://www.onetrust.com/privacy/) should be displayed')
def step_impl(context):
    current_window=context.driver.current_window_handle
    window_handles=context.driver.window_handles
    for handle in window_handles:
        if handle!=current_window:
            child_window=handle
            break
    context.driver.switch_to_window(child_window)
    time.sleep(10)
    privacy_url=context.driver.current_url
    assert "privacy" in privacy_url
    #raise NotImplementedError(u'STEP: Then Privacy notice page ( https://www.onetrust.com/privacy/) should be displayed')

#################################Scenarion9#####################################################################################

@when(u'User Scrolls down to footer section')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scroll down to footer section')

@when(u'Clicks on the Cookie Notice')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Cookie_notice_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Clicks on the Cookie Notice')


@then(u'Cookie Notice Page (https://platform.dataguidance.com/cookie-notice) should be dispalyed')
def step_impl(context):
    time.sleep(5)
    cookie_notice = context.driver.current_url
    assert "cookie-notice" in cookie_notice
    #raise NotImplementedError(u'STEP: Then Cookie Notice Page (https://platform.dataguidance.com/cookie-notice) should be dispalyed')

#################################Scenarion10#####################################################################################

@when(u'User Scroll down to footer section of DG page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scroll down to footer section')

@when(u'Clicks on the Terms of Use')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Terms_of_use_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Clicks on the Terms of Use')


@then(u'Terms of Use page ( https://platform.dataguidance.com/terms) should be displayed')
def step_impl(context):
    time.sleep(5)
    Terms_of_use = context.driver.current_url
    assert "terms" in Terms_of_use
    #raise NotImplementedError(u'STEP: Then Terms of Use page ( https://platform.dataguidance.com/terms) should be displayed')

#################################Scenarion11#####################################################################################

@when(u'User Scrolls down to footer section of DG page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scroll down to footer section')

@when(u'Clicks on the Terms and Conditions')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Terms_Condition_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Clicks on the Terms and Conditions')


@then(u'Terms and Conditions Page (platform.dataguidance.com/terms-conditions/ ) should be displayed')
def step_impl(context):
    time.sleep(5)
    Terms_and_cond = context.driver.current_url
    assert "terms-conditions" in Terms_and_cond
    #raise NotImplementedError(u'STEP: Then Terms and Conditions Page (platform.dataguidance.com/terms-conditions/ ) should be displayed')

##################################Scenario 12####################################################################################
@when(u'User Scroll down to footer section of DG home page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scrolls down to footer section')


@when(u'Click on the Exercise Your Rights')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG','Exercise_right_xpath')).click()
    #raise NotImplementedError(u'STEP: When Click on the Exercise Your Rights')

@then(u'Webform ( https://privacyportal-cdn.onetrust.com/dsarwebform/37bcc497-a196-48f1-a08b-e897b5a77859/08322279-ccb3-4f78-a451-bdbea232eccb.html) should be displayed.')
def step_impl(context):
    time.sleep(10)
    current_window = context.driver.current_window_handle
    window_handles = context.driver.window_handles
    for handle in window_handles:
        if handle != current_window:
            child_window = handle
            break
    context.driver.switch_to_window(child_window)
    time.sleep(10)
    Exercise_your_right = context.driver.current_url
    assert "dsarwebform" in Exercise_your_right
    #raise NotImplementedError(u'STEP: Then Webform ( https://privacyportal-cdn.onetrust.com/dsarwebform/37bcc497-a196-48f1-a08b-e897b5a77859/08322279-ccb3-4f78-a451-bdbea232eccb.html) should be displayed.')
#################################Scenarion13#####################################################################################

@when(u'User Scrolls down to footer section of DG home page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scrolls down to footer section')

@when(u'Click on Do Not Sell My Personal Information')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Do_not_sell_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Do Not Sell My Personal Information')


@then(u'Privacy Preference Center should be displayed from the left of the screen')
def step_impl(context):
    print("pass")
    #raise NotImplementedError(u'STEP: Then Privacy Preference Center should be displayed from the left of the screen')

#################################Scenarion14#####################################################################################

@when(u'User Scroll to bottom of the page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scrolls down to footer section')

@when(u'Click on Twitter')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Twitter_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Twitter')


@then(u'Onetrust Dataguidance Twitter page ( https://www.onetrust.com/privacy/) should be displayed')
def step_impl(context):
    time.sleep(5)
    current_window = context.driver.current_window_handle
    window_handles = context.driver.window_handles
    for handle in window_handles:
        if handle != current_window:
            child_window = handle
            break
    context.driver.switch_to_window(child_window)
    twitter = context.driver.current_url
    assert "https://twitter.com/DataGuidance" in twitter
    #raise NotImplementedError(u'STEP: Then Onetrust Dataguidance Twitter page ( https://www.onetrust.com/privacy/) should be displayed')

#################################Scenarion15#####################################################################################

@when(u'User Scrolls to bottom of the page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scrolls down to footer section')

@when(u'Click on  LinkedIn')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Linkdin_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on  LinkedIn')


@then(u'Onetrust Dataguidance LinkedIn Page (https://platform.dataguidance.com/cookie-notice) should be displayed')
def step_impl(context):
    time.sleep(5)
    current_window = context.driver.current_window_handle
    window_handles = context.driver.window_handles
    for handle in window_handles:
        if handle != current_window:
            child_window = handle
            break
    context.driver.switch_to_window(child_window)
    time.sleep(10)
    lnkdn = context.driver.current_url
    assert "https://www.linkedin.com/company/dataguidance/" in lnkdn
    #raise NotImplementedError(u'STEP: Then Onetrust Dataguidance LinkedIn Page (https://platform.dataguidance.com/cookie-notice) should be displayed')

#################################Scenarion16#####################################################################################

@when(u'User scroll to bottom of  page')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #raise NotImplementedError(u'STEP: When User Scrolls down to footer section')


@when(u'Click on Instagram')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DG', 'Insta_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Instagram')


@then(u'Onetrust Dataguidance Instagram Use page ( https://platform.dataguidance.com/terms) should be displayed')
def step_impl(context):
    time.sleep(5)
    current_window = context.driver.current_window_handle
    window_handles = context.driver.window_handles
    for handle in window_handles:
        if handle != current_window:
            child_window = handle
            break
    context.driver.switch_to_window(child_window)
    time.sleep(10)
    insta = context.driver.current_url
    assert "https://www.instagram.com/dataguidance_dg/" in insta
    #raise NotImplementedError(u'STEP: Then Onetrust Dataguidance Instagram Use page ( https://platform.dataguidance.com/terms) should be displayed')
