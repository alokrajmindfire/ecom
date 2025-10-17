import unittest
from unittest.mock import patch, mock_open
import main
import models as mx

class TestProductMain(unittest.TestCase):

    def setUp(self):
        self.electronic = mx.Electronics("E001", "Laptop", "Electronics", 1000.0, 10)
        self.clothing = mx.Clothing("C001", "T-Shirt", "Clothing", 50.0, 20)
        self.generic = mx.Product("P001", "Book", "Books", 20.0, 5)

    @patch("builtins.open", new_callable=mock_open, read_data="E001,Laptop,Electronics,1000,10\nC001,T-Shirt,Clothing,50,20\n")
    def test_load_products(self, mock_file):
        products = main.load_products("dummy.txt")
        self.assertEqual(len(products), 2)
        self.assertIsInstance(products[0], mx.Electronics)
        self.assertIsInstance(products[1], mx.Clothing)

    @patch("builtins.open", new_callable=mock_open)
    def test_write_product(self, mock_file):
        main.write_product("test,data")
        mock_file().write.assert_called_once_with("test,data\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_order(self, mock_file):
        main.write_order("order,test")
        mock_file().write.assert_called_once_with("order,test\n")

    @patch("builtins.input", side_effect=["dummy.txt", "Alice", "alice@email.com", "E001", "2"])
    @patch("builtins.print")
    @patch("main.load_products")
    @patch("main.write_order")
    def test_main_order_success(self, mock_write_order, mock_load_products, mock_print, mock_input):
        mock_load_products.return_value = [self.electronic]

        main.main()

        mock_write_order.assert_called_once()
        self.assertTrue(any("Order placed successfully" in str(call) for call in mock_print.call_args_list))

    @patch("builtins.input", side_effect=["dummy.txt", "Alice", "alice@email.com", "INVALID", "2"])
    @patch("builtins.print")
    @patch("main.load_products")
    @patch("main.write_order")
    def test_main_invalid_product(self, mock_write_order, mock_load_products, mock_print, mock_input):
        mock_load_products.return_value = [self.electronic]
        main.main()
        self.assertTrue(any("Product ID not found" in str(call) for call in mock_print.call_args_list))
        mock_write_order.assert_not_called()

if __name__ == "__main__":
    unittest.main()
