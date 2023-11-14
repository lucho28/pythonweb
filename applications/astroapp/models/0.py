from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Astro App'
settings.subtitle = 'Observaciones'
settings.author = 'lucho'
settings.author_email = 'luedugonzalez@gmail.com'
settings.keywords = None
settings.description = None
settings.layout_theme = 'Default'
settings.database_uri = 'mysql://root:Luchogon28!@localhost/observaciones'
settings.security_key = '02a0e77d-c213-4e12-957e-40707eef9cdd'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
