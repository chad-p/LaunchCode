from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rotate">Rotate by: </label>
            <input type="text" name="rotate" value="0">
            <br>
            <textarea name="text" value="">{text}</textarea>
            <br>
            <input type="submit" name="rot" value="Submit Query">
        </form>
    </body>
</html>
"""


@app.route("/", methods=['GET'])
def index():
    return form.format(text='')


@app.route("/", methods=['POST'])
def rotate():

    rotation = request.form['rotate']
    text = request.form['text']

    result = encrypt(text, rotation)
    return form.format(text=result)


app.run()
