from django.test import TestCase

# Create your tests here.
class SortTest(TestCase):
    def setUP(self):
        self.shippers = Shippers.objects.create(name= 'Joni')
        self.transporters = Transporters.objects.create(name= 'Sejahtera')
        self.job1 = Jobs.objects.create(
            origin =  'JKT',
            destination = 'JOG',
            ship_date = '12/12/2019',
            budget = 8000000,
            description = 'JKT-JOG',
            status = 'Acc',
            shippers = self.shippers
        )
        self.job2 = Jobs.objects.create(
            origin =  'JKT',
            destination = 'JOG',
            ship_date = '09/12/2019',
            budget = 8000000,
            description = 'JKT-JOG',
            status = 'Acc',
            shippers = self.shippers
        )
        self.job3 = Jobs.objects.create(
            origin =  'JKT',
            destination = 'JOG',
            ship_date = '20/12/2019',
            budget = 8000000,
            description = 'JKT-JOG',
            status = 'Acc',
            shippers = self.shippers
        )

        self.bid1 = Bids.objects.create(
            price = 8000000,
            vehicle = 'Kargo',
            description = 'TErbaik',
            transporters = self.transporters,
            jobs = self.job1
        )
        self.bid2 = Bids.objects.create(
            price = 7000000,
            vehicle = 'Kargo',
            description = 'TErbaik',
            transporters = self.transporters,
            jobs = self.job2
        )
        self.bid3 = Bids.objects.create(
            price = 9000000,
            vehicle = 'Kargo',
            description = 'TErbaik',
            transporters = self.transporters,
            jobs = self.job3
        )

        result = [
            {
                'origin': 'JKT',
                'destination': 'JOG',
                'ship_date': '09/12/2019',
                'budget': 8000000,
                'description': 'JKT-JOG',
                'status': 'Acc',
                'shippers': 'Joni'
            },
            {
                'origin': 'JKT',
                'destination': 'JOG',
                'ship_date': '12/12/2019',
                'budget': 8000000,
                'description': 'JKT-JOG',
                'status': 'Acc',
                'shippers': 'Joni'
            },
            {
                'origin': 'JKT',
                'destination': 'JOG',
                'ship_date': '20/12/2019',
                'budget': 8000000,
                'description': 'JKT-JOG',
                'status': 'Acc',
                'shippers': 'Joni'
            }
        ]

        result2 = [
            {
                'price': 7000000,
                'vehicle': 'Kargo',
                'description': 'TErbaik',
                'transporters': 'Sejahtera',
                'jobs': '09/12/2019'
            },
            {
                'price': 8000000,
                'vehicle': 'Kargo',
                'description': 'TErbaik',
                'transporters': 'Sejahtera',
                'jobs': '12/12/2019'
            },
            {
                'price': 9000000,
                'vehicle': 'Kargo',
                'description': 'TErbaik',
                'transporters': 'Sejahtera',
                'jobs': '20/12/2019'
            }
        ]
    
        response = self.client.get(reverse('jobs'))
        self.assertEqual(response.data, result)

        response = self.client.get(reverse('bids'))
        self.assertEqual(response.data, result2)