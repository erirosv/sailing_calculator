from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    start_time = request.form['start_time']
    end_time = request.form['end_time']
    normal = float(request.form['normal_setup'])  
    faster = float(request.form['extra'])  

    seconds = get_seconds(start_time, end_time)
    normal_time = calculate_SRS(seconds, normal)
    fast_time = calculate_SRS(seconds, faster)
    
    result = f"Normal: {normal_time:.2f}\tFast: {fast_time:.2f}"

    return render_template('index.html', result=result)

def get_seconds(start_time, end_time):
    try:
        start_time = datetime.strptime(start_time, "%H:%M:%S")
        end_time = datetime.strptime(end_time, "%H:%M:%S")
        time_difference = end_time - start_time
        time_difference_seconds = time_difference.total_seconds()
        return time_difference_seconds

    except ValueError:
        print('Error: convertion error')

def calculate_SRS(seconds, param):
    return (seconds * param) / 3600

if __name__ == '__main__':
    app.run(debug=True)
