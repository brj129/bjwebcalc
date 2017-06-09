from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"

@app.route('/<int:a>/<op>/<int:b>')
def calc(a, op, b):
    operation = mongo.db.operations.find_one({'name': op})
    if operation:
        return Template(operation['pattern']).render(a=a, b=b)
    elif op == '+':
        return f"Result: {a} {op} {b} = {a + b}"
    else:
        return f"Result: {a} {op} {b} = ???"
    return f"Result: {a} {op} {b} = {a + b}"


if __name__ == '__main__':
    app.run(debug=True)
