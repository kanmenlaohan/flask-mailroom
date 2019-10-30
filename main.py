import os
import base64
from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor
from time_api import time
from piglatin import get_fact, pig_latin_translation


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/')
def home():
    return redirect(url_for('utc_time'))

@app.route('/time')
def utc_time():
    utc_time = time()
    # return render_template('time.html', time=utc_time)
    return render_template('local_time.jinja2', time=utc_time)

@app.route('/piglatin')
def piglatin():
    url = pig_latin_translation()

    return render_template('piglatin.jinja2', url=url)

@app.route('/donations')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/donate', methods=['GET', 'POST'])
def donate():
# make a donation and redirect to donor page
    if request.method == 'POST':
        donor = Donor(name=request.form['name'])
        donor.save()

        amount = Donation(donor=donor, value=request.form['amount'])
        amount.save()
        
        return redirect(url_for('all'))
    else:
        return render_template('donate.jinja2', donations=Donation.select())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='172.16.68.3', port=port, debug=True)

