from conectar_con_mongo import conectar_con_mongo

def actualizar_basic(nombre_pack,calidad_pack,precio_pack,stock_pack,dimensiones_pack,contenido,documento):
    contenidos = {"contenidos":{
        contenido[0]:{
            "caracteristicas":{
                "Precio":contenido[1],
                "Calidad":contenido[2],
                "Material":contenido[3],
                "Cantidad":contenido[4],
                "Stock":contenido[5],
                "Demanda":contenido[6]
            }
        },
        contenido[7]:{
            "caracteristicas":{
                "Precio":contenido[8],
                "Calidad":contenido[9],
                "Material":contenido[10],
                "Cantidad":contenido[11],
                "Stock":contenido[12],
                "Demanda":contenido[13]
            }
        }}}
    
    colleccion = conectar_con_mongo()
    
    documento_actualizado ={"Nombre pack":nombre_pack,
    "calidad":"Basic",
    "precio":precio_pack,
    "stock":stock_pack,
    "dimensiones":{
        "altura":dimensiones_pack[0],
        "ancho":dimensiones_pack[1]
    },
    "contenidos":contenidos["contenidos"]
    }

    colleccion.update_one(documento, documento_actualizado)
    print('El documento ha sido actualizado con extio')