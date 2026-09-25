from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def say_hello():
    return f'''
        <p>Hello, World, I am a Flask app!</p>
        <a href="{url_for('about')}">About</a> |
        <a href="{url_for('contact')}">Contact</a>
    '''

@app.route('/contact')
def contact():
    return '''
        <p>Email me at: <a href="mailto:c24405302@mytudublin.ie">c24405302@mytudublin.ie</a></p>
        <a href="/">Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)