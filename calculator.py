from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('calculator.html')


@app.route('/result', methods=['POST'])
def result():
    firstnumber = request.form.get("firstnumber", type=int)
    secnumber = request.form.get("secnumber", type=int)
    option = request.form.get("option")
    if(option == 'Add'):
        result = firstnumber + secnumber
    elif(option == 'Sub'):
        result = firstnumber - secnumber
    elif(option == 'Mult'):
        result = firstnumber * secnumber
    elif(option == 'div'):
        result = firstnumber / secnumber
    else:
        result = 'INVALID CHOICE'
    entry = {'result': result}
    return render_template('result.html', entry=entry)
if __name__ == '__main__':
    app.run(debug=True)
