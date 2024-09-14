from flask import Flask, render_template, request, session
from pynput.keyboard import Key, Controller

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'memcache'

keyboard = Controller()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print ("Value 1")
            pass # do something
        elif  request.form.get('action2') == 'VALUE2':
            print ("Value 2")
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/background_process_test/<key>', methods=['GET'])
def background_process_test(key):
    if 'rx_string' not in session:
        session['rx_string'] = ''
        
    if 'upper' not in session:
        session['upper'] = False
        
    if key == 'space':
        keyboard.press(Key.space)
        key = " "
        
    elif key == "shift":
        session['upper'] = not session['upper']
        key = ''
    elif key == "bck_space":
        keyboard.press(Key.backspace)
        session['rx_string'] = session['rx_string'][:-1]
        return ("nothing")
    
    elif key == "enter":
        keyboard.press(Key.enter)
        print (session['rx_string'])
        session['rx_string'] = ""
        return ("nothing")
    else:
        if session['upper']:
            key = key.upper()
            session['upper'] = False
            
        keyboard.press(key)
        
    session['rx_string'] = session['rx_string'] + key
    return ("nothing")

app.run(host="192.168.178.26", debug=True, ssl_context='adhoc')