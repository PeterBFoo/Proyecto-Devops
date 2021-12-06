from datos_insertar_documento import datos_insertar_documento
from insertar_documento_basic import insertar_documento_basic
from insertar_documento_standard import insertar_documento_standard
from insertar_documento_premium import insertar_documento_premium

def insertar_documento ():
    nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido = datos_insertar_documento()
    if calidad_pack.lower() == 'basic':
        insertar_documento_basic(nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido)
    elif calidad_pack.lower() == 'standard':
        insertar_documento_standard(nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido)
    elif calidad_pack.lower() == 'premium':
        insertar_documento_premium(nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido)
    else:
        print('Ha introducido mal la calidad del pack')
insertar_documento()
    