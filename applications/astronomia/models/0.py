from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Astronomia'
settings.subtitle = 'Fotografias'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = None
settings.description = None
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '8162a126-bdba-48ce-8d3b-a297831e519f'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
