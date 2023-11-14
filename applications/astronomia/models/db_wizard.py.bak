### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_observador',
    Field('f_dni', type='string',
          label=T('Dni')),
    Field('f_nombre', type='string',
          label=T('Nombre')),
    Field('f_apellido', type='string',
          label=T('Apellido')),
    Field('f_email', type='string',
          label=T('Email')),
    auth.signature,
    format='%(f_dni)s',
    migrate=settings.migrate)

db.define_table('t_observador_archive',db.t_observador,Field('current_record','reference t_observador',readable=False,writable=False))

########################################
db.define_table('t_camara',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_marca', type='string',
          label=T('Marca')),
    Field('f_pxls', type='string',
          label=T('Pxls')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_camara_archive',db.t_camara,Field('current_record','reference t_camara',readable=False,writable=False))

########################################
db.define_table('t_instrumento',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_marca', type='string',
          label=T('Marca')),
    Field('f_diametro', type='string',
          label=T('Diametro')),
    Field('f_focal', type='string',
          label=T('Focal')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_instrumento_archive',db.t_instrumento,Field('current_record','reference t_instrumento',readable=False,writable=False))

########################################
db.define_table('t_objetivo',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_nombre', type='string',
          label=T('Nombre')),
    Field('f_comentario', type='string',
          label=T('Comentario')),
    auth.signature,
    format='%(f_tipo)s',
    migrate=settings.migrate)

db.define_table('t_objetivo_archive',db.t_objetivo,Field('current_record','reference t_objetivo',readable=False,writable=False))

########################################
db.define_table('t_proceso',
    Field('f_software', type='string',
          label=T('Software')),
    Field('f_comentario', type='string',
          label=T('Comentario')),
    auth.signature,
    format='%(f_software)s',
    migrate=settings.migrate)

db.define_table('t_proceso_archive',db.t_proceso,Field('current_record','reference t_proceso',readable=False,writable=False))

########################################
db.define_table('t_observacion',
    Field('f_lugar', type='string',
          label=T('Lugar')),
    Field('f_fecha', type='string',
          label=T('Fecha')),
    Field('f_hora', type='string',
          label=T('Hora')),
    Field('f_exposicion', type='string',
          label=T('Exposicion')),
    Field('f_tomas', type='string',
          label=T('Tomas')),
    Field('f_observador', type='reference t_observador',
          label=T('Observador')),
    Field('f_camara', type='reference t_camara',
          label=T('Camara')),
    Field('f_instrumento', type='reference t_instrumento',
          label=T('Instrumento')),
    Field('f_proceso', type='reference t_proceso',
          label=T('Proceso')),
    auth.signature,
    format='%(f_lugar)s',
    migrate=settings.migrate)

db.define_table('t_observacion_archive',db.t_observacion,Field('current_record','reference t_observacion',readable=False,writable=False))
