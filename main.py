import os
from flask import Flask, render_template, request, jsonify
from model import *
from logging import exception

app = Flask(__name__)
# Set the path of our SQLAlquemy db
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////home/PycharmProjects/flask_test/coink.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/add_user', methods=['POST'])
def add_user():
    try:
        db_create = Connection_db()
        db_create.create_conn()
        #   We capture the information from our form
        user_name = request.form["full_name"]
        user_email = request.form["email"]
        user_city = request.form["ls_city"]

        db_create.add_records(user_name, user_email, user_city)

        # Creating the dictionary to show the new register.
        dicc_user = [{"user_full_name": user_name,
                      "user_email": user_email,
                      "user_city": user_city
                      }]

        print(f'diccionario de datos: {dicc_user}')

        # Using jsonify to convert a dictionary in a JSON file response
        return jsonify(dicc_user), 200

    except Exception as e:
        print(f'Error: {e}')

        # Using exception method from logging module to show track of the error
        exception("{SERVER}: Error ->\n")
        return jsonify({"msg": "Ha ocurrido un error en tiempo de ejecución"}), 500


# Method to show the users
@app.route('/api/show_users', methods=["GET"])
def get_user():
    try:
        conn = Connection_db()
        users_list = conn.show_users()

        # We can show the outcome to html code:
        for user in users_list:
            print(f'Lista de usuarios: {users_list}')
            structure_html = f'<h4> Listado de Registros Almacenados. {user}\n</h4>'
        return jsonify(users_list), 200

    except Exception as e:
        exception("{SERVER}: Error ->")
        return jsonify({"msg": "Ha ocurrido un error en tiempo de ejecución"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
