from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'


# @app.route("/index.html")
# def index():
#     return render_template("index.html")

# @app.route("/works.html")
# def works():
#     return render_template("works.html")

# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")



if __name__=='__main__':
    app.run()
    
    
    
    