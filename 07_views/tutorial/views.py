from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home')
def home(request):
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')
