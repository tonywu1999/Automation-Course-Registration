# SIS & Brody Automated Registration

Run: python3 brody.py

This is a script that you can run to automate registering for classes
and automate registering for a brody room at a designated time.

NOTE: You must download the selenium and webdriver package before
running this script because that package allows you to automate
opening up google chrome.  Unfortunately, I kind of forgot the whole
process of downloading selenium.

I think it may be the following though not exactly sure:
pip install selenium

Ultimately, the script will ask for your username and password
and in the main method, you can designate whether to run the
brody scheme or the course registration scheme.  You can designate
with the datetime package when the webdriver should open and perform
certain actions.
