from flask import Flask, render_template, request, redirect
from conn import Connection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/RI", methods=['GET', 'POST'])
def RI():
    if request.method == 'POST':
        
        mydb = Connection.createConn()

        nome = request.form['nome']
        email = request.form['email']

        Connection.insertDB(mydb, nome, email)

        print(nome, email)

        return redirect("/")

    return render_template("RI.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)