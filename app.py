from flask import Flask,request,Response,render_template
import pandas as pd
import json
app = Flask(__name__)


@app.route('/getcountry', methods = ['GET'])
def getcountry():
    country = request.args.get('country')
    df = pd.read_csv('covid_countries.csv')
    df['location']=df['location'].str.lower()
    f = df[(df.values == country.lower())]
    # print(f.size)
    if f.size<1:
        return Response('Empty')

    f =json.dumps(f.to_dict('r')[0])
    resp = Response(f)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/')
def home():
    return render_template('country_map.html')

if __name__ == '__main__':
    app.run()
