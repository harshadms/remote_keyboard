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

@app.route('/media', methods=['GET'])
def media():
    return render_template('media.html')

@app.route('/test_keyboard', methods=['GET'])
def test_keyboard():
    return render_template('test_keyboard.html')

#background process happening without any refreshing
@app.route('/general_control/<key>', methods=['GET'])
def genera_control(key):
    if 'rx_string' not in session:
        session['rx_string'] = ''
        
    if 'upper' not in session:
        session['upper'] = False
        
    if key == 'space':
        key = Key.space
        
    elif key == "shift":
        session['upper'] = not session['upper']
        key = ''

    elif key == "bck_space":
        #keyboard.press(Key.backspace)
        session['rx_string'] = session['rx_string'][:-1]
        key = Key.backspace
    
    elif key == "enter":
        print (session['rx_string'])
        session['rx_string'] = ""
        key = Key.enter

    elif key == "esc":
        key = Key.esc

    else:
        if session['upper']:
            key = key.upper()
            session['upper'] = False
    
    keyboard.press(key)
    session['rx_string'] = session['rx_string'] + key
    return ("nothing")

#background process happening without any refreshing
@app.route('/media_control/<key>', methods=['GET'])
def media_control(key):
    print (key)
    #session['rx_string'] = session['rx_string'] + key
    return ("nothing")

#background process happening without any refreshing
@app.route('/test_keyboard_ctrl/<key>', methods=['GET'])
def test_keyboard_ctrl(key):
    print (key)
    if 'rx_string' not in session:
        session['rx_string'] = ''

    if key == "Enter":
        print (session['rx_string'])
        session['rx_string'] = ""
    else:
        session['rx_string'] = session['rx_string'] + key

    return ("nothing")


app.run(debug=True, ssl_context='adhoc')