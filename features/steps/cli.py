from importlib import import_module
import subprocess
from behave import given, when, then
from behave.runner import Context


@given("I have the cli installed")
def step_impl(context: Context):
    module = import_module("flasked_blog")
    assert module is not None


@when("I run the 'hello' command with 'Ivan Pina' as argument")
def step_impl(context: Context):
    response = subprocess.check_output(["flasked_blog_cli", "hello", "--name", "Ivan Pina"], text=True)
    context.response = response


@then("I should see 'Hello Ivan Pina!'")
def step_impl(context: Context):
    assert context.response == "Hello Ivan Pina!\n"
    # assert False
