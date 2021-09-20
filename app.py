import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World ... again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
    # set to true because you want to see the actual errors that may appear
    # make sure to udpate this to debug=False prior to actual deployment
