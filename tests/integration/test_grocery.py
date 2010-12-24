# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import commands
import re

from tests.asserts import assert_equals, assert_not_equals
from lettuce.fs import FileSystem

current_directory = FileSystem.dirname(__file__)

def test_django_admin_media_serving():
    'serving admin media in django projects that have "admin" in INSTALLED_APPS'

    FileSystem.pushd(current_directory, "django", "grocery")

    status, out = commands.getstatusoutput("python manage.py harvest --verbosity=2 ./features/")
    assert_equals(status, 0)
    FileSystem.popd()

    lines = out.splitlines()

    assert_not_equals(re.match(r"Creating test database for alias '\w+'\.\.\.",lines[0]), None)
    assert_equals(lines[1], u"Preparing to server django's admin site static files...")
    assert_not_equals(re.match(r"Django's builtin server is running at 0\.0\.0\.0:\d+",lines[2]), None)

def test_django_no_test_database_option():
    'test whether no test database is used if not wanted'

    FileSystem.pushd(current_directory, "django", "grocery")

    status, out = commands.getstatusoutput("python manage.py harvest --verbosity=2 --no-test-database ./features/")
    assert_equals(status, 0)
    FileSystem.popd()

    assert_equals(re.match(r".*Creating test database for alias '\w+'\.\.\..*",out), None)
