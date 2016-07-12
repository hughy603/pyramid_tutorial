This is example code following the Pyramid tutorial at http://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html

Pyramid tutorials 21 and 22 were not completed.
This gives a basic example of how pyramid works.
Authentication and Authorization are important, but
ease of AD integration is more important.

The most interesting benefit of Pyramid was view
classes being usable from templates.  Need to confirm
if the same is possible in DJango or Flask


Pyramid vs Django:
Seems like a tradeoff between
    community activity(Django) and custom ORM(Pyramid).
Benefit of Django is built in admin view.
Benefit of Pyramid is SQLAlchemy
Benefit of Pyramid is no database is required.  SQLite
    and migrations aren't needed for SOA

Pyramid vs Flask: How does scaling Flask compare to
    intial overhead of Pyramid
Pyramid's .ini config seems limited across environments
How different is a strict MVC Setup.  They both use
    SQLAlchemy and Jinja2

Use Case: Build Services Quickly.
    Win users can't use Python or Linux, so build web interface
        Download risks security violation
        Coorporate Security (No Anaconda)
    Use REST API for validation
    Parse database data
        Develop faster than PL/SQL (ex. XML Parsing)
    IO Service
        Input all vendors, products, and variables
        Ouput optimal choice


