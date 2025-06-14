from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World, Fuck the King!!! I\'m the one who knocks'


@app.route('/index.html')
def my_home():
    return render_template('index.html')


# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

def write_to_file(data):
    with open('database.txt', mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def contact():  
#     return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route("/static/assets/apple-icon-180x180.png")
# def favicon():
#     return app.send_static_file('/static/assets/apple-icon-180x180.png')

# @app.route('/blog')
# def blog():
#     return 'This is my blog space'

# @app.route('/blog/2025/dog')
# def blog2():
#     return 'this is my dog'