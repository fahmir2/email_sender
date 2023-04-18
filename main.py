import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Eze Duvied'
email['to'] = 'ezequieldiglesias@gmail.com'
email['subject'] = 'A nigerian prince needs you'

email.set_content(html.substitute(name='poronguis'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pypysender@gmail.com', 'aruuehviqvmlvtgf')
    smtp.send_message(email)
    print('all good')
