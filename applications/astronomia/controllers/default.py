# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def observador_manage():
    form = SQLFORM.smartgrid(db.t_observador,onupdate=auth.archive)
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
def objetivo_manage():
    form = SQLFORM.smartgrid(db.t_objetivo,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def proceso_manage():
    form = SQLFORM.smartgrid(db.t_proceso,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def observacion_manage():
    form = SQLFORM.smartgrid(db.t_observacion,onupdate=auth.archive)
    return locals()

