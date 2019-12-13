from flask import Flask, render_template, flash,request
from wtforms import Form, TextField, TextAreaField, validators, StringField

class ReusableForm(Form):
    consumer_id = TextField('Consumer-ID:')
    consumer_secret = TextField('Consumer-Secret:')

def remove_all_users_for_twitter_account(consumer_id, consumer_secret):
    print('Removing all subscriptions for {}{}'.format(consumer_id,consumer_secret))

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    
    @app.route("/", methods=['GET', 'POST'])
    def index_html():
        form = ReusableForm(request.form)
        if request.method == 'POST':
            consumer_id=request.form['consumer-id']
            consumer_secret=request.form['consumer-secret']

            if form.validate():
                remove_all_users_for_twitter_account(consumer_id, consumer_secret)
                flash('Removed all subscriptions for: {}'.format(consumer_id))

            else:
                flash('Error: All Fields are Required')

        return render_template('index.html', form=form)

    return app


def main():
    app = create_app()
    app.run()

if __name__ == '__main__':
    main()