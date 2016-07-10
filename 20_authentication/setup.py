# Install with "pip install -e ."
from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',   # Common, simple template
    'paste',            # Captures Access Logs
    'deform',           # Form Library
    'sqlalchemy',       # DB ORM
    'pyramid_tm',       # Transaction Management
    'zope.sqlalchemy',  # SqlAlchemy Transaction Management
]

setup(name='tutorial',
      install_requires=requires,
      # If a . is used instead of :, it will cause ImportError: No module named 'tutorial.main'
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      [console_scripts]
      initialize_tutorial_db = tutorial.initialize_db:main
      """,
      )
