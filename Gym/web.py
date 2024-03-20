from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('webwelcome.html')

# @app.route('/table', methods=['get'])
# def table():
#     name=request.args.get('name')
#     email=request.args.get('email')
#     phone=request.args.get('phone')
#     date=request.args.get('date')
#     return render_template('table.html',name=name,mail=email,phone=phone,date=date)
@app.route('/web')
def web():
    return render_template('web.html')
@app.route('/table', methods=['POST'])
def table():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    date=request.form['date']
    return render_template('table.html',name=name,mail=email,phone=phone,date=date)

@app.route('/webclass')
def webclass():
    return render_template('webclass.html')

if __name__=='__main__':
    app.run(debug=True)