"""Main file of our application.

When ran with:
$ python run.py
it will reset the database and start the webserver.
"""

{% if cookiecutter.start_from == "Scaffolding" -%}
from todo import app, db

{% endif %}
if __name__ == "__main__":
{% if cookiecutter.start_from == "Scaffolding" %}
    db.drop_all()
    db.create_all()

    app.run()
{% else %}
    # TODO: Code here should set up the everything and run the web server
{% endif -%}
