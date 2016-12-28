'''
Creator - Oksana Sakhniuk, 12/27/2016
The source code is the website blocker that runs in the back and blocks facebook page during working hours
During fun hours, the program accesses the hosts file and deletes facebook's restrictions by overwriting file
with the lines that the file had before modification. 

'''
import time
from datetime import datetime as dt

hosts_path="/etc/hosts_copy"
redirect='127.0.0.1'
website_list=['facebook.com','www.facebook.com']

while True:
    if dt.now() > dt(dt.now().year, dt.now().month, dt.now().day,9 ) and dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17,30):
        print('Working hours')
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print('Fun hours')

    time.sleep(5)
