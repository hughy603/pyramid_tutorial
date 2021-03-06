from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from sqlalchemy import engine_from_config

from .models import DBSession, Base
from .security import groupfinder


def main(global_config, **settings):
    my_session_factory = SignedCookieSessionFactory(
        'adfadsf324dsf345523aadfv')
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings,
                          root_factory='tutorial.models.Root',
                          session_factory=my_session_factory)

    # Security policies
    authn_policy = AuthTktAuthenticationPolicy(
        settings['tutorial.secret'],
        callback=groupfinder,
        hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('wiki_view', '/')
    config.add_route('wikipage_add', '/add')
    config.add_route('wikipage_view', '/{uid}')
    config.add_route('wikipage_edit', '/{uid}/edit')
    config.add_route('wikipage_delete', '/{uid}/delete')
    config.add_static_view('deform_static', 'deform:static/')

    config.scan('.views')
    app = config.make_wsgi_app()
    from paste.translogger import TransLogger
    app = TransLogger(app, setup_console_handler=False)
    return app
