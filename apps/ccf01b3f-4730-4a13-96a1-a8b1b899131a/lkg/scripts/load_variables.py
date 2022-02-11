import logging, os

log = logging.getLogger(__name__)


def run(context):def run(context):

    # Setting a variable directly
    script_vals = context.get_test_script_vals()
    script_vals['username'] = 'this_is_my_username'

    # setting a variable from os env variables
    script_vals = context.get_test_script_vals()
    script_vals['password'] = os.environ.get('password')