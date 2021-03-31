# Step 1 - Import Flask
from flask import Flask,render_template

# Step 2 - Create Flask app instance
app = Flask(__name__)

# Step 3 - Define a route
@app.route('/') #This is called a decorator
def helloWorld():
    return render_template('mypage.html')