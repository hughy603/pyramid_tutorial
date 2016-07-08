from setuptools import setup

requires = [
    'pyramid',
]

setup(name='tutorial',
      install_requires=requires,
      # If a . is used instead of :, it will cause ImportError: No module named 'tutorial.main'
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
      )
