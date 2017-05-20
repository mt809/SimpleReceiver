from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    b = str((dict(request.form).items())[0][0])
    e = b.split(" ")
    a = e[1:]
    print(b)
    print(e)
    print(a)
    return "Received"

if __name__ == "__main__":
    app.run(host="172.20.10.4", debug=True)