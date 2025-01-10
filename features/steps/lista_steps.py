from behave import given, when, then
from lista import ToDoListManager
import os

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoListManager()  # Crear una nueva instancia del administrador de tareas

# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo_list.add_task(task)  # Agregar tarea usando el método de la clase

# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    assert any(t["task"] == task for t in context.todo_list.tasks), f"Task '{task}' not found in to-do list"

# Step 4: Given the to-do list contains tasks
@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoListManager()  # Crear una nueva instancia del administrador de tareas
    for row in context.table:  # Iterar sobre las filas de la tabla
        context.todo_list.add_task(row['Task'])  # Agregar cada tarea a la lista

# Step 5: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    import io
    import sys
    # Redirigir la salida estándar a un buffer para capturar el texto
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.todo_list.list_tasks()  # Llamar al método para listar las tareas
    sys.stdout = sys.__stdout__  # Restaurar la salida estándar
    context.output = captured_output.getvalue()  # Guardar la salida para comparar

# Step 6: Then the output should contain
@then('the output should contain')
def step_impl(context):
    expected_output = "Tasks:\n" + "\n".join(f"- {row['Task']}" for row in context.table)
    # Comprobar que la salida generada por list_tasks es igual a la salida esperada
    assert context.output.strip() == expected_output.strip(), f"Expected output: {expected_output}, but got: {context.output}"

# Step 7: When the user marks task "{task}" as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    task_index = next((i for i, t in enumerate(context.todo_list.tasks) if t["task"] == task), None)
    if task_index is not None:
        context.todo_list.mark_task_completed(task_index)

# Step 8: Then the to-do list should show task "{task}" as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    assert any(t["task"] == task and t["completed"] for t in context.todo_list.tasks), f"Task '{task}' not marked as completed"

# Step 9: When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_tasks()  # Limpiar las tareas

# Step 10: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0, "To-do list is not empty"

# Step 11: When the user edits task "{old_task}" to "{new_task}"
@when('the user edits task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    task_index = next((i for i, t in enumerate(context.todo_list.tasks) if t["task"] == old_task), None)
    if task_index is not None:
        context.todo_list.edit_task(task_index, new_task)

# Step 12: When the user saves the to-do list to "{filename}"
@when('the user saves the to-do list to "{filename}"')
def step_impl(context, filename):
    context.todo_list.save_tasks(filename)

# Step 13: Then the file "{filename}" should exist
@then('the file "{filename}" should exist')
def step_impl(context, filename):
    assert os.path.exists(filename), f"File '{filename}' does not exist"

# Step 14: And the file "{filename}" should contain
@then('the file "{filename}" should contain:')
def step_impl(context, filename):
    expected_content = context.text.strip()  # Aquí asegúrate de que se capturen correctamente los datos del archivo
    with open(filename, "r") as file:
        actual_content = file.read().strip()
    assert actual_content == expected_content, f"Expected:\n{expected_content}\nBut got:\n{actual_content}"

# Step 15: Given the file "{filename}" contains
@given('the file "{filename}" contains:')
def step_impl(context, filename):
    with open(filename, "w") as file:
        file.write(context.text.strip())  # Asegúrate de que el texto esté limpio antes de escribir

# Step 16: When the user loads the to-do list from "{filename}"
@when('the user loads the to-do list from "{filename}"')
def step_impl(context, filename):
    context.todo_list.load_tasks(filename)  # Cargar tareas desde el archivo
