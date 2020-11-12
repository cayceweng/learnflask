from flask import Flask, request, render_template, redirect
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = '8913cfecdc87eaf1555f99846ee67db7'
    city = request.args.get('q')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    temperature = response.json()
    weather = temperature["weather"][0]['description']
    return 'Weather:' + weather

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    
    return redirect("http://www.google.com", code=302)



@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')

        return '''<h1>The language value is: {}</h1>
                  <ht>The framework value is: {}</h1>'''.format(language, framework)

    return '''<form method="POST">
                    Language: <input type="text" name="language"><br>
                    Framework: <input type="text" name="framework"><br>
                    <input type="submit" value="Submit"<br>
                </form>'''
    
    
if __name__ == '__main__':
    app.run(debug=True)