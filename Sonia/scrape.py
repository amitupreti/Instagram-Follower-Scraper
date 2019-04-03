from time import sleep
from datetime import datetime
import sys
import os
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import pandas as pd
import ipdb




def display(message_type,message):
    print('0'*100)
    print(message_type+'::'+message)
    print('0'*100)


def main():
    filename = str(datetime.now().strftime(r'%d-%m-%Y::%H-%M'))+'.csv'

    with open(filename,'w',newline='') as csvf:
        csv_writer = csv.writer(csvf)
        csv_writer.writerow(['hotel_name','check_in','check_out','no_of_rooms','guests','adults','children','room_type','occupancy','bed_choices','room_photo','cancellation','options','price'])


    #reading input files for settings of hotels
    hotels = pd.read_excel('Input.xlsx')
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    for i  in range(len(hotels)):

        hotel_url  = hotels['Hotel URL'].iloc[i]
        hotel_name  = hotels['Hotel Name'].iloc[i]
        check_in  = hotels['Check In'].iloc[i]
        check_out  = hotels['Check Out'].iloc[i]
        rooms  = hotels['Rooms'].iloc[i]
        adults  = hotels['Adults'].iloc[i]
        children  = hotels['Children'].iloc[i]
        end_date  = hotels['End-Date'].iloc[i]
        child_age = hotels['Children Age'].iloc[i]
        os.system('clear')
        display('Message','\n'+str(i+1)+' Working on {name}'.format(name = hotel_name))


        if children>3:
            display('Warning',"Max 3 children allowed.\nSetting the number of children to 3")
            children=3
        if adults>8:
            display('Warning',"Max 8 Adults allowed.\nSetting the number of Adults to 8")
        if child_age>17:
            display('Warning',"Max 17 years old Children is allowed.\nSetting the Age of Child to 17")

        start_scrape = Hotels()
        # print(hotel_name)
        current_time = datetime.now()
        if current_time > end_date:
            display('Message','The End date has passed for {hotel_name}.So i am skipping it. Please check the ExpiredHotels.csv file for the  expired hotel date.\nYou might need to edit the Input file'.format(hotel_name=hotel_name))
            with open('ExpiredHotels.csv','a') as f:
                f.write(hotel_url+','+str(end_date)+'\n')

        else:
            driver,decide = start_scrape.activate_search(hotel_url, check_in, check_out, rooms, adults, children, child_age, driver)
            if decide==1:
                driver = start_scrape.get_data(driver,check_in, check_out, rooms, adults, children,filename)
 


class Hotels:

    def activate_search(self, hotel_url,check_in,check_out, rooms, adults, children, child_age, driver):
        '''This function will visit the hotel urls and enter the search criteria as 
        kept in input file.'''
      
        driver.get(hotel_url)
        # ipdb.set_trace()

        #clearing input filed of check in
        driver.find_element_by_xpath('//*[@id="totpq-localised-check-in"]').clear() 
        # driver.find_element_by_xpath('//*[@id="totpq-localised-check-in"]').clear() 
        #sending the time input for checkin
        print(check_in.strftime(r'%d-%m-%Y'))
        driver.find_element_by_xpath('//*[@id="totpq-localised-check-in"]').send_keys(check_in.strftime(r'%d-%m-%Y')) 

         #clearing input filed of checkOut
        driver.find_element_by_xpath('//*[@id="totpq-localised-check-out"]').clear() 
        # driver.find_element_by_xpath('//*[@id="totpq-localised-check-out"]').clear() 
        #sending the time input for checkout
        driver.find_element_by_xpath('//*[@id="totpq-localised-check-out"]').send_keys(check_out.strftime(r'%d-%m-%Y')) 
        print(check_out.strftime(r'%d-%m-%Y'))
        input('Skip')

        #sending no of rooms
        driver.find_element_by_id('totpq-rooms').send_keys(str(rooms))
        #sending the no of adults and children for each room

        for i in range(rooms):
            try:
                a  = 'totpq-room-{a}-adults'.format(a=i)
                c =  'totpq-room-{a}-children'.format(a=i)
                driver.find_element_by_id(a).send_keys(str(adults)) #adults
                Select(driver.find_element_by_id(c)).select_by_value(str(children)) #child

                for j in range(children):
                    age = 'totpq-room-{a}-child-{b}-age'.format(a=i,b=j)
                    Select(driver.find_element_by_id(age)).select_by_value(str(child_age)) #child age


                # ipdb.set_trace()


            except Exception as e:
                print(e)
                # display('Error','Couldn\'t add adults to room')


        # ipdb.set_trace()
        #submitting search criteria
        driver.find_element_by_xpath('//*[@role="search"]//button[@type="submit"]').click()    
        check_availiability_xpath =  '//*[@class="hotel sold-out pinned-unavailable"]//h2'
        try:    
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH,check_availiability_xpath)))
            
            if len(driver.find_element_by_xpath(check_availiability_xpath).text)>10:
                print('Warning','No booking availiable for following search criteria')
                return driver,0
        
        except:
            display('Message','Booking Found')

        # ipdb.set_trace()

       
        return driver,1


    def get_data(self,driver,check_in, check_out, rooms, adults, children, filename):
        '''it will get all the fields needed to be scraped from each hotels'''
        
        hotel_name =  driver.find_element_by_xpath('//h1').text  
        check_in = check_in.strftime(r'%d-%m-%Y')
        check_out = check_out.strftime(r'%d-%m-%Y')
        no_of_rooms = rooms
        guests = (adults+children)*no_of_rooms
        # amenties = driver.find_elements_by_xpath('//*[@class="amenity-icons"]')[0].text.split('\n')   
        # postal_address =  driver.find_element_by_xpath('//*[@class="postal-addr"]').text
        # rating = driver.find_element_by_xpath('//*[@class="rating"]').text 

        #getting the main data about room
        room_types  = driver.find_elements_by_xpath('//*[@class="room-info"]//h3')

        for i in range(len(room_types)):
            room_type = room_types[i].text

            #######################################
            #change occupancy to room-and-hotel-info
            occupancy  =  driver.find_elements_by_xpath('//*[@class="room-info"]//*[@class="occupancy"]')[i].text  
            ############################################
            bed_choices = driver.find_elements_by_xpath('//*[@class="room-info"]//ul')[i].text
            room_photo = driver.find_elements_by_xpath('//*[@class="room-info"]//*[@class="room-image"]//img')[i].get_attribute('src')         
            
            rate_plans = driver.find_elements_by_xpath('//*[@class="rooms"]/li[{}]//*[@class="rateplan"]'.format(i+1)) 

            # ipdb.set_trace()
            for j in range(len(rate_plans)):
                cancellation = driver.find_elements_by_xpath('//*[@class="rooms"]/li[{}]//*[@class="rateplan"]//*[@class="cancellation"]'.format(i+1))[j].text.replace('\n',' ') 

                # cancellation = (driver.find_elements_by_xpath('//*[@class="rateplan"]//*[@class="cancellation"]')[j].text).replace('\n',' ') 

                options = driver.find_elements_by_xpath('//*[@class="rooms"]/li[{}]//*[@class="rateplan"]//*[@class="options"]'.format(i+1))[j].text
                # options = driver.find_elements_by_xpath('//*[@class="rateplan"]//*[@class="options"]')[j].text

                price = driver.find_elements_by_xpath('//*[@class="rooms"]/li[{}]//*[@class="rateplan"]//*[@class="price"]'.format(i+1))[j].text
                # price = driver.find_elements_by_xpath('//*[@class="rateplan"]//*[@class="pricing"]//*[@class="price"]')[j].text      



                with open(filename,'a',newline='') as csvf:
                    csv_writer = csv.writer(csvf)
                    csv_writer.writerow([hotel_name,check_in,check_out,no_of_rooms,guests,adults,children,room_type,occupancy,bed_choices,room_photo,cancellation,options,price])
            
                print([hotel_name,check_in,check_out,no_of_rooms,guests,adults,children,room_type,occupancy,bed_choices,room_photo,cancellation,options,price])

        return driver
main()