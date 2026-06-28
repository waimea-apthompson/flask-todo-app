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

def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT name, priority, complete
            FROM tasks
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/tasks_list.jinja",tasks = tasks )






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
            INSERT INTO task (priority, name)
            VALUES (?, ?)

        """
        params = (priority, name)

    #run the query
        db.execute(sql,params)

        flash(f"tasks {name} added successfully")

    return redirect("/tasks")



    #-----------------------------------------------------------
# Creature deletson- delate creature via id
#-----------------------------------------------------------
@app.get("/task/<int:id>/complete")
def complete_tasks(id):
    with connect_db() as db:
        
        sql = """
            COMPLETE FROM tasks
            WHERE id=?
        """
        params = (id,)
        db.execute(sql, params)

# back to list
        flash("task done", "success")
        return redirect("/tasks")
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

