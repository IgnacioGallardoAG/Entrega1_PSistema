import unittest
from distance_client import Client

class PruebasCliente(unittest.TestCase):

    def setUp(self):
        self.delta = 20  # Delta de 0,1% de 20000
        print(f"\n--- Ejecutando prueba: {self._testMethodName} ---")

    def test_millas_nauticas(self):
        # Caso 1: Usando millas náuticas
        client = Client(0, 0, 90, 45, "nm")
        client.ask_distance()
        self.assertIsNotNone(client.distancia)
        self.assertAlmostEqual(client.distancia, 5408.75, delta=self.delta)

    def test_latitud_longitud_fuera_de_rango(self):
        # Caso 2: Latitud y longitud fuera de rango
        client = Client(0, -91, 181, 0, "km")  # Longitud en a y c, latitud en b y d.
        with self.assertRaises(ValueError):
            client.ask_distance()

    def test_unidad_vacia(self):
        # Caso 3: Unidad vacía, se espera distancia en kilómetros por defecto
        client = Client(0, 0, 90, 45, "")
        client.ask_distance()
        self.assertIsNotNone(client.distancia)
        self.assertAlmostEqual(client.distancia, 10018.75, delta=self.delta)

    def test_un_punto_faltante(self):
        # Caso 4: Un punto faltante
        client = Client(90, 45, None, None, "km")
        with self.assertRaises(ValueError):
            client.ask_distance()

    def test_misma_posicion(self):
        # Caso 5: Mismos puntos (debería dar 0 km)
        client = Client(0, 0, 0, 0, "km")
        client.ask_distance()

        # Asegúrate de que no sea None antes de comparar
        if client.distancia is None:
            self.fail("El cliente devolvió None, se esperaba 0.")
        else:
            self.assertEqual(client.distancia, 0)

    def test_infinita_distancia_latitud(self):
        # Caso 6: Prueba de latitud con infinitas distancias iguales (-90,0) a (90,0)
        client = Client(0, -90, 0, 90, "km")
        client.ask_distance()
        self.assertAlmostEqual(client.distancia, 20000, delta=10)  # Aproximación cercana a 20,000 km

    def test_infinita_distancia_longitud(self):
        # Caso 7: Prueba con longitudes extremas (longitud -180 y 180)
        client = Client(-180, 0, 180, 0, "km")
        client.ask_distance()

        # Verificar si client.distancia es None
        if client.distancia is None:
            self.fail("El cliente devolvió None, se esperaba una distancia alrededor de 20037.51 km.")
        else:
            self.assertAlmostEqual(client.distancia, 20037.51, delta=self.delta)

    def test_longitud_extrema(self):
        # Caso 8: Prueba con longitud extrema (0,0) a (0,180)
        client = Client(0, 0, 180, 0, "km")
        client.ask_distance()
        self.assertAlmostEqual(client.distancia, 20037.51, delta=self.delta)

    def test_distancia_simetrica(self):
        # Caso 9: Dos puntos simétricos, (-45,-90) y (45,90)
        client = Client(-90, -45, 90, 45, "km")
        client.ask_distance()
        self.assertAlmostEqual(client.distancia, 20037.51, delta=self.delta)

    def test_distancia_a_metros(self):
        # Caso 10: Retorno de distancia en metros, [0,0] a [0.00001,0]
        client = Client(0, 0, 0.00001, 0, "km")
        client.ask_distance()
        self.assertAlmostEqual(client.distancia, 0.001, delta=self.delta)

    def test_unidad_invalida(self):
        # Caso 11: Usando millas náuticas
        client = Client(0, 0, 90, 45, "cm")
        self.assertEqual(client.unidadMedida, "nm")


if __name__ == '__main__':
    unittest.main()