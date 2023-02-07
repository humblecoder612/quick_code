from flask import Flask, jsonify,render_template, request,redirect
import requests
import json
import time
#run app
app=Flask(__name__)

client_id = ''
client_secret=''
output=['yo']

current='python'

code_list={
    'python': {'language':"python3",'versionIndex': "4",'value':"#Python \n # \u2193 \u2193 Code here \u2193 \u2193"},
    'java': {'language':"java",'versionIndex':"4"},
    'cpp': {'language':"cpp",'versionIndex':"5"},
    'csharp': {'language':"csharp",'versionIndex':"4"},
}

@app.route('/')
def index(): 
    return render_template('index.html',code_option=code_list,current=current)


def coderesult(code):
    program= {"script" : code,
    "language": code_list[current]['language'],
   "versionIndex": code_list[current]['versionIndex'],
    "clientId": client_id,
    "clientSecret":client_secret }
    response=requests.post('https://api.jdoodle.com/v1/execute',headers = {"Content-Type" : "application/json"},json=program)
    return response.json()

@app.route('/getcode', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    res=coderesult(jsdata)
    output[0]=res['output']
    print(output)
    return res['output']

@app.route('/outputcode',methods=['POST'])
def output_code():
    res=output[-1]
    print(res)
    return res

@app.route("/options" , methods=['GET', 'POST'])
def options():
    select = request.form.get('comp_select')
    global current
    current=select
    return render_template('index.html',code_option=code_list,current=current)  

@app.route("/defaultvalue",methods=['Post'])
def def_val():
    global current
    res=code_list[current]['value']
    return res
     

if __name__ == '__main__':
    app.run(debug=True)