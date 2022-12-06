from flask import Flask
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG)
app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-YBSGVH69GD"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-YBSGVH69GD');
</script>
 """
 return prefix_google + "Hello World"

@app.route('/logger', methods=["GET"])
def hello_world2():
    print("I'm a logger")
    #app.logger.debug("Debug log level")
    return "I'm a logger"
if __name__ == '__main__':
  app.run(debug=True)