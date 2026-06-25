#===========================================================
# APP NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome page
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    return render_template("pages/welcome.jinja")


#-----------------------------------------------------------
# Creature list page - Show all the creatures
#-----------------------------------------------------------
@app.get("/todotable")
def show_all_task():
    with connect_db() as db:
        sql = """
            SELECT id, task
            FROM todotable
        """
        params = ()
        todotable = db.execute(sql, params).fetchall()

        return render_template("pages/todotable_list.jinja", )



#-----------------------------------------------------------
# handle the creature from data
#-----------------------------------------------------------
@app.post("/todotable/new")
def process_todotable_form():
    priority = request.form.get("priority", "unknown").strip()
    name = request.form.get("name", "unknown").strip()

#connect to the db
    with connect_db() as db:

        sql = """
            INSERT INTO todotable (priority, name)
            VALUES (?, ?)

        """
        params = (priority, name)

    #run the query
        db.execute(sql,params)

        flash(f"todotable {name} added successfully")

    return redirect("/todotable")



    #-----------------------------------------------------------
# Creature deletson- delate creature via id
#-----------------------------------------------------------
@app.get("/todotable/<int:id>/complete")
def complete_tasks(id):
    with connect_db() as db:
        # delete the creature using its id
        sql = """
            COMPLETE FROM todotable
            WHERE id=?
        """
        params = (id,)
        db.execute(sql, params)

# back to list
        flash("task done", "success")
        return redirect("/todotable")
#-----------------------------------------------------------
# Help page - Show some help
#-----------------------------------------------------------
@app.get("/help")
def show_help():

    flash("Flash test message")
    flash("Flash test message with a longer bit of text")
    flash("Success test message", "success")
    flash("Error test message", "error")

    return render_template("pages/help.jinja")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

