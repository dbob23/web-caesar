from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        </body>
            <form action="/rotate" method="post">
                <label for="rotate-by">
                    Rotate by:
                    <input type="text" id="rot" name="rot" value="0"/>
                </label>
                <label for="/text" method="post">
                    <textarea id="text" name="text"/>
                    </textarea>
                </label>
                <input type="submit" value="Submit Query"/>

        </body>
    </html>

    """

@app.route("/", methods=['POST'])
def encrypt():
    rot_element = int(rot)
    text_element = text
    encrypted_element = rotate_string(text_element)

    return "<h1>" + encrypted_element + "</h1>"

@app.route("/")
def index():
    return form

app.run()

