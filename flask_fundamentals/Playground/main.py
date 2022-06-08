from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')         
def hello():
    return 'Hello World!' 

@app.route('/play')
def boxes():
    return render_template('index.html')


@app.route('/play/<num>')
def blue_boxes(num):
    return render_template('index.html', _num=int(num))


@app.route('/play/<num>/<color>')
def boxes_color(num, color):
    return render_template('index.html', _num=int(num), _color=color)


@app.route('/<any>')
def error(any):
    return "Sorry! No response. Try again."


if __name__ == "__main__":  
    app.run(debug=True)  
