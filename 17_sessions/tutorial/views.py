from pyramid.view import (view_config, view_defaults)
import logging
log = logging.getLogger(__name__)


@view_defaults(route_name='hello')
class TutorialViews:

    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'

    @property
    def full_name(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return first + ' ' + last

    @property
    def counter(self):
        session = self.request.session
        session['counter'] = session.get('counter',0) + 1
        return session['counter']

    @view_config(route_name='home', renderer='home.jinja2')
    def home(self):
        log.debug('In home view')
        return {'page_title': 'Home View'}

    @view_config(renderer='hello.jinja2')
    def hello(self):
        log.debug('In home view')
        return {'name': 'Hello View'}

    @view_config(request_method='POST', renderer='edit.jinja2')
    def edit(self):
        new_name = self.request.params['new_name']
        log.debug('Editing ' + new_name)
        return {'page_title': 'Edit View', 'new_name': new_name}

    @view_config(request_method='POST',
                 request_param='form.delete',
                 renderer='delete.jinja2')
    def delete(self):
        log.debug('Deleting ' + new_name)
        return {'page_title': 'Delete View'}
