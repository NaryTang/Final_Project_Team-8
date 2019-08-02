from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/data')
def data():
    return render_template("data.html")

@app.route('/route_name', methods=['GET', 'POST'])
def method_name():
   pass

if __name__ == '__main__':
    app.run()