I created this script with a simple interface in order to automatically publish on one of my sites without any interference from me, this site is for publishing mobile applications, and in order to publish in it manually, I have to copy the content from Play store (apps) and re-upload it to My website WordPress and this takes a lot of time per day To publish only 30 or 50 applications, so I created this program so that I could publish 100 applications with the click of a button.

This program consists of 1253 lines of code.

As I always say, I know that it is easy for professional programmers and not that difficult, but it is normal for me because I am still on my way to professionalism and have not yet become a professional, as any ambitious programmer I always try to develop my abilities in order to keep pace with the development of all technologies.
Program action steps:

Script actions steps:

1-browse category on play store to get links of 20 apps.

2-browse all link apps one by one and copy all data I need (data: title-img-description-app link).

3-browse WordPress site and login

5-browse new post

6-past all data one by one as an download app form like in play store

7-click publish button

8-script will repeat this process again and again for 20 times


Libraries I use in this script :

Tkinter : create GUI for script python.
Selenium Webdriver : create autotest, scraping information from different websites like Fiverr.
Pyautogui : Used to programmatically control the mouse & keyboard.
Pickle : give you the option to save data like(email&pass of WordPress) into file.dat and use them later without entering it again and again
pyinstaller : make you able to convert your script.py to app.exe (work on any windows without IDLE).
