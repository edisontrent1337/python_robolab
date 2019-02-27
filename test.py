import unittest
import car_seller

class TestCarSeller(unittest.TestCase):

    # test methods have to be prexied with test_
    def test_sellBMW(self):
        bmw = car_seller.sellBMW()
        self.assertEqual(bmw.doors, 5)

    # test methods have to be prexied with test_
    def test_upgradeCar(self):
        bmw = car_seller.sellBMW()
        car_seller.upgradeCar(bmw)
        # this fails because we expect the new hp to be 450
        self.assertEqual(bmw.hp, 450)

# main entry point
if __name__ == '__main__':
    unittest.main()
