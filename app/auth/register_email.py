from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import smtplib


def register_email(emp_email, emp_name):
    from_email = "thatikondasaikrishna111@gmail.com"
    from_password = "s@iKRISHNA123456"
    to_email = emp_email

    # msg=MIMEText(message,'html')
    # msg['Subject']=subject
    # msg['To']=to_email
    # msg['From']=from_email

    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Metrixlab, @ Registration Successfully"
    the_msg["From"] = from_email
    the_msg["To"] = to_email

    plain_text = " Testing the message "
    html_text = """\
    <html>
        <head></head>
        <body>
            <div>
                <h1><b> Thanks for registering with us.</b></h1>
                <h3> Your details will be safe and secure with us. Please make sure to update the logout details regularly for better service. 
                <img src="https://cdn.dribbble.com/users/35310/screenshots/2893503/london-black-cab-glyph.png"/>
                <h2> Kind Regards, <br> Metrixlab Inc </h2>
            </div>
        </body>
     </html>
     """

    part_1 = MIMEText(plain_text, 'plain')
    part_2 = MIMEText(html_text, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn = smtplib.SMTP('smtp.gmail.com', 587)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(from_email, from_password)
    email_conn.sendmail(from_email, to_email, the_msg.as_string())
    email_conn.quit()

