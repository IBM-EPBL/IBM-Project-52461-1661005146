from flask import Flask , render_template,request,json
app = Flask(name)

@app.route('/')
def home():
    return  render_template('index.html')
@app.route("/siginin",methods=['POST'])
def sigmin():
     username=request.form['username']
     password =request.form['password']
     if username and password:
        return json.dumps({'validation': validate(username,password)})
     return json.dumps({'validation':False})
