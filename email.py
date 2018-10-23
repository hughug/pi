#!/usr/bin/python
# -*- coding: utf-8 -*-
# this program sends emails to target address

import smtplib

def mailing(subject, content, target):
    
    # the message content
    sub  = 'Subject: %s'%subject
    cont = '%s'%content
    end  = "Best,\nPi"
    message = sub + '\n' + content + '\n\n' + end

    # send the email using smtp service
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('mumeiprpr@gmail.com','wyylovecby')
    smtp.sendmail('mumeiprpr@gmail.com','%s'%target, message)
    smtp.quit()

#mailing("hello", "are you okay", "cbywyy@gmail.com")