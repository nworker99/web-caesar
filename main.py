from flask import Flask, request, redirect
from caesar import encrypt
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
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
    <body>
"""

page_footer = """
    </body>
</html>
"""

encrypt_form = """
    <form action="/encrypt" method="post">
        <label>
            Rotate by:
            <input type="text" name="rotation" value="0"/>
        </label>
        <textarea type="text" name="text">
"""

encrypt_form_2 = """
        </textarea>
        <input type="submit" value="Submit"/>
    </form>
"""

@app.route("/encrypt", methods=['POST'])
def rotation():
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''
    
    rotation = request.form['rotation']
    text = request.form['text']
    new_text = encrypt(text, rotation)
    main_content =encrypt_form + new_text + encrypt_form_2 + error_element
    content = page_header + main_content + page_footer

    return content


@app.route("/")
def index():
    error = request.args.get("error")
    if error:
        error_esc = cgi.escape(error, quote=True)
        error_element = '<p class="error">' + error_esc + '</p>'
    else:
        error_element = ''
    main_content =encrypt_form + encrypt_form_2 + error_element
    content = page_header + main_content + page_footer

    return content

app.run()
