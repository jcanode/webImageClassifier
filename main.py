from flask import Flask
from flask import request
from flask import render_template
from flask import json
# import form
import json
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SubmitForm(FlaskForm):
    url = StringField('Url')
    submit = StringField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'temp_secret_key'

# class SubmitForm(FlaskForm):
#     url = StringField('Url')
#     submit = StringField('submit')

@app.route('/')
def template():
    form = SubmitForm()
    return render_template('index.html', form=form)

@app.route('/test', methods=['GET', 'POST'] )
def submit():
    if request.method == 'POST':
        data = request.form['submit']
        jdata = {'url':data}
        with open('data.json', 'w') as outfile:
            json.dump(jdata, outfile)

        r = requests.post('http://localhost:8888', data=jdata)

        print(r.content)
        return render_template("data.html", url=data, classes=r.content)
    else:
        return "<a href='/'>login </a>"
