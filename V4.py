#Elvar Halldór Hróarr Sigurðsson
#10.09.18
#Verkefni4
from sys import argv
from bottle import*
import urllib.request, json

"""
with open("Gengi.json","r") as skra:
    gogn=json.load(skra)

print(gogn)
"""

@route("/")
def index():
    return """
    <h2>Verkefni 4</h2>
    <p><a href="/a">Local Json</a></p>
    <p><a href="/b">Json API</a></p>
    """

#template dæmi 1 - json
@route("/a")
def index():
    return template("index.tpl")

with urllib.request.urlopen("http://apis.is/currency/") as url:
    data = json.loads(url.read().decode())

@route("/b")
def index():
    return template("index2.tpl", data=data)


#########################################################
@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

@error(404)
def villa(error):
    return "<h1 style = color:red>Þessi síða finnst ekki</h1>"

#run(host="localhost", port=8080, debug=True)
run(host='0.0.0.0', port=os.environ.get('PORT'))
