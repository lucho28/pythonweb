### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_observador',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_apellido', type='string',
          label=T('Apellido')),
    Field('f_dni', type='string',
          label=T('Dni')),
    Field('f_email', type='string', notnull=True,
          label=T('Email')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_observador_archive',db.t_observador,Field('current_record','reference t_observador',readable=False,writable=False))

########################################
db.define_table('t_objetivo',
    Field('f_nombre', type='string', notnull=True,
          label=T('Nombre')),
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_comentario', type='text',
          label=T('Comentario')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_objetivo_archive',db.t_objetivo,Field('current_record','reference t_objetivo',readable=False,writable=False))

########################################
db.define_table('t_marca',
    Field('f_nombre', type='string',
          label=T('Nombre')),
    auth.signature,
    format='%(f_nombre)s',
    migrate=settings.migrate)

db.define_table('t_marca_archive',db.t_marca,Field('current_record','reference t_marca',readable=False,writable=False))

########################################
db.define_table('t_camara',
    Field('f_tipo', type='string',
          label=T('Tipo')),
    Field('f_marca', type='reference t_marca',
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
    Field('f_marca', type='reference t_marca',
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
db.define_table('t_lugar',
    Field('f_pais', type='string',
          label=T('Pais')),
    Field('f_provincia', type='string',
          label=T('Provincia')),
    Field('f_ciudad', type='string',
          label=T('Ciudad')),
    Field('f_localidad', type='string',
          label=T('Localidad')),
    auth.signature,
    format='%(f_pais)s',
    migrate=settings.migrate)

db.define_table('t_lugar_archive',db.t_lugar,Field('current_record','reference t_lugar',readable=False,writable=False))

########################################
db.define_table('t_observacion',
    Field('f_observador', type='reference t_observador',
          label=T('Observador')),
    Field('f_objetivo', type='reference t_objetivo',
          label=T('Objetivo')),
    Field('f_lugar', type='reference t_lugar',
          label=T('Lugar')),
    Field('f_fecha', type='date',
          label=T('Fecha')),
    Field('f_hora', type='time',
          label=T('Hora')),
    Field('f_instrumento', type='reference t_instrumento',
          label=T('Instrumento')),
    Field('f_camara', type='reference t_camara',
          label=T('Camara')),
    Field('f_tomas', type='string',
          label=T('Tomas')),
    Field('f_exp', type='string',
          label=T('Exp')),
    Field('f_iso', type='string',
          label=T('Iso')),
    Field('f_imagen', type='upload',
          label=T('Imagen')),
    Field('f_proceso', type='text',
          label=T('Proceso')),
    auth.signature,
    format='%(f_observador)s',
    migrate=settings.migrate)

db.define_table('t_observacion_archive',db.t_observacion,Field('current_record','reference t_observacion',readable=False,writable=False))
