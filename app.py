from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)


# importing image in code from web 
@app.route('/imagefinder')
def printing():
    return render_template('newindex.html')

@app.route('/imagefinder',methods=['POST'])
def predict():
    imagefile = request.files['imagefile']  
    image_path= './images/' + imagefile.filename
    imagefile.save(image_path)
    return render_template('newindex.html')


# trial
@app.route('/test')
def tptp():
    return render_template('newindex.html')

@app.route('/test1',methods=['GET'])
def btnfunc():
    
    return render_template('newnewindex.html')

# @app.route("/tptp")
# def home():
    
#     m='hello_world'
#     return redirect(url_for(m))
 

# @app.route('/helloworld')
# def hello_world():
#     return "<p>Hello, World from \
#                 redirected page.!</p>"




# login page
@app.route('/load')
def load():
    return render_template('login.html')

@app.route('/')
def login2():
    return render_template('login2.html')

database={'user':'123'}

@app.route('/formlogin',methods=['GET','POST'])
def login():
    num1=request.form['tp1']
    num2=request.form['tp2']
    x=""
    if num1 not in database:
        x='fail'
        return redirect(url_for(x))
    else:
        if database[num1]!=num2:
            x='failed'
            return redirect(url_for(x))
        else:
            return render_template('login.html')
            
    
@app.route('/failed')
def failed():
    return render_template('failedpass.html')
@app.route('/fail')
def fail():
    return render_template('failed.html')




# result pass/fail

@app.route('/resultfindermid')
def resultinp():
    return render_template('score.html')

@app.route('/resultfinder',methods=['POST','GET'])
def result():
    total=0
    maths=(int)(request.form['maths'])
    daa=(int)(request.form['daa'])
    cn=(int)(request.form['cn'])
    flat=(int)(request.form['flat'])
    uhv=(int)(request.form['uhv'])
    total=(maths+daa+cn+flat+uhv)/5
    if total<=50:
        return render_template('resfailed.html',ans=total)
    else:
        return render_template('respass.html',ans=total)
    


if __name__ == "__main__":
    app.run(debug=True)