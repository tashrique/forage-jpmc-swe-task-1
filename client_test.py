import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'top_bid': {
                'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {
                'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, (bid_price + ask_price) / 2)
            self.assertEqual((stock, bid_price, ask_price,
                             price), getDataPoint(quote))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'top_bid': {
                'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {
                'price': 117.87, 'size': 81}, 'stock': 'DEF'}
        ]
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            self.assertEqual(price, (bid_price + ask_price) / 2)
            self.assertEqual((stock, bid_price, ask_price,
                             price), getDataPoint(quote))

    # Additional Tests for getRatio
    def test_getRatio_priceAZero(self):
        self.assertEqual(getRatio(0, 1), 0)

    def test_getRatio_priceBZero(self):
        self.assertIsNone(getRatio(1, 0))

    def test_getRatio_bothPricesZero(self):
        self.assertIsNone(getRatio(0, 0))

    def test_getRatio_normalCondition(self):
        self.assertEqual(getRatio(2, 1), 2)

    def test_getRatio_largePriceA(self):
        self.assertEqual(getRatio(1000000, 1), 1000000)

    def test_getRatio_largePriceB(self):
        self.assertEqual(getRatio(1, 1000000), 1/1000000)

    def test_getRatio_decimalPrices(self):
        self.assertAlmostEqual(getRatio(1.5, 0.5), 3)


if __name__ == '__main__':
    unittest.main()
