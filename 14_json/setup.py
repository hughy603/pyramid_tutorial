# Install with "pip install -e ."
from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
]

setup(name='tutorial',
      install_requires=requires,
      # If a . is used instead of :, it will cause ImportError: No module named 'tutorial.main'
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
      )
