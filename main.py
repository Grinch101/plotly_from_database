import plotly.graph_objects as go
import json
import requests

fig = go.Figure()
fig.add_trace(go.Bar(x=[1,2,3],y=[1,2,3]))

jsonvalue = fig.to_json()


# requests.post("https://myblog101.herokuapp.com/", json={"title":"A PLotly Figure","body":jsonvalue})

r = requests.get("https://myblog101.herokuapp.com/getall")

print(json.loads(r.text)['data'][1]['body'])
jdata = json.loads(json.loads(r.text)['data'][1]['body'])

f = go.Figure(data = jdata['data'] , layout=jdata['layout'])


f.show()