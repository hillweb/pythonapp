from flask import Flask
app = Flask(__name__)
PORT='20166'
@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("favicon.ico")
    
       
    
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=PORT,debug=True)
