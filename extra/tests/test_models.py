from django.test import TestCase
from extra.models import CT,User,ExtraField,Extrafield_values,CTInstance,Relationship
from django.utils import timezone
class Usertest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.test1=User.objects.create(first_name='birju',last_name='deewakar')
	def setUp(self):
		self.test1.refresh_from_db()
	def test_first_name_label(self):
		field_label=self.test1._meta.get_field('first_name').verbose_name
		self.assertEqual(field_label,'first name')
	def test_last_name_label(self):
		field_label=self.test1._meta.get_field('last_name').verbose_name
		self.assertEqual(field_label,'last name')
	def test_str_method(self):
		self.assertEqual(self.test1.__str__(),self.test1.name)
	def test_length_of_first_name(self):
		max_length=self.test1._meta.get_field('first_name').max_length
		self.assertEqual(max_length,255)
class CTmodeltest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.test1=CT.objects.create(name='tester',created_by_id=1,updated_by_id=1,created_on=timezone.now(),updated_on=timezone.now())
	def setUp(self):
		self.test1.refresh_from_db()
	def test_ct(self):
		self.assertEqual(self.test1.__str__(),self.test1.name)
	def test_ct_name_length(self):
		max_length = self.test1._meta.get_field('name').max_length
		self.assertEqual(max_length,255)
class Extrafield_model_test(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.test1=ExtraField.objects.create(container_type_id=1,type='CH',name='tester',created_by_id=1,updated_by_id=1,created_on=timezone.now(),updated_on=timezone.now())
	def setUp(self):
		self.test1.refresh_from_db()
	def test_name_label(self):
		field_label=self.test1._meta.get_field('name').verbose_name
		self.assertEqual(field_label,'name')
	def test_ef_name_length(self):
		max_length=self.test1._meta.get_field('name').max_length
		self.assertEqual(max_length,255)






