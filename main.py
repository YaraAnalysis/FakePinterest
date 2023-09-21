from flask import Flask, render_template, url_for

# o url_for permite pegar a url de acordo com o nome da função, e não com a rota dele.
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>")
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


if __name__ == "__main__":
    app.run(debug=True)


