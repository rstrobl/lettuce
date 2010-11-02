import commands
from tests.asserts import assert_equals
from lettuce.fs import FileSystem

current_directory = FileSystem.dirname(__file__)

def test_test_database_creation_and_migration():
    "creating, migrating (with south) and destroying test database with the -t param on harvest"
    FileSystem.pushd(current_directory, 'django', 'espinafre')

    status, out = commands.getstatusoutput("python manage.py harvest --test-database --verbosity=3 --apps=leaves")
    assert_equals(status, 0)
    FileSystem.popd()

    lines = out.splitlines()
    assert_equals(lines[0], u"Django's builtin server is running at 0.0.0.0:8000")
    assert_equals(lines[1], u"Setting up a test database...")
    assert_equals(lines[3], u"Syncing...")
    assert u"Destroying test database..." in out
