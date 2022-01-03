# Baidod Librarys / المكاتب
import smtplib
import time
import config

# open Baidod File / ملف الايميلز
files = open('email.txt', 'r')
Baidodmail = files.readlines()

# Baidod Config / الكوننفج

email = config.email
password = config.password
message = input("Enter Message: ")
message_relode = int(input("How many message you want to send:"))

num = 0
for Baidodmaili in Baidodmail:
    for x in range(0, message_relode):
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,Baidodmaili,message)
        num += 1
        print("message sent to {}[{}]".format(Baidodmaili, num))
    time.sleep(1)

mail.close()
files.close()

print("Done")
