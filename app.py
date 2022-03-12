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

@app.route('/sidebars')
def sidebars():
    return render_template('sidebars.html')

@app.route('/dropdowns')
def dropdowns():
    return render_template('dropdowns.html')

@app.route('/components')
def components():
    return render_template('components.html')

if __name__ == '__main__':
    app.run()
