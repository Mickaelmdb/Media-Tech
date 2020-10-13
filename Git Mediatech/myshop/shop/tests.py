from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Category, Product
from django.core.urlresolvers import reverse
#Ma home page doit me renvoyer un code de statut 200 car elle fonctionne 
#Ma page detail doit me renvoyer un code 200 si mon article existe 
#Ma page detail doit me renvoyer un code 404 si mon article n'existe pas 


class ProductPageTestCase(TestCase):
    def test_product_page(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

