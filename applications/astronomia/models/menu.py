response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Observador'),URL('default','observador_manage')==URL(),URL('default','observador_manage'),[]),
(T('Camara'),URL('default','camara_manage')==URL(),URL('default','camara_manage'),[]),
(T('Instrumento'),URL('default','instrumento_manage')==URL(),URL('default','instrumento_manage'),[]),
(T('Objetivo'),URL('default','objetivo_manage')==URL(),URL('default','objetivo_manage'),[]),
(T('Proceso'),URL('default','proceso_manage')==URL(),URL('default','proceso_manage'),[]),
(T('Observacion'),URL('default','observacion_manage')==URL(),URL('default','observacion_manage'),[]),
]