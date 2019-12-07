from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/<int:n>')
def index(n):
    n_menos_2 = 0
    n_menos_1 = 0
    actual = 1
    for i in range(1,n):
        n_menos_2 = n_menos_1
        n_menos_1 = actual
        actual = n_menos_1 + n_menos_2
    return str(actual)

if __name__ == "__main__":
    app.run(debug=True)