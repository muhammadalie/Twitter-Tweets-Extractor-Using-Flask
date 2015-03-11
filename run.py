#!flask/bin/python
import sqlite3
from flask import Flask
from flask.ext.login import LoginManager
app= Flask(__name__)
app.config.from_object('config')
from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required,user_logged_in
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField, validators,TextField,TextAreaField,IntegerField
from wtforms.validators import DataRequired
import requests
import json
import twitter
import oauth2 as oauth,json
def oauth_req(url, key='597987159-cX3oqo8rGFVC0i1WZZuN8hI0qKXjcAQBZlE66un7', secret='7idwwQzFB1TqRmKBcTSFwW79BGKMkykb6c2oT1s2GLWoN', http_method="GET", post_body=None, http_headers=None):
    consumer = oauth.Consumer(key='GcPPtjWQoHZiLWTpMQa3z44Es', secret='JJo4VbMBKJ6J9FdSl6x10tpGWGh2mEBjc1NzHXxDWCNo3mhILz')
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request( url)
    return content
class URLForm(Form):
	url = StringField('url', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
	form= URLForm()
	r=[]
	if form.validate_on_submit():
		name=form.url.data
		a= oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+name+'&count=10')
		r=json.loads(a)
			
	return render_template('home.html',form=form,r=r)

app.run(debug=True)
