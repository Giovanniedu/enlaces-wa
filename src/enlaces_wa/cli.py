import argparse
from .core import enlace_whatsapp
from .plantillas import PLANTILLAS
def main(argv=None):
    p = argparse.ArgumentParser(prog="enlaces-wa", description="Genera enlaces de WhatsApp (wa.me) correctos y codificados.")
    p.add_argument("telefono", help="Telefono con o sin codigo de pais")
    p.add_argument("--mensaje", default="", help="Texto del mensaje")
    p.add_argument("--plantilla", choices=sorted(PLANTILLAS), help="Usa una plantilla incluida")
    p.add_argument("--pais", default="51", help="Codigo de pais por defecto (51 = Peru)")
    a = p.parse_args(argv)
    msg = a.mensaje
    if a.plantilla:
        print(f"Plantilla '{a.plantilla}': {PLANTILLAS[a.plantilla]}")
        print("Editala con --mensaje o usala desde Python con render_plantilla().")
    print(enlace_whatsapp(a.telefono, msg, a.pais))
if __name__ == "__main__":
    main()
