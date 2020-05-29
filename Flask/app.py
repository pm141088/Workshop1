from flask import Flask

app = Flask(__name__)

# A route therefore defines what action is being requested
# A route defines what function in the app code should be called to perform that action
@app.route("/")
def index():
    return "Hello World!"

'''
@app.route('/films/list') 
def get_films():
    # code to fetch all film entries
    return render_template('AllFilms.html')
'''

if __name__ == "__main__":
    app.run()