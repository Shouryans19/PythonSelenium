Feature: Login Functionality
	 Here we target end to end scenarios

Background:
	 Given User is on Home page

Scenario: Verify context menu items on both Inventory List UI and Details Page for Asset
	When User click on DM module
	      And Click on Assets
	      And Click AddNew button
	      And Enter Asset name
	      And Select Managing Org
	      And Select Hosting Location
	      And Click save button
	  Then Verify Asset is created
	      And Navigate to inventory list UI
	      And Search for the created Asset
	      And Hover on the searched Asset
	      And Click on context menu
	  Then Verify the context menu items
	      And Drill into details tab of the inventory
	      And Click on context menu option
	  Then Verify the context menu items within details tab

Scenario: Add a record as master
	When User clicks on DM module
	      And Navigate to Asset inventory list UI
	      And Search for an Asset
	      And Hover on the Asset
	      And Click on context menu of that Asset
	      And Select Set up as Master option
	Then Create Master Record modal opens
	     And Click on Create option
	Then Verify Master Record is created

Scenario: Verify Audit event (on local record) - adding a local version from a master
	When User clicks on DM module tile
	      And User navigates to Asset inventory list UI
	      And Search for a master record
          And User drills into Local versions tab of Master Record
	     And Clicks on Add Local Versions button
	Then Verify Create Local Version tab opens
	     And User enters name of local version record
	     And User clicks on Copy button
	Then Verify Local Version is created
	     And Verify audit event is created in activity tab of Local Version


Scenario: Verify Audit event (on local record) - removing a local version from a master
	When User navigates to DM module tile
	      And User clicks on Asset inventory list UI
	      And Search for the master record
          And User drills into Local versions tab of the Master Record
	      And User removes the local version
	Then Verify Local Version is removed
	     And Verify audit event is triggered in activity tab of Local Version