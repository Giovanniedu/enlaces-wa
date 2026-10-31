# enlaces-wa

Generador **gratuito y open source** de enlaces de WhatsApp (`wa.me`) para emprendedores y negocios pequeños de habla hispana.

Muchos negocios pierden ventas por enlaces rotos: espacios sin codificar, `¿` y acentos que se rompen, o números sin código de país. `enlaces-wa` lo resuelve en una línea, **sin dependencias externas**.

## Qué hace
- Normaliza teléfonos (ej. `987 654 321` → `51987654321`, código 51 = Perú por defecto, configurable)
- Codifica el mensaje correctamente (acentos, `¿?`, emojis, saltos)
- 5 plantillas en español listas: saludo, cita, recordatorio de pago, delivery y postventa
- Generación masiva desde CSV: un enlace personalizado por cliente
- CLI y librería Python (solo biblioteca estándar)

## Instalación
```bash
pip install .
```

## Uso rápido
```bash
enlaces-wa 987654321 --mensaje "Hola, quiero info de precios"
# https://wa.me/51987654321?text=Hola%2C%20quiero%20info%20de%20precios
```
```python
from enlaces_wa import enlace_whatsapp, enlaces_desde_csv
print(enlace_whatsapp("987654321", "Hola ¿sigue disponible?"))
```

## Pruebas
```bash
python -m unittest discover -s tests -v
```

## Roadmap
- [ ] Generador de QR del enlace sin dependencias pesadas
- [ ] Más países de LatAm con validación de longitud por país
- [ ] Página web estática (GitHub Pages) que funciona 100% en el navegador
- [ ] Más plantillas aportadas por la comunidad (citas médicas, clases, reservas)

## Contribuir
Ver `CONTRIBUTING.md`. Los issues con la etiqueta `good first issue` son ideales para empezar.

## Licencia
MIT — úsalo libremente, también en proyectos comerciales.
