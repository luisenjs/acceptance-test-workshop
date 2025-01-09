from behave import given, when, then
import os

# Define a list to represent the to-do list
to_do_list = []

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []

# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    to_do_list.append({"task": task, "completed": False})

# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    global to_do_list
    assert any(t["task"] == task for t in to_do_list), f"Task '{task}' not found in to-do list"

# Step 4: Given the to-do list contains tasks:
@given('the to-do list contains tasks:')
def step_impl(context):
    global to_do_list
    to_do_list = [{"task": row["Task"], "completed": False} for row in context.table]

# Step 5: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    global to_do_list
    context.output = "\n".join([f"- {t['task']}" for t in to_do_list])

# Step 6: Then the output should contain:
@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip()
    actual_output = "\nTasks:\n" + context.output.strip()
    assert actual_output == expected_output, f"Expected:\n{expected_output}\nBut got:\n{actual_output}"

# Step 7: When the user marks task "{task}" as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    for t in to_do_list:
        if t["task"] == task:
            t["completed"] = True
            break

# Step 8: Then the to-do list should show task "{task}" as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    assert any(t["task"] == task and t["completed"] for t in to_do_list), f"Task '{task}' not marked as completed"

# Step 9: When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []

# Step 10: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    global to_do_list
    assert len(to_do_list) == 0, "To-do list is not empty"

# Step 11: When the user edits task "{old_task}" to "{new_task}"
@when('the user edits task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    global to_do_list
    for t in to_do_list:
        if t["task"] == old_task:
            t["task"] = new_task
            break

# Step 12: When the user saves the to-do list to "{filename}"
@when('the user saves the to-do list to "{filename}"')
def step_impl(context, filename):
    global to_do_list
    with open(filename, "w") as file:
        for t in to_do_list:
            file.write(f"{t['task']}|{t['completed']}\n")

# Step 13: Then the file "{filename}" should exist
@then('the file "{filename}" should exist')
def step_impl(context, filename):
    assert os.path.exists(filename), f"File '{filename}' does not exist"

# Step 14: And the file "{filename}" should contain:
@then('the file "{filename}" should contain:')
def step_impl(context, filename):
    expected_content = context.text.strip()
    with open(filename, "r") as file:
        actual_content = file.read().strip()
    assert actual_content == expected_content, f"Expected:\n{expected_content}\nBut got:\n{actual_content}"

# Step 15: When the user loads the to-do list from "{filename}"
@when('the user loads the to-do list from "{filename}"')
def step_impl(context, filename):
    global to_do_list
    if os.path.exists(filename):
        with open(filename, "r") as file:
            to_do_list = []
            for line in file:
                task, completed = line.strip().split("|")
                to_do_list.append({"task": task, "completed": completed == "True"})

# Step 16: Given the file "{filename}" contains:
@given('the file "{filename}" contains:')
def step_impl(context, filename):
    with open(filename, "w") as file:
        file.write(context.text.strip())

@given(u'the to-do list contains tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the to-do list contains tasks')


@then(u'the output should contain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain')


@then(u'the file "tasks.txt" should contain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the file "tasks.txt" should contain')


@given(u'the file "tasks.txt" contains')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the file "tasks.txt" contains')