import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())

smtp_object.starttls()

subject = 'this is a test'
message = 'this is a test'
email = 'java.gdb@gmail.com'

msg = "Subject:" + subject + '\n' + message

print(smtp_object.login(email, 'xxxx'))

smtp_object.sendmail(email, email, msg)

