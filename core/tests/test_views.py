from django.test import TestCase, Client
from django.core.urlresolvers import reverse # vai indicar a url atraves de um nome

def IndexViewTestCase(TestCase):
    # esse metodo vai ser execuatdo para cada teste
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self): # toda vez que acaba um teste
        pass

    def test_status_code(self):
        response = self.client.get(self.url) # para nao ter que ficar passando a url sempre
        #assertEquals é para ver se o response.status_code bate com 200
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertEqualsUsed(response, 'index.html')
