from flask import Flask
from flask_mail import Mail, Message

app=Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']='587'
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="_______@gmail.com"
app.config['MAIL_PASSWORD']="imasdsyppcvrbafr"
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USE_TLS'] = True
 
mail = Mail(app)

@app.route("/")
def index():
    msg = Message("its me2",sender = '____@gmail.com', recipients=['_____@gmail.com'])
    
    msg.body = "Hello bro"
    mail.send(msg)
    return "mail send"

if __name__=='__main__':
    app.run(debug = True)
