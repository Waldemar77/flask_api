from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home/add_user', methods=['POST'])
def add_user():
    try:
        #   We capture the date from our form
        user_name = request.form["full_name"]
        user_email = request.form["email"]
        user_city = request.form["ls_city"]


    except Exception as e:
        pass


if __name__ == '__main__':
    app.run(debug=True)
