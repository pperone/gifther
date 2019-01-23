from django.test import TestCase
from .models import Product
from decimal import *


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            picture="http://www.image.com/image.jpg",
            name="Purse",
            description="This is a description.",
            price=199.99,
            woman=('{mother}'),
            occasion=('{birthday christmas}'),
            profile=('{fashion elegance}')
        )

        Product.objects.create(
            picture="http://www.image.com/image2.jpg",
            name="Bracelet",
            description="This is a description.",
            price=299.99,
            woman=('{wife girlfriend}'),
            occasion=('{birthday anniversary}'),
            profile=('{fashion elegance}')
        )


    def test_products(self):
        purse = Product.objects.get(name="Purse")
        bracelet = Product.objects.get(name="Bracelet")

        self.assertEqual(purse.description, 'This is a description.')
        self.assertEqual(bracelet.price, Decimal('299.99'))
