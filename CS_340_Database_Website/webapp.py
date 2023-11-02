# Sample Flask application for a BSG database, snapshot of BSG_people

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection
# Template:
# app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
# app.config["MYSQL_USER"] = "cs340_OSUusername"
# app.config["MYSQL_PASSWORD"] = "XXXX" | last 4 digits of OSU id
# app.config["MYSQL_DB"] = "cs340_OSUusername"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_javiyaa"
app.config["MYSQL_PASSWORD"] = "3900"
app.config["MYSQL_DB"] = "cs340_javiyaa"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes
# have homepage route to /customers by default for convenience, generally this will be your home route with its own template
@app.route("/")
def home():
    return redirect("/customers")


# route for people page
@app.route("/customers", methods=["POST", "GET"])
def customers():
    # Separate out the request methods, in this case this is for a POST
    # insert a customer into the customer entity
    if request.method == "POST":
        # fire off if user presses the Add Customer button
        if request.form.get("Add_Customer"):
            # grab user form inputs
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]


            query = "INSERT INTO Customers (first_name, last_name, email) VALUES (%s, %s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/customers")

    # Grab Customers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the customers in Customers
        query = "SELECT customer_id, first_name, last_name, email FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()


        # render edit_customers page passing our query data and rental data to the edit_customers template
        return render_template("customers.j2", data=data)


# route for delete functionality, deleting a person from bsg_people,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_customers/<int:customer_id>")
def delete_customers(customer_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Customers WHERE customer_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customer_id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/customers")


# route for edit functionality, updating the attributes of a person in bsg_people
# similar to our delete route, we want to the pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/edit_customers/<int:customer_id>", methods=["POST", "GET"])
def edit_customers(customer_id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Customers WHERE customer_id = %s" % (customer_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_people.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("Edit_Customer"):
            # grab user form inputs
            customer_id = request.form["customer_id"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email = request.form["email"]

            
            query = "UPDATE Customers SET Customers.first_name = %s, Customers.last_name = %s, Customers.email = %s WHERE Customers.customer_id = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (first_name, last_name, email, customer_id))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/customers")


# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3000, debug=True)