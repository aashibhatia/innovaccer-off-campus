import smtplib
import reminder

tv_series_status = reminder.start()

MY_ADDRESS = 'harshit.codepy@gmail.com'
PASSWORD = 'password'

sender = 'admin@innovaccer.com'
receiver = 'harshit.codepy@gmail.com'

name = reminder.get_series()
messages = []
j = 0

for i in range(0, len(tv_series_status)):
    message = name[i] + ': ' + tv_series_status[i]
    messages.append(message)

server = smtplib.SMTP(host='localhost', port='1025')

for k in range(0, len(messages)):
    server.sendmail(sender, receiver, messages[k])

print("Successfully sent email")
server.quit()
