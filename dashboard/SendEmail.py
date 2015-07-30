import smtplib

fromaddr = 'czhou@bentonow.com'
toaddrs  = 'jason@bentonow.com'
msg = 'Automatic email test'


# Credentials (if needed)
username = 'czhou@bentonow.com'
password = 'Roger9218'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
