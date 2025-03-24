from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # Listen on all network interfaces so Docker can expose it
    app.run(host='0.0.0.0', port=5000, debug=True)
