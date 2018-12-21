from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,QueryDict
from .models import CT,User,ExtraField,Extrafield_values,CTInstance,Relationship
import pdb,json
from django.db.models import Sum
from django.db import connection
from django.core import serializers

# Create your views here.
class Adduser(View):
	def post(self,request):
		first_name=request.POST["first_name"]
		last_name=request.POST["last_name"]
		data=User(first_name=first_name,last_name=last_name)
		data.save()
		return HttpResponse("User Created Successfully",status=200)
	def get(self,request):
		obj=User.objects.all()
		dict_a = {"data":obj}
		if obj:
			res=[]
			for i in obj:
				res.append({
				'User Name':i.name
				})
			#return HttpResponse(json.dumps(res),content_type='application/json',status=200)
			return render(request,'index.html',context = dict_a)
class Container_types(View):
	def get(self,request):
		obj=CT.objects.all()
		#a=serializers.serialize("json",CT.objects.all())
		if obj:
			#print obj
			res=[]
			for i in obj:
				res.append({
					'Container Type':i.name

					})
			print obj[0].get_all_ct
			return HttpResponse(json.dumps(res),content_type='application/json',status=200)
		else:
			HttpResponse("No Container Found")
	def post(self,request):
		user_id=request.POST["user_id"]
		container_name=request.POST["container_name"]
		if CT.objects.filter(name=container_name):
			return HttpResponse("Container already Exists")
		try:
			obj=User.objects.get(pk=user_id)
			if obj:
				data=CT(created_by_id=obj.pk,updated_by_id=obj.pk,name=container_name)
				data.save()
				return HttpResponse(json.dumps(str(data))+" "+"Container Created Successfully",content_type='application/json',status=201)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")
	def put(self,request):
		try:
			ct_id=request.GET.get('ct_id','0')
			data=QueryDict(request.body)
			ct_object=CT.objects.get(pk=ct_id,is_deleted=False)
			if ct_object:
				ct_object.name=data['container_name']
				ct_object.save()
				return HttpResponse("Updated Successful",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")
	def delete(self,request):
		try:
			ct_id=request.GET.get('ct_id','0')
			ct_object=CT.objects.get(pk=ct_id,is_deleted=False)
			print ct_object
			if ct_object:
				ct_object.is_deleted=True
				ct_object.save()
				#print ct_object.is_deleted
				return HttpResponse("Container Deleted Successfully",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")


class Extrafield_instance(View):
	def get(self,request,ct_id):
		obj=ExtraField.objects.filter(container_type_id=ct_id).select_related('container_type')
		res=[]
		tes=[]
		if obj:
			tes.append({
				'Conatiner Type':obj[0].container_type.name
				})
			for i in obj:
				res.append({
					'Extra Field':i.name
					})
			tes.append(res)
			print len(connection.queries)
			return HttpResponse(json.dumps(tes),content_type='application/json',status=200)
		else:
			return HttpResponse("Wrong Container ID")
	def post(self,request,ct_id):
		print ct_id
		try:
			#print "SDSSAD"
			obj=CT.objects.get(pk=ct_id)
			print obj
			ef_name=request.POST["extrafield_name"]
			data_type=request.POST["data_type"]
			data=ExtraField(name=ef_name,type=data_type,created_by_id=obj.created_by.pk,updated_by_id=obj.updated_by.pk,container_type_id=obj.pk)
			data.save()
			return HttpResponse(json.dumps(str(data))+" "+"Extra Field Created Successfully",content_type='application/json',status=201)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist",status=200)
	def put(self,request):
		try:
			ef_id=request.GET.get('ef_id','0')
			ef_object=ExtraField.objects.get(pk=ef_id)
			data=QueryDict(request.body)
			ef_object.name=data['ef_name']
			ef_object.save()
			return HttpResponse("Updated Successful",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")
	def delete(self,request):
		try:
			ef_id=request.GET.get('ef_id','0')
			ef_object=ExtraField.objects.get(pk=ef_id,is_deleted=False)
			ef_object.is_deleted=True
			ef_object.save()
			#print ct_object.is_deleted
			return HttpResponse("Container Deleted Successfully",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")



class Container_types_instance(View):
	def post(self,request,ct_id):
		obj=ExtraField.objects.filter(container_type_id=ct_id)
		ct_instance_data=CTInstance(ct_id=ct_id)
		ct_instance_data.save()
		user_data=QueryDict(request.body)
		#print request.POST[obj[1].name]
		for i in obj:
			if request.POST[i.name] and i.type=='CH':
				store_data=Extrafield_values(value_char=request.POST[i.name],extrafield_id=i.pk,ct_instance_id=ct_instance_data.pk)
				store_data.save()
			elif request.POST[i.name] and i.type=='INT':
				 store_data=Extrafield_values(value_int=request.POST[i.name],extrafield_id=i.pk,ct_instance_id=ct_instance_data.pk)
				 store_data.save()
			elif request.POST[i.name] and i.type=='DT':
				 store_data=Extrafield_values(value_date=request.POST[i.name],extrafield_id=i.pk,ct_instance_id=ct_instance_data.pk)
				 store_data.save()
			elif request.POST[i.name] and i.type=='DEC':
				 store_data=Extrafield_values(value_dec=request.POST[i.name],extrafield_id=i.pk,ct_instance_id=ct_instance_data.pk)
				 store_data.save()
			else:
				return HttpResponse("Error")
			#print store_data.extrafield.pk
		return HttpResponse("Successful")
	def get(self,request,ct_id):
		#import pdb;pdb.set_trace()
		#print len(connection.queries)
		cti_object=CTInstance.objects.filter(ct_id=ct_id).select_related('ct')
		result=[]
		if cti_object:
			for i in cti_object:
				ef_object=Extrafield_values.objects.filter(ct_instance_id=i.pk).select_related('extrafield','ct_instance')
				data=[]
				result.append({
					"container_type":i.ct.name,
					"id":i.pk,
					"data":data,
					})
				for j in ef_object:
					if j.value_char:
						value=j.value_char
					if j.value_int:
						value=j.value_int
					if j.value_dec:
						value=j.value_dec
					if j.value_date:
						value=j.value_date
					data.append({
						"ef_id":j.extrafield_id,
						"ef_name":j.extrafield.name,
						"ef_value":str(value),
						"id":j.pk
						})
				#data.append(tes)
				#result.append(res)
				print len(connection.queries)
			return HttpResponse(json.dumps(result),content_type='application/json',status=200)
		else:
			return HttpResponse("No ExtraField for the mentioned Container Type Instance/Container Instance Type Does Not Exist")
	def put(self,request,ci_id):
		try:
			ci_object=CTInstance.objects.get(pk=ci_id)
			data=QueryDict(request.body)
			ef_object=Extrafield_values.objects.filter(ct_instance_id=ci_id).select_related('extrafield','ct_instance')
			#print ef_object[0]
			for i in ef_object:
				if data[i.extrafield.name] and i.extrafield.type=='CH':
					i.value_char=data[i.extrafield.name]
					#print i.value_char
					i.save()
				elif data[i.extrafield.name] and i.extrafield.type=='INT':
					i.value_int=data[i.extrafield.name]
					i.save()
				elif data[i.extrafield.name] and i.extrafield.type=='DT':
					i.value_date=data[i.extrafield.name]
					i.save()
				elif data[i.extrafield.name] and i.extrafield.type=='DEC':
					i.value_dec=data[i.extrafield.name]
					i.save()
				else:
					return HttpResponse("Error")
				#print len(connection.queries)
			return HttpResponse("Updation Successful",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist",status=200)
	def delete(self,request,ci_id):
		try:
			ci_object=CTInstance.objects.get(pk=ci_id)
			ci_object.is_deleted=True
			ci_object.save()
			return HttpResponse("CT Instance Deleted Successful",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("Object Does Not Exist")
class Extrafield_operations(View):
	def get(self,request):
		ct_id=request.GET.get('ct_id','0')
		ef=request.GET.get('ef','0')
		value=request.META
		obj=CT.objects.all()
		print value

		print obj
		data=Extrafield_values.objects.filter(ct_instance_id=ct_id,extrafield__name=ef)
		obj=User.objects.all()
		q=obj[1].basic_info
		print q
		print data
		return HttpResponse(q)
class Relationship_view(View):
	def post(self,request):
		try:
			data=QueryDict(request.body)
			object_parent=CT.objects.get(pk=data['parent_ct'])
			object_child=CT.objects.get(pk=data['child_ct'])
			object_relation=Relationship.objects.filter(parent_id_id=object_parent.pk,child_id_id=object_child.pk)
			if object_relation:
				return HttpResponse("Relation Already Exist",status=200)
			else:
				if data['exclusive']=='True' and data['multiple_allowed']=='True':
					store_relation=Relationship(parent_id_id=object_parent.pk,child_id_id=object_child.pk,created_by_id=object_parent.created_by.pk,updated_by_id=object_parent.updated_by.pk,relation_type=Relationship.MTM)
					store_relation.save()
				elif data['exclusive']=='True' and data['multiple_allowed']=='False':
					store_relation=Relationship(parent_id_id=object_parent.pk,child_id_id=object_child.pk,created_by_id=object_parent.created_by.pk,updated_by_id=object_parent.updated_by.pk,relation_type=Relationship.OTM)
					store_relation.save()
					print store_relation
				elif data['exclusive']=='False' and data['multiple_allowed']=='True':
					store_relation=Relationship(parent_id_id=object_parent.pk,child_id_id=object_child.pk,created_by_id=object_parent.created_by.pk,updated_by_id=object_parent.updated_by.pk,relation_type=Relationship.MTO)
					store_relation.save()
				elif data['exclusive']=='False' and data['multiple_allowed']=='False':
					store_relation=Relationship(parent_id_id=object_parent.pk,child_id_id=object_child.pk,created_by_id=object_parent.created_by.pk,updated_by_id=object_parent.updated_by.pk,relation_type=Relationship.OTO)
					store_relation.save()
				else:
					return HttpResponse("Error")
		
			return HttpResponse("Relationship Established",status=200)
		except ObjectDoesNotExist:
			return HttpResponse("ObjectDoesNotExist",status=200)
	def put(self,request):
		try:
			data=QueryDict(request.body)
			object_parent=CT.objects.get(pk=data['parent_ct'])
			object_child=CT.objects.get(pk=data['child_ct'])
			object_relation=Relationship.objects.get(parent_id_id=object_parent.pk,child_id_id=object_child.pk)
			print object_relation.is_otm
			if data['exclusive']=='True' and data['multiple_allowed']=='True':
				object_relation.relation_type=4
				object_relation.save()
			elif data['exclusive']=='True' and data['multiple_allowed']=='False' and object_relation.is_oto:
				object_relation.relation_type=2
				object_relation.save()
			elif data['exclusive']=='False' and data['multiple_allowed']=='True' and object_relation.is_oto:
				object_relation.relation_type=3
				object_relation.save()
			elif data['exclusive']=='False' and data['multiple_allowed']=='False':
				return HttpResponse("Not Allowed as there are already Existing Relations")
			else:
				return HttpResponse("Not Allowed")
			return HttpResponse("Updation Successful")
		except ObjectDoesNotExist:
			return HttpResponse("ObjectDoesNotExist",status=200)
class RuntimeR(View):
	def put(self,request,ci_id):
		try:
			#import pdb;pdb.set_trace()
			early_list=[]
			data=QueryDict(request.body)
			_list=data['child_id'].split(",")
			_list_len=len(_list)
			get_cti_object=CTInstance.objects.filter(pk__in=_list)
			get_same_cti=get_cti_object.filter(ct_id=get_cti_object[0].ct.pk)

			#print get_same_cti,get_cti_object
			if len(get_cti_object)==len(get_same_cti):	
			# Except child ct id from user
			# all the child instance ids should be of one child ct id mentioned
			# make all queries outside for loop
				get_ct_parent=CTInstance.objects.get(pk=ci_id)
				#get_ct_child=CTInstance.objects.get(pk=child_ci_id)
				parent_object=CTInstance.objects.get(pk=get_ct_parent.pk)
				relation_obj=Relationship.objects.get(parent_id=get_ct_parent.ct.pk,child_id=get_same_cti[0].ct.pk)
				if relation_obj.is_oto:
					if len(_list) != 1:
						return HttpResponse("you can attach only one child", status=400)
					child_object=CTInstance.objects.get(pk__in=_list)
					if CTInstance.objects.filter(pk__in=_list).exclude(pk=child_object.pk):
						return HttpResponse("requested child already attached to different parent",status=400)
					if parent_object:
						if parent_object.collection_many.filter(ct_id=child_object.ct.pk).count() >= 1:
							return HttpResponse("requested parent can only have one collection",status=400)
						else:
							parent_object.collection_many.add(child_object)
							return HttpResponse("child attached to parent successfully",status=200)
				elif relation_obj.is_mtm:
					for collection_many in parent_object.collection_many.all():
						early_list.append(collection_many.pk)
					_old_list=map(unicode,early_list)
					diff_list=list(set(_list)-set(_old_list))
					if diff_list:
						obj_new=get_cti_object.filter(pk__in=diff_list)
						print obj_new
						for i in obj_new:
							parent_object.collection_many.add(i)
						#parent_object.save()
						#add_runtime[0].collection_many.add(get_ct_child)
						return HttpResponse("successfully added collection",status=200)
					else:
						return HttpResponse("mentioned collection already present",status=200)
				elif relation_obj.is_otm:
					obj_otm=CTInstance.objects.filter(ct_id=parent_object.ct.pk)
					for i in obj_otm:
						for collection_many in i.collection_many.all():
							early_list.append(collection_many.pk)
					_old_list=map(unicode,early_list)
					print _list
					print _old_list
					diff_list=list(set(_list)-set(_old_list))
					print diff_list
					if diff_list:
						obj_new=get_cti_object.filter(pk__in=diff_list)
						for i in obj_new:
							parent_object.collection_many.add(i)
						return HttpResponse("successfully added collection",status=200)
					else:
						return HttpResponse("mentioned collection already present",status=200)
				else:
					return HttpResponse("Error")
			else:
				return HttpResponse("choices are valid only for same type of collections",status=400)
		except ObjectDoesNotExist:
			return HttpResponse("ObjectDoesNotExist") 
	def get(self,request,ci_id):
		print len(connection.queries)
		cti_parent=CTInstance.objects.get(pk=ci_id)
		col_object=cti_parent.collection_many.all().select_related('ct')
		from collections import defaultdict
		group_collection=defaultdict(list)
		for i in col_object:
			group_collection[i.ct.name].append(i.pk)
		_extrafield_values=Extrafield_values.objects.all().select_related('ct_instance','extrafield')
		#cti_list=RuntimeRelation.objects.get(parent_id=ci_id)
		data=[]
		res = {
			"Parent_name":cti_parent.ct.name,
			"Parent_id":cti_parent.id,
			"Collection":data,
			}
		for col in group_collection:
			ef_data=[]
			data.append({
				"Collection_name":col,
				"Data":ef_data,
				})
	
			ef_object=_extrafield_values.filter(ct_instance_id__in=group_collection[col])
			for j in ef_object:
				if j.value_char:
					value=j.value_char
				if j.value_int:
					value=j.value_int
				if j.value_dec:
					value=j.value_dec
				if j.value_date:
					value=j.value_date
				ef_data.append({
					"ef_id":j.extrafield_id,
					"ef_name":j.extrafield.name,
					"ef_value":str(value),
					"id":j.pk
					}) 
			print len(connection.queries)
		return HttpResponse(json.dumps(res))





















