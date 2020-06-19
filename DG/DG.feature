Feature: DG functionality
	 Here we target DG scenarios

Background:
	 Given User is on Home page

Scenario: Verify D7 CTA Banner: Homepage UI
  When User lands DG Home page Verify if the Call to action banner is shown  below the page title Latest Privacy News and above the News and Opinion content
     And  Verify if the banner is blue
     And  Verify if the first line of the text contains "Design, optimise and maintain today"
     And  Verify if the second paragraph contains " Monitor regulatory developments, mitigate risk and achieve global compliance with the full OneTrust DataGuidance platform"
  Then Verify if the banner contains Two CTA's 1. Try for Free button 2. Login button


Scenario: Verify D7 CTA Banner: Homepage Try for free CTA
  When User lands DG Home page Hover on  "Try for free" CTA button
    And Click on "Try for free" CTA button
  Then Registration Page [https://platform.dataguidance.com/user/register] page should be displayed


Scenario: Verify D7 CTA Banner: Homepage Login CTA functionality
  When User lands DG Home page Hover on  "Login" CTA button
    And Click on "Login" CTA button
  Then Login Page [https://platform.dataguidance.com/user/login?destination=node/1] page should be displayed

Scenario: Verify D7 CTA Banner: News UI
  When User lands DG Home page Click on News  from the navigation bar
    And Verify if the Call to action banner is shown below the title News and above the search for Keywords and dates
    And  Verify if the banner is blue
    And  Verify if the first line of the text contains "Intelligent regulatory tracking"
    And  Verify if the second paragraph contains "Access the full breadth and functionality of OneTrust DataGuidance's intelligent regulatory tracking tools to implement and monitor compliance"
  Then Verify if the banner contain Two CTA's 1. Try for Free button 2. Login button


Scenario: Verify D7 CTA Banner: News Try for free CTA
  When User land DG Home page Clicks on News  from the navigation bar
    And Click on "Try for free" CTA
  Then Registration Page [https://platform.dataguidance.com/user/register] should be displayed


Scenario: Verify D7 CTA Banner: News/Homepage Login CTA functionality
  When User lands DG Home page Clicks on News  from the navigation bar
    And Click on "Login" CTA
  Then Login Page [https://platform.dataguidance.com/user/login?destination=node/1] should be displayed


Scenario: Verify D7 CTA Banner: Guidance Notes UI
  When User lands DG Home page Click on Guidance Notes UI  from the navigation bar
    And Verify if the Call to action banner is shown below the title  Guidance Notes and above the Browse Guidance Notes by category
    And  Verify if banner is blue
    And  Verify if the first line of the text contains "Research and compare"
    And  Verify if the second paragraph contains "Unlock over 1,000 in-depth notes around core topics and jurisdictions to conduct your privacy research efficiently and accurately"
  Then Verify if banner contain Two CTA's 1. Try for Free button 2. Login button


Scenario: Verify D7 CTA Banner: Templates UI
  When User lands DG Home page Click on Templates from the navigation bar
    And Verify if the Call to action banner is shown below the title   Templates & Checklists and above the Browse Templates & Checklists
    And  Verify if banner on Templates page is blue
    And  Verify if the first line of the text contains "Leverage pre-built templates"
    And  Verify if the second paragraph contains "Choose from over 200 templates and checklists from supervisory authorities to support implementation of global compliance programs"
  Then Verify if banner contains Two CTA's 1. Try for Free button 2. Login button



Scenario: Verify D7 Footer Updates Sections Our Policies Functionality
  When User Scroll down to footer section
     And Clicks on Privacy Notice
  Then Privacy notice page ( https://www.onetrust.com/privacy/) should be displayed

Scenario: Verify D7 Footer Updates Sections Our Policies Functionality/Cookie Notice
   When User Scrolls down to footer section
     And Clicks on the Cookie Notice
  Then Cookie Notice Page (https://platform.dataguidance.com/cookie-notice) should be dispalyed

Scenario: Verify D7 Footer Updates Sections Our Policies Functionality/Terms of Use
  When User Scroll down to footer section of DG page
    And Clicks on the Terms of Use
  Then Terms of Use page ( https://platform.dataguidance.com/terms) should be displayed

Scenario: Verify D7 Footer Updates Sections Our Policies Functionality/Terms and Conditions
  When User Scrolls down to footer section of DG page
    And Clicks on the Terms and Conditions
  Then Terms and Conditions Page (platform.dataguidance.com/terms-conditions/ ) should be displayed

Scenario: Verify D7 Footer Updates Sections Your Rights Functionality
  When User Scroll down to footer section of DG home Page
     And Click on the Exercise Your Rights
  Then Webform ( https://privacyportal-cdn.onetrust.com/dsarwebform/37bcc497-a196-48f1-a08b-e897b5a77859/08322279-ccb3-4f78-a451-bdbea232eccb.html) should be displayed.

Scenario: Verify D7 Footer Updates Sections Your Rights Functionality/Do Not Sell My Personal Information
  When User Scrolls down to footer section of DG home Page
    And Click on Do Not Sell My Personal Information
  Then Privacy Preference Center should be displayed from the left of the screen

Scenario: Verify D7 Footer Updates Sections Your Rights Functionality/Twitter
  When User scroll to bottom of the page
    And Click on Twitter
  Then Onetrust Dataguidance Twitter page ( https://www.onetrust.com/privacy/) should be displayed

Scenario: Verify D7 Footer Updates Sections Your Rights Functionality/Linkdin
  When User scrolls to bottom of the page
    And Click on  LinkedIn
  Then Onetrust Dataguidance LinkedIn Page (https://platform.dataguidance.com/cookie-notice) should be displayed

Scenario: Verify D7 Footer Updates Sections Your Rights Functionality/Insta
  When User scroll to bottom of  page
    And Click on Instagram
  Then Onetrust Dataguidance Instagram Use page ( https://platform.dataguidance.com/terms) should be displayed



