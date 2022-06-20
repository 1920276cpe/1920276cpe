from flask import Flask, render_template, request
import webbrowser
from importlib import reload
from threading import Thread

app = Flask(__name__)
abstract_imported, ch11_12_imported, ch13_imported, inheritance_imported, pos_imported = False, False, False, False, False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/exercises/abstract')
def abstract():
    global abstract_imported
    from static.abstract import employee
    #from static.abstract import fulltimeemployee
    #from static.abstract import hourlyemployee
    from static.abstract import payroll
    if abstract_imported:
        reload(employee)
        #reload(fulltimeemployee)
        #reload(hourlyemployee)
        reload(payroll)
    abstract_imported = True
    return render_template('abstract.html')

@app.route('/exercises/ch11_12')
def ch11_12():
    global ch11_12_imported
    from static.ch11_12 import main
    if ch11_12_imported:
        reload(main)
    ch11_12_imported = True
    return render_template('ch11_12.html')

@app.route('/exercises/ch13')
def ch13():
    global ch13_imported
    from static.ch13 import main
    if ch13_imported:
        reload(main)
    ch13_imported = True
    return render_template('ch13.html')

@app.route('/exercises/inheritance')
def inheritance():
    global inheritance_imported
    from static.inheritance import main
    if inheritance_imported:
        reload(main)
    inheritance_imported = True
    return render_template('inheritance.html')

@app.route('/exercises/pos')
def pos():
    global pos_imported
    from static.pos import pos
    if pos_imported:
        reload(pos)
    pos_imported = True
    return render_template('pos.html')

@app.route('/about')
def about():
    return render_template('about.html')

def run_app():
    app.run()

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

first_thread = Thread(target=run_app)
second_thread = Thread(target=open_browser)

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()