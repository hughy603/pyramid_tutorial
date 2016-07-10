from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

import colander
import deform.widget

from .models import DBSession, Page

import logging

log = logging.getLogger(__name__)


class WikiPage(colander.MappingSchema):

    """ Represents a form with a title and body field.
    The body field is wrapped in a widget that allows the
    user change text format(bold, bullet, etc.)
    """
    title = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.RichTextWidget()
    )


class WikiViews(object):

    def __init__(self, request):
        self.request = request

    @property
    def wiki_form(self):
        """ Returns the HTML that represents the WikiPage form.
        @property makes this a first order function
        """
        schema = WikiPage()
        return deform.Form(schema, buttons=('submit',))

    @property
    def reqts(self):
        """ This gets a dictionary of all css and js resources by Deform forms.
        {
            'css':['req1', req2'],
            'js':['req1', 'req2', 'req3'],
        }
        """
        return self.wiki_form.get_widget_resources()

    @property
    def counter(self):
        """ Increments an arbitrary counter by 1 and stores it in the session
        """
        session = self.request.session
        session['counter'] = session.get('counter', 0) + 1
        return session['counter']

    @property
    def get_page(self):
        uid = int(self.request.matchdict['uid'])
        return DBSession.query(Page).filter_by(uid=uid).one()

    @view_config(route_name='wiki_view', renderer='wiki_view.jinja2')
    def wiki_view(self):
        """ This passes a list of all wiki pages to the template
        """
        pages = DBSession.query(Page).order_by(Page.title)
        return dict(title='Wiki View', pages=pages)

    @view_config(route_name='wikipage_add',
                 renderer='wikipage_addedit.jinja2')
    def wikipage_add(self):
        """ This creates a new page on the wiki
        """
        form = self.wiki_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()

            # How to get data from a form or return errors
            try:
                appstruct = self.wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new page to the database
            new_title = appstruct['title']
            new_body = appstruct['body']
            DBSession.add(Page(title=new_title, body=new_body))

            # Get the new ID and redirect
            page = DBSession.query(Page).filter_by(title=new_title).one()
            new_uid = page.uid
            url = self.request.route_url('wikipage_view', uid=new_uid)
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='wikipage_view', renderer='wikipage_view.jinja2')
    def wikipage_view(self):
        return dict(page=self.get_page)

    @view_config(route_name='wikipage_delete')
    def wikipage_delete(self):
        DBSession.delete(self.get_page)
        return HTTPFound(location='/')

    @view_config(route_name='wikipage_edit',
                 renderer='wikipage_addedit.jinja2')
    def wikipage_edit(self):
        page = self.get_page

        wiki_form = self.wiki_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = wiki_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(page=page, form=e.render())

            # Change the content and redirect to the view
            page.title = appstruct['title']
            page.body = appstruct['body']

            url = self.request.route_url('wikipage_view', uid=page['uid'])
            return HTTPFound(url)

        # The tutorial suggests deform requires a dictionary
        # There must be a pythonic was of doing this
        # form = wiki_form.render(page)
        form = self.wiki_form.render(dict(
            uid=page.uid, title=page.title, body=page.body)
        )

        return dict(page=page, form=form)
