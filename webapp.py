# Sample Flask application for a BSG database, snapshot of BSG_people

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_magnust"
app.config["MYSQL_PASSWORD"] = "2723"
app.config["MYSQL_DB"] = "cs340_magnust"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Routes
# have homepage route
@app.route("/index")
def index():
    return render_template("index.j2")

@app.route("/")
def home():
    return redirect("/index")

# route for Customers page
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

        if not data:
            return render_template("insert_customer.j2", data=data)

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
        return render_template("edit_customers.j2", data=data)

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

# route for Movies page
@app.route("/movies", methods=["POST", "GET"])
def movies():
    cur = mysql.connection.cursor()
    
    # POST
    if request.method == "POST":
        if request.form.get("Add_Movie"):
            title = request.form["title"]
            genre_id = request.form["genre_id"]

            query1 = "INSERT INTO Movies (title) VALUES (%s)"
            query2 = "INSERT INTO Movie_Genre_Details (movie_id, genre_id) VALUES (%s, %s)"
            cur.execute(query1, (title,))
            movie_id = cur.lastrowid  
            cur.execute(query2, (movie_id, genre_id))
            mysql.connection.commit()
            return redirect("/movies")
        
    # GET
    if request.method == "GET":
        query_movies = "SELECT movie_id, title FROM Movies"
        cur.execute(query_movies)
        movies_data = cur.fetchall()

        query_genres = "SELECT genre_id, genre_name FROM Genres"  
        cur.execute(query_genres)
        genres_data = cur.fetchall()

        cur.close()
        return render_template("movies.j2", data=movies_data, genres=genres_data)


# route for delete functionality, deleting a movie from Movies,
# we want to pass the 'id' value of that movie on button click (see HTML) via the route
@app.route("/delete_movies/<int:movie_id>")
def delete_movies(movie_id):
    # mySQL query to delete the movie with our passed movie_id
    query = "DELETE FROM Movies WHERE movie_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (movie_id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/movies")

# route for Genres page
@app.route("/genres", methods=["POST", "GET"])
def genres():
    # Separate out the request methods, in this case this is for a POST
    # insert a genre into the Genre entity
    if request.method == "POST":
        # fire off if user presses the Add Genre button
        if request.form.get("Add_Genre"):
            # grab user form inputs
            genre_name = request.form["genre_name"]

            query = "INSERT INTO Genres (genre_name) VALUES (%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (genre_name,))
            mysql.connection.commit()

            # redirect back to Genres page
            return redirect("/genres")

    # Grab Genres data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the genres in Genres
        query = "SELECT genre_id, genre_name FROM Genres"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_genres page passing our query data to the edit_genres template
        return render_template("genres.j2", data=data)

# route for delete functionality, deleting a genre from Genres,
# we want to pass the 'id' value of that genre on button click (see HTML) via the route
@app.route("/delete_genres/<int:genre_id>")
def delete_genres(genre_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Genres WHERE genre_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (genre_id,))
    mysql.connection.commit()

    # redirect back to genres page
    return redirect("/genres")

@app.route("/movie_genre_details", methods=["POST", "GET"])
def movie_genre_details():
    cur = mysql.connection.cursor()

    if request.method == "POST":
        # fire off if user presses the Add movie_genre_details button
        if request.form.get("Add_Movie_Genre_Detail"):
            # grab user form inputs
            genre_id = request.form["genre_id"]
            movie_id = request.form["movie_id"]

            query = "INSERT INTO Movie_Genre_Details (genre_id, movie_id) VALUES (%s,%s)"
            cur.execute(query, (genre_id, movie_id))
            mysql.connection.commit()

            # redirect back to movie_genre_details page
            return redirect("/movie_genre_details")

    # Handle GET request
    # Fetch all movie_genre_details
    details_query = "SELECT movie_genre_id, movie_id, genre_id FROM Movie_Genre_Details"
    cur.execute(details_query)
    details = cur.fetchall()

    # Fetch all movies
    movies_query = "SELECT movie_id, title FROM Movies"
    cur.execute(movies_query)
    movies = cur.fetchall()

    # Fetch all genres
    genres_query = "SELECT genre_id, genre_name FROM Genres"
    cur.execute(genres_query)
    genres = cur.fetchall()

    # Pass fetched data to the template
    return render_template("movie_genre_details.j2", details=details, movies=movies, genres=genres)

@app.route("/edit_movie_genre_details/<int:movie_genre_id>", methods=["POST", "GET"])
def edit_movie_genre_details(movie_genre_id):
    if request.method == "GET":
        cur = mysql.connection.cursor()

        # get the genre-id 
        movie_genre_query = "SELECT * FROM Movie_Genre_Details WHERE movie_genre_id = %s"
        cur.execute(movie_genre_query, (movie_genre_id,))
        movie_genre_detail = cur.fetchone()

        # get all movies 
        movies_query = "SELECT movie_id, title FROM Movies"
        cur.execute(movies_query)
        movies = cur.fetchall()

        # get all genres
        genres_query = "SELECT genre_id, genre_name FROM Genres"
        cur.execute(genres_query)
        genres = cur.fetchall()

        # pass data to template
        return render_template("edit_movie_genre_details.j2",
                               movie_genre_detail=movie_genre_detail,
                               movies=movies,   
                               genres=genres)
    
    return redirect("/movie_genre_details")

# route for delete functionality, deleting a person from bsg_people,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_movie_genre_details/<int:movie_genre_id>")
def delete_movie_genre_details(movie_genre_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Movie_Genre_Details WHERE movie_genre_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (movie_genre_id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/movie_genre_details")

# route for Rentals page
@app.route("/rentals", methods=["POST", "GET"])
def rentals():
    # Separate out the request methods, in this case this is for a POST
    # insert a rental into the Rentals entity
    if request.method == "POST":
        # fire off if user presses the Add Rental button
        if request.form.get("Add_Rental"):
            # grab user form inputs
            customer_id = request.form["customer_id"]
            movie_id = request.form["movie_id"]
            due_date = request.form["due_date"]


            query = "INSERT INTO Rentals (customer_id, movie_id, due_date) VALUES (%s, %s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, movie_id, due_date))
            mysql.connection.commit()

            # redirect back to people page
            return redirect("/rentals")

    # Grab Customers data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all the customers in Customers
        query = "SELECT rental_id, customer_id, movie_id, due_date FROM Rentals"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()


        # render edit_customers page passing our query data and rental data to the edit_customers template
        return render_template("rentals.j2", data=data)


# route for delete functionality, deleting a person from bsg_people,
# we want to pass the 'id' value of that person on button click (see HTML) via the route
@app.route("/delete_rentals/<int:rental_id>")
def delete_rentals(rental_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Rentals WHERE rental_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (rental_id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/rentals")

# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=3243, debug=True)