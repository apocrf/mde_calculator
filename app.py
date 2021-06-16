from flask import Flask, render_template, request
from validation import InputForm
import pandas as pd
from compute import compute

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.alpha.data, form.beta.data)
        df = pd.read_csv(request.files.get('file'))
    else:
        df = pd.DataFrame()
        result = None
    return render_template("index.html", current_title = 'Custom Title', MDE=df.shape, form = form, result = result)

if __name__ == '__main__':
    app.run(debug=True)
