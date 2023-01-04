from flask import Flask, render_template , url_for


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YBSGVH69GD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YBSGVH69GD');
</script>
<a href="/trend">Google Trend</a><br>
<a href="/counter">Counter</a><br>
<a href="/time-execution">Log Time Execution</a><br>
 """
    return prefix_google

###########################         Google trend        #############################################""

from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

@app.route('/trend', methods=["GET"])
def trend():

    pytrends = TrendReq(hl='en-US', tz=360)

    kw_list=['France','England']
    pytrends.build_payload(kw_list, timeframe='2022-01-09 2023-01-01', geo='US')
    df = pytrends.interest_over_time()
    france_data = df['France'].values.tolist()
    england_data = df['England'].values.tolist()
    dates = [datetime.fromtimestamp(int(date/1e9)).date().isoformat() for date in df.index.values.tolist()]

    params = {
        "type": 'line',
            "data": {
                "labels": dates,
                "datasets": [{
                    "label": 'France',
                    "data": france_data,
                    "borderColor": '#3e95cd',
                    "fill": 'false',
                },
                {
                    "label": 'England',
                    "data": england_data,
                    "borderColor": '#ffce56',
                    "fill": 'false',
                }
                ]
            },
            "options": {
                "title": {
                    "text": 'My Line Chart'
                },
                "scales": {
                    "yAxes": [{
                        "ticks": {
                            "beginAtZero": 'true'
                        }
                    }]
                }
            }
    }
    
    
    
    prefix_google = """

    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>

    <canvas id="myChart" width="50" height="50"></canvas>""" + f"""
    <script>
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {params});
    </script>

    """

    return prefix_google



###########################        Timer Log        #############################################""

import time
from collections import Counter

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@app.route('/counter')
@log_execution_time
def counter():
    # Download Shakespear artwork
    """
    for i in range(1):
        start_time = time.time()
        with open('shakespeare.txt', 'r') as f:
            text = f.read()
        word_count_dict = count_words_dict(text)
        start_time_2 = time.time()
        word_count_counter = count_words_counter(text)
        print(word_count_dict)
        print(word_count_counter) """
        
        #f"{word_count_dict}<br><br><br>     {word_count_counter}"
    return render_template('counter.html')#"Counting time Counter"+"   "+f"  {(time.time() - start_time_2)}"+"Counting time dictionnary"+"   "+f"{(start_time_2 - start_time)}"

def count_words_dict(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def count_words_counter(text):
    return Counter(text.split())



if __name__ == '__main__':
    app.run()