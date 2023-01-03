from flask import Flask, render_template
import requests

app = Flask(__name__)

# def hello_world():

#     prefix_google = """
#     <!-- Google tag (gtag.js) -->
#     <script async
#     src="https://www.googletagmanager.com/gtag/js?id=G-YBSGVH69GD"></script>
#     <script>
#     window.dataLayer = window.dataLayer || [];
#     function gtag(){dataLayer.push(arguments);}
#     gtag('js', new Date());
#     gtag('config', 'G-YBSGVH69GD');
#     </script>
#     """
#     return prefix_google + "Hello World"


# @app.route('/text/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/logger/', methods = ["GET"])
def logger():
    return render_template('logger.html')

@app.route('/cookies/', methods = ["GET"])
def req():
    #req = requests.get("https://www.google.com/")
    req = requests.get("https://analytics.google.com/analytics/web/#/p344247817/reports/reportinghub?params=_u..nav%3Dmaui")
    
    #return req.cookies.get_dict()
    return req.text


# add a route to print the user input in the console from the textbox
@app.route('/textbox', methods=["POST"])
def text():
    return render_template('text.html')
    
