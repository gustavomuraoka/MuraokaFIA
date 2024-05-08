from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/RI", methods=['GET', 'POST'])
def RI():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="RI",
        )

        nome = request.form['nome']
        email = request.form['email']

        print(nome, email)

        mycursor = mydb.cursor()

        sql = f'INSERT INTO Usuario (user_nome, user_email) VALUES ({nome}, {email})'
        mycursor.execute(sql)

        mydb.commit()

        return render_template("RI.html")

    return render_template("RI.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)