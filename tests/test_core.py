import unittest, sys
sys.path.insert(0, "src")
from enlaces_wa import enlace_whatsapp, normalizar_telefono, enlaces_desde_csv

class TestCore(unittest.TestCase):
    def test_normaliza_peru(self):
        self.assertEqual(normalizar_telefono("+51 987 654 321"), "51987654321")
        self.assertEqual(normalizar_telefono("987654321"), "51987654321")
    def test_enlace_codifica(self):
        url = enlace_whatsapp("987654321", "Hola ¿sigue disponible?")
        self.assertTrue(url.startswith("https://wa.me/51987654321?text="))
        self.assertIn("%C2%BF", url)  # ¿ codificado, no roto
        self.assertNotIn(" ", url)
    def test_csv(self):
        csv_txt = "telefono,nombre,negocio,tema\n987654321,Ana,MiTienda,zapatos\n"
        out = enlaces_desde_csv(csv_txt, "Hola {nombre}, soy de {negocio}. Consulta: {tema}.")
        self.assertEqual(len(out), 1)
        self.assertIn("Ana", out[0]["mensaje"])
    def test_telefono_vacio(self):
        with self.assertRaises(ValueError):
            normalizar_telefono("")
if __name__ == "__main__":
    unittest.main()
