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


def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT name, priority, complete, id
            FROM tasks
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/task_list.jinja",tasks = tasks )






#-----------------------------------------------------------
# handle the creature from data
#-----------------------------------------------------------
@app.post("/task/new")
def process_task_form():
    priority = request.form.get("priority", "unknown").strip()
    name = request.form.get("name", "unknown").strip()

#connect to the db
    with connect_db() as db:

        sql = """
            INSERT INTO tasks (name, priority)
            VALUES (?, ?)

        """
        params = (name, priority)

    #run the query
        db.execute(sql,params)

        flash(f"task {name} added successfully")

    return redirect("/")



#-----------------------------------------------------------
# Creature deletson- delate creature via id
#-----------------------------------------------------------
@app.get("/<int:id>/delete")
def delete_a_task(id):
    with connect_db() as db:
        # delete the creature using its id
        sql = """
            DELETE FROM tasks
            WHERE id=?
        """
        params = (id,)
        db.execute(sql, params)

# back to list
        flash("task deleted", "success")
        return redirect("/")
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

