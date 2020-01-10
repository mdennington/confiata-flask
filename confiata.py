# CONFIATA WEB SITE
# TODO CLEAN UP PACKAGES NOT REQUIRED e.g. flask_migrate
import os
import click
from app import create_app, db
from app.models import User, Role, Permission

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# allows Flask SHELL to load the model
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission)


# TODO Investigate how to do this with pytest
@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
