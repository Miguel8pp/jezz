from flask import Flask, render_template

app = Flask(__name__)

# Ruta para /alana
@app.route('/alana')
def alana():
    return render_template('alana.html')

# Ruta para /jezz
@app.route('/')
def jezz():
    return render_template('videos.html')

if __name__ == '__main__':
    app.run(debug=True)
