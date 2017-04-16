from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    a = "\u5934\u6761\u5973\u795e \u5782\u9493\u7f8e\u4eba \u6a0a\u5b89\u59ae"
    print a.encode("UTF-8");
    return a;#render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)