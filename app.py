import requests
import os
from flask import Flask, render_template, request, url_for, make_response, redirect
from wtforms import Form, RadioField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.utils import secure_filename
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/faam')
def faam():
    return render_template('faam.html')

@app.route('/ases')
def ases():
    return render_template('ases.html')


@app.route('/koos')
def koos():
    return render_template('koos.html')

@app.route('/ikdc')
def ikdc():
    return render_template('ikdc.html')


#########404######
@app.errorhandler(404)
def page_not_found(e):
    # Отображение шаблона страницы 404
    return render_template('error.html'), 404

####################Отправка формы в телеграм##########################

bot_token = "5875182826:AAHa3bIyWDRob_3tyDmfnZ2qpQXemaYHH4I"
chat_id = "-929458358"


##########################################Контакты 


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/contacts', methods=['POST'])
def send_message():
    # Получаем данные из формы
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    file = request.files['file']

    # Отправляем сообщение в телеграм-бота
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": f"Новое сообщение:\n\nИмя: {name}\nПочта: {email}\nСообщение: {message}"}
    requests.post(url, data=data)

    # Отправляем файл в телеграм-бота
    if file:
        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        files = {"document": (file.filename, file.read())}
        data = {"chat_id": chat_id}
        requests.post(url, data=data, files=files)

    return render_template('success.html')
##########################################################################

######################### Glenoid Track Calculator

##############################################################




if __name__ == "__main__":
    app.run(debug=True)