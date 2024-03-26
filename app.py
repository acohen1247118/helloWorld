from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Alexander Cohen! This is my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')
@app.route('/favorite-course', methods=["GET","POST"])
def favorite():  # put application's code here
    return render_template('favorite-course.html')
@app.route('/contact', methods=["GET","POST"])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')
@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()
