from flask import Flask, flash

# create application
app = Flask(__name__)

# define root route
@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)