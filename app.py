from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson import ObjectId

app = Flask(__name__)

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb+srv://MOSHEL7:MosheL2680@cluster0.zebvavo.mongodb.net/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/mongo', methods=['GET', 'POST'])
def mongo():
    if request.method == 'POST':
        # Get form data
        customer_name = request.form.get('customer_name')
        customer_email = request.form.get('customer_email')

        # Insert new document/customer
        new_customer = {"name": customer_name, "email": customer_email}
        mycol.insert_one(new_customer)

    # Retrieve all customers from the database
    customers = list(mycol.find())
    return render_template('mongo.html', customers=customers)
                           
                           
@app.route('/delete', methods=['POST'])
def delete_customer():
    customer_id = request.form.get('customer_id')
    mycol.delete_one({'_id': ObjectId(customer_id)})
    return redirect(url_for('mongo'))


if __name__ == '__main__':
    app.run(debug=True)