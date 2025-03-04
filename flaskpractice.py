from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scores', methods=['GET','POST'])
def scores():
    return render_template('scores.html')

@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        math = int(request.form['math'])
        science = int(request.form['science'])
        english = int(request.form['english'])
        score = (math+science+english)/3
        res=""
        mathres="Passed" if math>=50 else "Failed"
        scienceres="Passed" if science>=50 else "Failed"
        englishres="Passed" if english>=50 else "Failed"

        if score>=50:
            res=f"{score}% and Passed"
        else:
            res=f"{score}% and Failed"
        return render_template('result.html', result=res,math=math,science=science,english=english,mathres=mathres,scienceres=scienceres,englishres=englishres)

if __name__=="__main__":
    app.run(debug=True)
