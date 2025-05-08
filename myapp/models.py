from django.db import models
from django_mysql.models import ListTextField
from datetime import datetime
# Create your models here.


class service(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class service_item(models.Model):
    service_data=models.ForeignKey(service,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(upload_to="image")

    def __str__(self) -> str:
        return self.name



class blog_categories(models.Model):
    category_name=models.CharField(max_length=250,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self) -> str:
        return self.category_name


class blog(models.Model):
    blog_category_data=models.ForeignKey(blog_categories,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(upload_to="image")
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self) -> str:
        return self.title



class nft_barriers(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    image=models.ImageField(upload_to="image")

    def __str__(self) -> str:
        return self.name

class contact_us(models.Model):
    name=models.CharField(max_length=250,db_index=True)
    email=models.EmailField()
    country=models.CharField(max_length=250)
    phone_no=models.BigIntegerField()
    message=models.TextField()

    def __str__(self) -> str:
        return self.name

class berries_structure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    berry_type = models.CharField(max_length=50)
    farm_code = models.CharField(max_length=50)
    batch_id = models.CharField(max_length=50)
    harvest_date = models.CharField(max_length=50)
    quantity_grams = models.IntegerField(blank=True,null=True)
    certifications = ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    carbon_offset_kg = models.FloatField(blank=True,null=True)
    grower = models.CharField(max_length=100)
    traceability_qr  = models.CharField(max_length=100)
    current_owner = models.CharField(max_length=100)
    utility_tags = ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)

    def save(self, *args, **kwargs):
        try:
            # Convert string to datetime object if format is valid
            date_obj = datetime.strptime(self.harvest_date, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%Y%m%d")
        except Exception:
            formatted_date = "UNKNOWN"

        self.name = f"APX-{self.berry_type.upper()}-{self.farm_code}-{self.batch_id}-{formatted_date}"
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name


class admin_login(models.Model):
    email=models.EmailField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.email


class ad(models.Model):
    file=models.FileField(upload_to="image")
    type = models.CharField(max_length=500,blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    sub_title = models.CharField(max_length=500,blank=True, null=True)






class user_document(models.Model):
    user_data = models.OneToOneField("user",on_delete=models.CASCADE,related_name="kyc_document")
    aadhar_card_front=models.FileField(upload_to="user_doc",blank=True,null=True)
    aadhar_card_back=models.FileField(upload_to="user_doc",blank=True,null=True)
    pan_card_front=models.FileField(upload_to="user_doc",blank=True,null=True)
    driving_licence=models.FileField(upload_to="user_doc",blank=True,null=True)


class user(models.Model):
    user_id=models.CharField(max_length=100,blank=True,null=True)
    device_token=models.CharField(max_length=250,blank=True,null=True)
    name=models.CharField(max_length=100)
    mobile_no=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    date_time=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="image",blank=True,null=True)
    aadhar_card_no=models.CharField(max_length=100,blank=True,null=True)
    pan_card_no=models.CharField(max_length=100,blank=True,null=True)


class token(models.Model):
    price=models.IntegerField()


class grower(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    farm_code=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
    
class certifications(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
    
class utility_tags(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
    
    
    
class berry_types(models.Model):
    type=models.CharField(max_length=100,blank=True,null=True)
    nft_code=models.CharField(max_length=100,blank=True,null=True)
    nft_label=models.CharField(max_length=100,blank=True,null=True)
    batch_id=models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.type
    
    
    
class berry_batch(models.Model):
    description = models.TextField(blank=True, null=True)
    berry_type = models.ForeignKey(berry_types, on_delete=models.SET_NULL, null=True, blank=True)
    # batch_id = models.CharField(max_length=100, blank=True, null=True)
    harvest_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    quantity_grams = models.IntegerField(blank=True, null=True)
    carbon_offset_kg = models.FloatField(blank=True, null=True)
    traceability_qr = models.CharField(max_length=100, blank=True, null=True)
    current_owner = models.CharField(max_length=100, blank=True, null=True)
    farm_code = models.ForeignKey(grower, on_delete=models.SET_NULL, null=True, blank=True)
    certifications = models.ManyToManyField(certifications, blank=True)
    utility_tags = models.ManyToManyField(utility_tags, blank=True)

    def __str__(self):
        return f"{self.berry_type}"