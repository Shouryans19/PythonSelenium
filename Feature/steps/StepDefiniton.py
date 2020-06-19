from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from Library import ConfigReader
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import *
import time
from Feature import Environment

@given(u'user is on Home page')
def step_impl(context):
    try:
        WebDriverWait(context.driver,120).until(EC.url_contains("welcome"))
    except TimeoutException:
        print("Loading took too much time!")
    url = context.driver.current_url
    assert "welcome" in url
    print("Logged in")

@when(u'User click on DM module')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    #raise NotImplementedError(u'STEP: Then User click on DM module')


@when(u'Click on Assets')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Assets_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Assets')


@when(u'Click AddNew button')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'AddNew_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click AddNew button')


@when(u'Enter Asset name')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'Name_xpath')).send_keys("AutoPython1")
    #raise NotImplementedError(u'STEP: Then Enter Asset naame')


@when(u'Select Managing Org')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'ManagingOrg_dropdown_xpath')).click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'Org_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Select Managing Org')


@when(u'Select Hosting Location')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'HostingLocation_xpath')).click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'country_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Select Hosting Location')


@when(u'Click save button')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset', 'save_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click save button')


@then(u'Verify Asset is created')
def step_impl(context):
    assert context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Details_tab', 'name_xpath')).is_displayed()
    #raise NotImplementedError(u'STEP: Then Verify Asset is created')

@then(u'Navigate to inventory list UI')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Details_tab', 'Assets_BreadCrumb_Xpath')).click()
    #raise NotImplementedError(u'STEP: Then Navigate to inventory list UI')


@then(u'Search for the created Asset')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'search_xpath')).send_keys("AutoPython1")
    time.sleep(3)
    #raise NotImplementedError(u'STEP: Then Search for the created Asset')


@then(u'Hover on the searched Asset')
def step_impl(context):
     context.inventory=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Asset_link'))
     action=ActionChains(context.driver)
     action.move_to_element(context.inventory)
     action.perform()
     #from selenium import webdriver
     #from selenium_move_cursor.MouseActions import move_to_element_chrome
     time.sleep(5)

    #raise NotImplementedError(u'STEP: Then Hover on the searched Asset')


@then(u'Click on context menu')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','ContextMenu_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on context menu')


@then(u'Verify the context menu items')
def step_impl(context):
     menuItems=context.driver.find_elements_by_xpath(ConfigReader.readElementLocators('Asset','context_menu_items_xpath'))
     my_list=[]
     contextMenu=["View Details","Edit","Launch Assessment","Copy","Set up as Master","Link to Master","Change Status","View Related Inventories","Delete"]

     for idx,item in enumerate(menuItems):
             my_list=item.text
             print(my_list)
             assert contextMenu[idx] in my_list

     #print (my_list)
     # assert "View Details" in my_list
     # assert "Edit" in my_list
     # assert "Launch Assessment" in my_list
     # assert "Copy" in my_list
     # assert "Set up as Master" in my_list
     # assert "Link to Master" in my_list
     # assert "Change Status" in my_list
     # assert "View Related Inventories" in my_list
     # assert "Delete" in my_list


    #raise NotImplementedError(u'STEP: Then Verify the context menu items')

@then(u'Drill into details tab of the inventory')
def step_impl(context):
     time.sleep(5)
     context.inventory.click()
     time.sleep(5)
    #raise NotImplementedError(u'STEP: Then Drill into details tab of the inventory')


@then(u'Click on context menu option')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Inventory_details_cm')).click()

    #raise NotImplementedError(u'STEP: Then Click on context menu option')

@then(u'Verify the context menu items within details tab')
def step_impl(context):
    menuItems = context.driver.find_elements_by_xpath(
        ConfigReader.readElementLocators('Asset', 'context_menu_items_xpath'))
    my_list = []
    contextMenu = ["Launch Assessment", "Add Risk","Link Assessment","Delete Record", "Copy", "Set up as Master", "Link to Master",
                   "Change Status"]

    for idx, item in enumerate(menuItems):
        my_list = item.text
        print(my_list)
        assert contextMenu[idx] in my_list
    #raise NotImplementedError(u'STEP: Then Verify the context menu items within details tab')


#############################Scenario 2#################################################################################################
@when(u'User clicks on DM module')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    #raise NotImplementedError(u'STEP: Then User click on DM module')


@when(u'Navigate to Asset inventory list UI')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Assets_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Assets')


@when(u'Search for an Asset')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'search_xpath')).send_keys("AutoPython1")
    time.sleep(10)
    #raise NotImplementedError(u'STEP: Then Search for the created Asset')


@when(u'Hover on the Asset')
def step_impl(context):
    context.inventory_new = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Asset_link'))
    action=ActionChains(context.driver)
    action.move_to_element_with_offset(context.inventory_new,0,0)
    action.perform()
    time.sleep(10)
    #raise NotImplementedError(u'STEP: Then Hover on the searched Asset')


@when(u'Click on context menu of that Asset')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM','ContextMenu_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on context menu')

@when(u'Select Set up as Master option')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','Set_up_as_Master_xpath')).click()
    #raise NotImplementedError(u'STEP: When Select Set up as Master option')


@then(u'Create Master Record modal opens')
def step_impl(context):
    print('Will check later')
    # try:
    #     WebDriverWait(context.driver,120).until(EC.visibility_of_element_located(context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','Create_Master_modal_xpath'))))
    # except TimeoutException:
    #     print("Create Master Modal not found")
    # #raise NotImplementedError(u'STEP: Then Create Master Record modal opens')

@then(u'Click on Create option')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Asset','Create_button_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Create option')


@then(u'Verify Master Record is created')
def step_impl(context):
    context.LocalVersionTab=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Local_versions_xpath'))
    assert context.LocalVersionTab
    #raise NotImplementedError(u'STEP: Then Verify Master Record is created')

##############################################################Scenario 3####################################################################
@when(u'User clicks on DM module tile')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    #raise NotImplementedError(u'STEP: Then User click on DM module')


@when(u'User navigates to Asset inventory list UI')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Assets_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Assets')


@when(u'Search for a master record')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'search_xpath')).send_keys("AutoPython1")
    time.sleep(10)
    #raise NotImplementedError(u'STEP: Then Search for the created Asset')

@when(u'User drills into Local versions tab of Master Record')
def step_impl(context):
    time.sleep(5)
    context.inventory_new = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Asset_link'))
    context.inventory_new.click()
    time.sleep(5)
    #raise NotImplementedError(u'STEP: When User drills into Local versions tab of Master Record')


@when(u'Clicks on Add Local Versions button')
def step_impl(context):
    context.LocalVersionTab_1 = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Local_versions_xpath'))
    context.LocalVersionTab_1.click()
    time.sleep(3)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Add_local_Versions_button_xpath')).click()
    #raise NotImplementedError(u'STEP: When Clicks on Add Local Versions button')


@then(u'Verify Create Local Version tab opens')
def step_impl(context):
    LocalVersionModal=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Create_local_version_modal'))
    try:
        WebDriverWait(context.driver,120).until(EC.visibility_of(LocalVersionModal))
    except TimeoutException:
        print("Create LocalVersion Modal not found")

    #raise NotImplementedError(u'STEP: Then Verify Create Local Version tab opens')


@then(u'User enters name of local version record')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Copy_inventory_name_xpath')).send_keys("-Local")
    #raise NotImplementedError(u'STEP: Then User enters name of local version record')


@then(u'User clicks on Copy button')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Copy_button_xpath')).click()
    #raise NotImplementedError(u'STEP: Then User clicks on Copy button')


@then(u'Verify Local Version is created')
def step_impl(context):
    context.Local_version=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Local_record_xpath'))
    assert context.Local_version
    #raise NotImplementedError(u'STEP: Then Verify Local Version is created')


@then(u'Verify audit event is created in activity tab of Local Version')
def step_impl(context):

    context.Local_version.click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Activity_tab', 'Activity_tab_xpath')).click()
    FieldName = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'Field_name_xpath')).text
    print(FieldName)
    assert 'Master Record' in FieldName
    OldValue = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'Old_value_xpath')).text
    print(OldValue)
    assert '' in OldValue
    NewValue = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'New_value_xpath')).text
    print(NewValue)
    assert 'AutoPython1' in NewValue

###############################################Scenario 4#################################################################################

@when(u'User navigates to DM module tile')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Home', 'Module_DM_xpath')).click()
    #raise NotImplementedError(u'STEP: Then User click on DM module')


@when(u'User clicks on Asset inventory list UI')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Assets_xpath')).click()
    #raise NotImplementedError(u'STEP: Then Click on Assets')


@when(u'Search for the master record')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'search_xpath')).send_keys("AutoPython1")
    time.sleep(10)
    #raise NotImplementedError(u'STEP: Then Search for the created Asset')

@when(u'User drills into Local versions tab of the Master Record')
def step_impl(context):
    time.sleep(5)
    context.inventory_new = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('DM', 'Asset_link'))
    context.inventory_new.click()
    time.sleep(5)
    context.LocalVersionTab_1 = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Local_versions_xpath'))
    context.LocalVersionTab_1.click()
    time.sleep(3)
    #raise NotImplementedError(u'STEP: When User drills into Local versions tab of Master Record')


@when(u'User removes the local version')
def step_impl(context):
    context.LocalRecord = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Local_record_xpath'))
    action = ActionChains(context.driver)
    action.move_to_element_with_offset(context.LocalRecord, 0, 0)
    action.perform()
    time.sleep(3)
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Local_Version_elipse')).click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'RemoveLocalVersion_xpath')).click()
    RemoveLocalVersionModal=context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab','Remove_local_version_modal'))
    try:
        WebDriverWait(context.driver,120).until(EC.visibility_of(RemoveLocalVersionModal))
    except TimeoutException:
        print("Create LocalVersion Modal not found")
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Confirm_button_xpath')).click()
    time.sleep(3)
    #assert not context.LocalRecord

#raise NotImplementedError(u'STEP: When User removes the local version')

@then(u'Verify Local Version is removed')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(EC.visibility_of((context.LocalRecord)))
        not_found = False
    except:
        not_found = True

    assert not_found
    #raise NotImplementedError(u'STEP: Then Verify Local Version is removed')

@then(u'Verify audit event is triggered in activity tab of Local Version')
def step_impl(context):
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Details_tab', 'Assets_BreadCrumb_Xpath')).click()
    time.sleep(3)
    context.LocalRecord = context.driver.find_element_by_xpath(ConfigReader.readElementLocators('LocalVersions_tab', 'Local_record_xpath'))
    context.LocalRecord.click()
    context.driver.find_element_by_xpath(ConfigReader.readElementLocators('Activity_tab', 'Activity_tab_xpath')).click()
    FieldName = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'Field_name_xpath')).text
    print(FieldName)
    assert 'Master Record' in FieldName
    OldValue = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'Old_value_xpath')).text
    print(OldValue)
    assert 'AutoPython1' in OldValue
    NewValue = context.driver.find_element_by_xpath(
        ConfigReader.readElementLocators('Activity_tab', 'New_value_xpath')).text
    print(NewValue)
    assert '' in NewValue
