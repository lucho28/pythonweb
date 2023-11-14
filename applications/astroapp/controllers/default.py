# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
@auth.requires_login()
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def observador_manage():
    form = SQLFORM.smartgrid(db.t_observador,onupdate=auth.archive)
    return locals()
'''
def observador_manage():
    form=SQLFORM(db.t_observador)
    if form.process(session=None, formname='astroapp').accepted:
       response.flash = 'formulario aceptado'
    elif form.errors:
       response.flash = 'el formulario tiene errores'
    else:
       response.flash = 'por favor completa el formulario'
    # Ten en cuenta que no se pasa una instancia del formulario a la vista
    return dict()

'''
@auth.requires_login()
def objetivo_manage():
    form = SQLFORM.smartgrid(db.t_objetivo,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def marca_manage():
    form = SQLFORM.smartgrid(db.t_marca,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def camara_manage():
    form = SQLFORM.smartgrid(db.t_camara,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def instrumento_manage():
    form = SQLFORM.smartgrid(db.t_instrumento,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def lugar_manage():
    form = SQLFORM.smartgrid(db.t_lugar,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def observacion_manage():
    form = SQLFORM.smartgrid(db.t_observacion,onupdate=auth.archive)
    return locals()
