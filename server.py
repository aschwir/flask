from flask import Flask, render_template,request,url_for, redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt',mode='a') as database:
       email = data['email']
       subject = data['subject']
       message = data['message']
       file = database.write(f'\n{email},{subject},{message}')
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'