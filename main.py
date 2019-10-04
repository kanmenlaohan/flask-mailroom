import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

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

