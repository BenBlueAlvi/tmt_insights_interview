from django.test.testcases import TestCase
from django.test.client import Client

'''
No preset test env? Would have been nice to have so I could spend more time on 
demonstrating writing code rather than debugging test setup
'''
class Tests(TestCase):
    def setUp(self):
        self.client = Client()

    def test1_inventory_dates(self):
        response = self.client.post(
            '/core/inventory-after-date/',
            {'date': "03/22/2020T12:23:31"}
        )

        self.assertEqual(response.status_code, 200)

    def test2_deactivate_order(self):
        response = self.client.post(
            '/core/deactivate-order/',
            {'id': 1}
        )

        self.assertEqual(response.status_code, 200)

    def test3_embargo_date(self):
        response = self.client.post(
            '/core/orders-between-embargo-dates/',
            {
                'start_date': "03/22/2020T12:23:31",
                'embargo_date': "03/22/2025T12:23:31",
             }
        )

        self.assertEqual(response.status_code, 200)