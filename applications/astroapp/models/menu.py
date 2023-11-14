response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Inicio'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Observador'),URL('default','observador_manage')==URL(),URL('default','observador_manage'),[]),
(T('Objetivo'),URL('default','objetivo_manage')==URL(),URL('default','objetivo_manage'),[]),
(T('Marca'),URL('default','marca_manage')==URL(),URL('default','marca_manage'),[]),
(T('Camara'),URL('default','camara_manage')==URL(),URL('default','camara_manage'),[]),
(T('Instrumento'),URL('default','instrumento_manage')==URL(),URL('default','instrumento_manage'),[]),
(T('Lugar'),URL('default','lugar_manage')==URL(),URL('default','lugar_manage'),[]),
(T('Observacion'),URL('default','observacion_manage')==URL(),URL('default','observacion_manage'),[]),
]
