from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE'] = 0
app.config['SECRET-KEY'] = 'heresymarxismfailture'

@app.route('/')
def library():
    return render_template('library.html')