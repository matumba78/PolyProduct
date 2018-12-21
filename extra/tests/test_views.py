from django.test import TestCase,RequestFactory
from ..models import CT,User,ExtraField,Extrafield_values,CTInstance,Relationship
from .. import views
from django.test import Client
from django.utils import timezone
class CTviewtest(TestCase):
	#import pdb;pdb.set_trace()
	@classmethod
	def setUpTestData(cls):
		cls.test1=CT.objects.create(name='testin1',created_by_id=1,updated_by_id=1,created_on=timezone.now(),updated_on=timezone.now())
	def setUp(self):
		self.test1.refresh_from_db()
	def test_ctview_gets_successfull_response_and_data(self):
		import pdb;pdb.set_trace()
		resp = self.client.get('/extra/container-types/')
		self.assertEqual(resp.status_code,200)
		request = RequestFactory().get('/')




	def test_post(self):
		data={'user_id':'1','container_name':'tester'}
		c=Client()
		response=c.post('/extra/container-types/',data=data)
		self.assertEqual(response.status_code,200)
		#test for status code
		self.assertEqual(response.resolver_match.func.__name__,'Container_types')
		#test for function view
