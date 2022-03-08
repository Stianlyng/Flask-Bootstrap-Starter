from flask import Flask, render_template




# Flask configuration
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/heroes')
def heroes():
    return render_template('heroes.html')

@app.route('/navbars')
def navbars():
    return render_template('navbars.html')

@app.route('/footers')
def footers():
    return render_template('footers.html')

@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run()
