from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_observador,10)
     populate(db.t_objetivo,10)
     populate(db.t_marca,10)
     populate(db.t_camara,10)
     populate(db.t_instrumento,10)
     populate(db.t_lugar,10)
     populate(db.t_observacion,10)
