import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sarangthemmarchoni@gmail.com", "01Feb@1998")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sarangthemmarchoni@gmail.com", "sarangthemm4@gmail.com", message)

# terminating the session
s.quit()
