import os

import emails
from emails.template import JinjaTemplate 

from config import Config

CONFIG = Config()

def send_email(template, subject, data_map, recipient):
    template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "email_templates", template)
    print(template_path)

    smtp_config = {
        'host': CONFIG.smtp_host,
        'port': CONFIG.smtp_port,
        'user': CONFIG.smtp_user,
        'password': CONFIG.smtp_pass,
        'ssl': True
    }

    m = emails.Message(html=JinjaTemplate(open(template_path).read()), subject=subject, mail_from=("VulnFeed Agent", "vulnfeed@j2h2.com"))
    response = m.send(render=data_map, to=recipient, smtp=smtp_config)

    if response.status_code == 250:
        return True
    else:
        return False