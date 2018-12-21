from django.db import models
from django.http import HttpResponse,QueryDict
class User(models.Model):
    is_deleted=models.BooleanField(default=False)
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return (self.first_name +" " + self.last_name)
    @property
    def name(self):
        return self.first_name +" "+ self.last_name
    @property
    def basic_info(self):
        _basic_info={}
        _basic_info['id']=self.pk
        _basic_info['first_name']=self.first_name
        _basic_info['last_name']=self.last_name
        return _basic_info
class Base(models.Model):
	is_deleted=models.BooleanField(default=False)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)
	updated_by=models.ForeignKey(User,related_name="%(app_label)s_%(class)s_created")
	created_by=models.ForeignKey(User,related_name="%(app_label)s_%(class)s_updated")
	class Meta:
		abstract=True
class CT(Base):
    class Meta:
        verbose_name_plural='CT'
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    @property
    def get_all_ct(self):
        ct_list={}
        ct_list['CT ID']=self.pk
        ct_list['CT Name']=self.name
        return ct_list
class ExtraField(Base):
    class Meta:
        verbose_name_plural='ExtraField'
    INT=0
    CH=1
    DT=2
    DEC=3
    CHOICES=(
    ('INT','Number'),
    ('CH','Character'),
    ('DT','Date'),
    ('DEC','Decimal')
    )
    container_type=models.ForeignKey(CT)
    type=models.CharField(max_length=10,choices=CHOICES,default=1)
    name=models.CharField(max_length=255,null=True,blank=True)
    def __unicode__(self):
        return '%s--%s' % (self.name,self.container_type.name)
class CTInstance(models.Model):
    class Meta:
        verbose_name_plural='CTInstance'

    is_deleted=models.BooleanField(default=False)
    #ef_values = models.ForeignKey(Extrafield_values)
    ct=models.ForeignKey(CT)
    collection_many=models.ManyToManyField("self",blank=True)

    def __str__(self):
        return '%s--%s' % (self.pk,self.ct.name)
class Extrafield_values(models.Model):
    class Meta:
        verbose_name_plural='Values'

    #ct_instance = models.ForeignKey(CTInstance)
    extrafield=models.ForeignKey(ExtraField, related_name='ef_values')
    ct_instance=models.ForeignKey(CTInstance, related_name='ct_instance')
    value_int=models.IntegerField(null=True,blank=True)
    value_char=models.CharField(max_length=255,null=True,blank=True)
    value_date=models.DateTimeField(null=True,blank=True)
    value_dec=models.DecimalField(null=True,blank=True,max_digits=10, decimal_places=10)
    def __str__(self):
        return self.extrafield.name
class Relationship(Base):
    OTO=1
    OTM=2
    MTO=3
    MTM=4
    RELATION_CHOICES=((OTO,'One-to-One'),
                    (OTM,'One-to-Many'),
                    (MTM,'Many-to-Many'),
                    (MTO,'Many-to-One'),)
    parent_id=models.ForeignKey(CT,related_name='source_relationships')
    child_id=models.ForeignKey(CT,related_name='destination_relationships')
    relation_type=models.SmallIntegerField(choices=RELATION_CHOICES,default=1)
    def __unicode__(self):
        return '%s -- %s -->%s %s' % (self.pk,self.parent_id,self.child_id,self.get_relation_type_display())
    @property
    def is_oto(self):
        return True if self.relation_type==self.OTO else False
    @property
    def is_otm(self):
        return True if self.relation_type==self.OTM else False
    @property
    def is_mtm(self):
        return True if self.relation_type==self.MTM else False

# Move collection_many to CTInstance model




















    # return ef id, ef name, value, value id
