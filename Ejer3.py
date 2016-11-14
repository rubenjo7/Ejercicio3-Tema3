from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

#http://flask.pocoo.org/docs/0.11/quickstart/ --> Variable rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port=int(os.environ.get('PORT',2020))
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=port)
