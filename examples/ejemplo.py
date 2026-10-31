import sys; sys.path.insert(0, "src")
from enlaces_wa import enlace_whatsapp, render_plantilla
from enlaces_wa.plantillas import PLANTILLAS
print(enlace_whatsapp("987 654 321", "Hola, quiero info de precios"))
print(render_plantilla(PLANTILLAS["cita"], nombre="Ana", negocio="MiTienda", fecha="lunes 3", hora="10:00"))
