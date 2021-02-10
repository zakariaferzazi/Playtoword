# Libraries
from tkinter import *
from selenium import webdriver
import webbrowser
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import tkinter.font as font


driver = webdriver.Chrome()

#Create sample rooty for our script
root=Tk()
root.title("Bot play store to Wordpress")
root.geometry('400x300')
root.configure(background='#FF9933')
#we will put our link of wordpress site and user&modpass in this variable to use it later 
yoursite_login="https://yoursite.com/wp-admin"
yoursite_user="user of wordpresss"
yoursite_pwd="modpass of wordpress"
myFont1 = font.Font(family='Helvetica', size=10, weight='bold')
#here we will create 2 entries for make script ask you for link of categorie play store
link_categorie_playstore=Label(text="Enter the link of play store categorie : ", bg="#FF9933", fg="white")
link_categorie_playstore ["font"] = myFont1
link_categorie_playstore.pack()
link_google_playstore=Entry()
link_google_playstore.pack()

myFont2 = font.Font(family='Helvetica', size=10, weight='bold')

link_categorie_playstore1=Label(text="Enter the secend link of play store categorie : ", bg="#FF9933", fg="white")
link_categorie_playstore1 ["font"] = myFont2
link_categorie_playstore1.pack()
link_google_playstore1=Entry()
link_google_playstore1.pack()
#here we will create Function and write all code inside it because we need it to do all task in one click  

def my_machine():
    page_play_store=link_google_playstore.get()
    page_play_store1=link_google_playstore1.get()
    # go to url of categorie play store and get links of items (apps)
    # we will try to find two xpath (with handling problems)
    driver.get(page_play_store)
    try:
        ap1 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[1]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[2]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap3 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[3]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap4 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[4]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap5 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[5]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap6 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[6]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap7 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[7]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap8 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[8]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap9 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[9]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap10 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[10]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap11 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[11]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap12 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[12]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap13 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[13]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap14 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[14]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap15 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[15]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap16 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[16]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap17 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[17]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap18 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[18]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap19 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[19]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    try:
        ap20 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[20]/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    # here we will try with the other xpath

    try:
        app1 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[2]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app3 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app4 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[4]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app5 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[5]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app6 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[6]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app7 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[7]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app8 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[8]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app9 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[9]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app10 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[10]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app11 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[11]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app12 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[12]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app13 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[13]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app14 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[14]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app15 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[15]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app16 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[16]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app17 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[17]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app18 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[18]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app19 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[19]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app20 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[20]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass
    # now we will try to login on wordpress

    driver.get(yoursite_login)
    login1 = driver.find_element_by_id("user_login").send_keys(yoursite_user)
    login2 = driver.find_element_by_id("user_pass").send_keys(yoursite_pwd)
    login_submit = driver.find_element_by_id("wp-submit").click()
    time.sleep(5)
    # now we will go to extract link to pu link of item in google play
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap1)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap2)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap3)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap4)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap5)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap6)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap7)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap8)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap9)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap10)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap11)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap12)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap13)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap14)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap15)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap16)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap17)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap18)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap19)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap20)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    # here we will try to put the other xpath
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app1)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app2)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app3)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app4)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app5)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app6)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app7)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app8)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app9)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app10)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app11)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app12)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app13)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app14)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app15)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app16)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app17)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app18)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app19)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app20)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass



    #now we will try with secend link

    driver.get(page_play_store1)
    try:
        ap1 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[1]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap2 = driver.find_element_by_xpath( "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[2]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[3]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap3 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[4]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap5 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[5]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap6 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[6]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap7 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[7]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap8 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[8]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap9 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[9]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap10 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[10]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap11 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[11]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap12 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[12]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap13 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[13]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap14 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[14]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap15 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[15]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap16 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[16]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap17 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[17]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap18 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[18]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap19 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[19]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    try:
        ap20 = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/c-wiz[20]/div/div/div[1]/div/div/a").get_attribute("href")
    except:
        pass
    # here we will try with the other xpath

    try:
        app1 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app2 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[2]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app3 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app4 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[4]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app5 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[5]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app6 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[6]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app7 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[7]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app8 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[8]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app9 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[9]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app10 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[10]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app11 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[11]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app12 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[12]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app13 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[13]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app14 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[14]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app15 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[15]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app16 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[16]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app17 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[17]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app18 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[18]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app19 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[19]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    try:
        app20 = driver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/c-wiz/div/c-wiz/div/c-wiz/c-wiz/c-wiz/div/div[2]/div[20]/c-wiz/div/div/div[1]/div/div/a").get_attribute(
            "href")
    except:
        pass

    time.sleep(5)
    # now we will go to extract link to pu link of item in google play
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap1)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap2)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap3)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap4)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap5)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap6)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap7)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap8)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap9)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap10)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap11)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap12)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap13)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap14)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap15)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap16)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap17)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap18)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap19)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(ap20)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    # here we will try to put the other xpath
    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app1)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app2)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app3)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app4)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app5)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app6)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app7)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app8)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app9)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app10)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app11)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app12)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app13)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app14)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app15)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app16)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app17)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app18)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app19)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass

    try:
        driver.get("https://yoursite.com/wp-admin/admin.php?page=appyn_extraer_contenido_gp")
        extract_url = driver.find_element_by_id("url_googleplay").send_keys(app20)
        time.sleep(5)
        button_create = driver.find_element_by_id("extraer").click()
        time.sleep(12)
    except:
        pass
    driver.close()




# this part is about copyright, you can put the link of your Instagram or your website, I was put my Instagram

def callback(url):
    webbrowser.open_new(url)
myWidget = Label(root, text="Powered by @Zakaria_0.75")
myWidget.pack(side="bottom")
myWidget.bind("<Button-1>", lambda e: callback("https://www.instagram.com/zakaria_0.75/"))
#here we create font variable because we need it on button
myFont = font.Font(family='Helvetica', size=15, weight='bold')

#here we setup button (click button -> start bot)
button = Button(text = "Start",command=my_machine, bg="#00cc99", fg="white", height=2, width=10)
button ['font'] = myFont
button.pack(pady=5)


root.mainloop()
#The end, See you in the next code