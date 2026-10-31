"""Core: genera enlaces wa.me correctos, sin dependencias externas."""
from __future__ import annotations
import csv, io, re
from urllib.parse import quote

def normalizar_telefono(telefono: str, codigo_pais: str = "51") -> str:
    """Deja solo digitos. Si falta el codigo de pais, lo agrega.
    Ej: '+51 987 654 321' -> '51987654321'; '987654321' (PE) -> '51987654321'"""
    digitos = re.sub(r"\D", "", str(telefono or ""))
    if not digitos:
        raise ValueError("Telefono vacio")
    if digitos.startswith("00"):
        digitos = digitos[2:]
    if len(digitos) <= 9 and not digitos.startswith(codigo_pais):
        digitos = codigo_pais + digitos
    if not (8 <= len(digitos) <= 15):
        raise ValueError(f"Telefono fuera de rango E.164: {digitos}")
    return digitos

def enlace_whatsapp(telefono: str, mensaje: str = "", codigo_pais: str = "51") -> str:
    tel = normalizar_telefono(telefono, codigo_pais)
    base = f"https://wa.me/{tel}"
    return f"{base}?text={quote(mensaje.strip())}" if mensaje and mensaje.strip() else base

def render_plantilla(plantilla: str, **datos: str) -> str:
    """Reemplaza {nombre}, {negocio}, etc. Falla claro si falta un dato."""
    try:
        return plantilla.format(**datos)
    except KeyError as e:
        raise ValueError(f"Falta el dato {e} para la plantilla") from e

def enlaces_desde_csv(texto_csv: str, plantilla: str, columna_telefono: str = "telefono") -> list[dict]:
    lector = csv.DictReader(io.StringIO(texto_csv))
    if not lector.fieldnames or columna_telefono not in lector.fieldnames:
        raise ValueError(f"El CSV necesita la columna '{columna_telefono}'")
    salida = []
    for fila in lector:
        mensaje = render_plantilla(plantilla, **{k: (v or "") for k, v in fila.items()})
        salida.append({"telefono": normalizar_telefono(fila[columna_telefono]),
                       "mensaje": mensaje,
                       "enlace": enlace_whatsapp(fila[columna_telefono], mensaje)})
    return salida
