"""API functions to interact with TODO tasks."""

{% if cookiecutter.start_from == "Scaffolding" -%}
from todo.models import Task, db


def get_tasks():
    return Task.query.all()


def create_task(body):
    # TODO: add task to the database
    pass


def delete_task(task_id):
    # TODO: delete a task from the database
    pass


def finish_task(task_id):
    # TODO: mark task as done
    pass
{% else %}
# TODO: Write functions to list/create/delete/finish tasks
{% endif %}
