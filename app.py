from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template("home.html")


@app.route("/getData", methods=['GET', 'POST'])
def GetData():
    data = request.get_json
    print(data['text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
