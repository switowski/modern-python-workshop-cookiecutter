"""Database models for our application."""

{% if cookiecutter.start_from == "Scaffolding" -%}
from todo import db


class Task(db.Model):
    """Database table to store Todo tasks."""

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """Better string representation of our task."""
        return f"<Task(id={self.id}, body={self.body})>"
{% else %}
# TODO: Write a model for your TODO tasks - it should contain at least:
# * body: text of the task
# * done: boolean value to mark task as done
{% endif %}
