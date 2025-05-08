
from rest_framework import serializers
from .models import *
import pytz
class service_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)


    class Meta:
        models=service
        fields ='__all__'


    def create(self, validated_data):
        return service.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance

class service_item_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    service_data = serializers.SlugRelatedField(slug_field='id', queryset=service.objects.all(), required=True)
    name=serializers.CharField(max_length=250,required=True)
    description=serializers.CharField(required=True)
    image=serializers.ImageField(required=False)


    class Meta:
        models=service_item
        fields ='__all__'


    def create(self, validated_data):
        return service_item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service_data=validated_data.get('service_data',instance.service_data)
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.image=validated_data.get('image',instance.image)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["service_data"] = service_serializers(instance.service_data).data
        return representation

class blog_categories_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    category_name=serializers.CharField(max_length=250,required=True)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        models=blog_categories
        fields ='__all__'
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
            local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
            local_dt = obj.timestamp.astimezone(local_tz)
            return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return blog_categories.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name=validated_data.get('category_name',instance.category_name)
        instance.save()
        return instance




class blog_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    blog_category_data = serializers.SlugRelatedField(slug_field='id', queryset=blog_categories.objects.all(), required=True)
    title=serializers.CharField(max_length=250,required=True)
    description=serializers.CharField(required=False)
    image=serializers.ImageField(required=False)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        models=blog
        fields ='__all__'
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
            local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
            local_dt = obj.timestamp.astimezone(local_tz)
            return local_dt.strftime('%Y-%m-%d %H:%M:%S')


    def create(self, validated_data):
        return blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.blog_category_data = validated_data.get('blog_category_data', instance.blog_category_data)
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)
        instance.image=validated_data.get('image',instance.image)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["blog_category_data"] = blog_categories_serializers(instance.blog_category_data).data
        return representation
    
class nft_barriers_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
    description=serializers.CharField(required=True)
    image=serializers.ImageField(required=False)


    class Meta:
        models=nft_barriers
        fields ='__all__'


    def create(self, validated_data):
        return nft_barriers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.image=validated_data.get('image',instance.image)
        instance.save()
        return instance



class contact_us_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(max_length=250,required=True)
    email=serializers.EmailField(required=True)
    country=serializers.CharField(max_length=250,required=True)
    phone_no=serializers.IntegerField()
    message=serializers.CharField(required=True)



    class Meta:
        models=contact_us
        fields ='__all__'


    def create(self, validated_data):
        return contact_us.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.phone_no=validated_data.get('phone_no',instance.phone_no)
        instance.country=validated_data.get('country',instance.country)
        instance.message=validated_data.get('message',instance.message)
        instance.save()
        return instance


class berries_structure_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(read_only=True)  # auto-generated in save()
    description = serializers.CharField(required=True)
    berry_type = serializers.CharField(required=True)
    farm_code = serializers.CharField(required=True)
    batch_id = serializers.CharField(required=True)
    harvest_date = serializers.CharField(required=True)
    quantity_grams = serializers.IntegerField(required=True)
    certifications = serializers.ListField(
        child=serializers.CharField(allow_null=True, allow_blank=True),
        allow_null=True,
        required=True
    )
    carbon_offset_kg = serializers.FloatField(required=True)
    grower = serializers.CharField(required=True)
    traceability_qr = serializers.CharField(required=True)
    current_owner = serializers.CharField(required=True)
    utility_tags = serializers.ListField(
        child=serializers.CharField(allow_null=True, allow_blank=True),
        allow_null=True,
        required=True
    )
    class Meta:
        models=berries_structure
        fields ='__all__'


    def create(self, validated_data):
        return berries_structure.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.berry_type = validated_data.get('berry_type', instance.berry_type)
        instance.farm_code = validated_data.get('farm_code', instance.farm_code)
        instance.batch_id = validated_data.get('batch_id', instance.batch_id)
        instance.harvest_date = validated_data.get('harvest_date', instance.harvest_date)
        instance.quantity_grams = validated_data.get('quantity_grams', instance.quantity_grams)
        instance.certifications = validated_data.get('certifications', instance.certifications)
        instance.carbon_offset_kg = validated_data.get('carbon_offset_kg', instance.carbon_offset_kg)
        instance.grower = validated_data.get('grower', instance.grower)
        instance.traceability_qr = validated_data.get('traceability_qr', instance.traceability_qr)
        instance.current_owner = validated_data.get('current_owner', instance.current_owner)
        instance.utility_tags = validated_data.get('utility_tags', instance.utility_tags)

        instance.save()
        return instance


class admin_login_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=50,required=True)
    password=serializers.CharField(max_length=50,required=True)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        models=admin_login
        fields ='__all__'
        exclude = ('id',)
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return admin_login.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance


class ad_serializers(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    type = serializers.CharField(required=False)
    title = serializers.CharField(required=False, allow_blank=True)
    sub_title = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = ad
        fields = ['id', 'file', 'type', 'title', 'sub_title']

    def create(self, validated_data):
        return ad.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.file = validated_data.get('file', instance.file)
        instance.type = validated_data.get('type', instance.type)
        instance.title = validated_data.get('title', instance.title)
        instance.sub_title = validated_data.get('sub_title', instance.sub_title)
        instance.save()
        return instance




class user_document_Serializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    aadhar_card_front=serializers.ImageField(required=False)
    aadhar_card_back=serializers.ImageField(required=False)
    pan_card_front=serializers.ImageField(required=False)
    driving_licence=serializers.ImageField(required=False)


    class Meta:
        models = user_document
        fields =["id","aadhar_card_front","aadhar_card_back","pan_card_front","driving_licence"]
        exclude = ('id',)


class user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=True)
    name=serializers.CharField(max_length=100,required=True)
    email=serializers.CharField(max_length=100,required=True)
    mobile_no = serializers.IntegerField(required=True)
    device_token=serializers.CharField(max_length=255,required=True)
    image=serializers.ImageField(required=False)
    date_time = serializers.SerializerMethodField()
    aadhar_card_no=serializers.CharField(max_length=100,required=False)
    pan_card_no=serializers.CharField(max_length=100,required=False)
    kyc_document = user_document_Serializer(required=False)
    class Meta:
        models=user
        fields ='__all__'
        read_only_fields = ['date_time']
    def get_date_time(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.date_time.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')


    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.device_token = validated_data.get('device_token', instance.device_token)
        instance.image = validated_data.get('image', instance.image)
        instance.aadhar_card_no = validated_data.get('aadhar_card_no', instance.aadhar_card_no)
        instance.pan_card_no = validated_data.get('pan_card_no', instance.pan_card_no)
        document_data = validated_data.pop('kyc_document', None)
        print(document_data, "doc")

        if document_data:
            user_document1, _ = user_document.objects.get_or_create(user_data=instance)
            for attr, value in document_data.items():
                setattr(user_document1, attr, value)
            user_document1.save()

        instance.save()
        return instance

class token_serializers(serializers.ModelSerializer):
    price = serializers.FloatField(required=True)
    class Meta:
        model = token
        fields = ['id', 'price']

    def create(self, validated_data):
        return token.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
       
        instance.save()
        return instance
    
    
class grower_serializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
    farm_code = serializers.CharField(required=True)
    
    class Meta:
        model = grower
        fields = ['id', 'name',"farm_code"]

    def create(self, validated_data):
        return grower.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.farm_code = validated_data.get('farm_code', instance.farm_code)
        
       
        instance.save()
        return instance
    
    
class certifications_serializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
   
    
    class Meta:
        model = certifications
        fields = ['id', 'name']

    def create(self, validated_data):
        return certifications.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
    
        instance.save()
        return instance


class utility_tags_serializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
   
    
    class Meta:
        model = utility_tags
        fields = ['id', 'name']

    def create(self, validated_data):
        return utility_tags.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
    
        instance.save()
        return instance
    
    

class berry_types_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    type=serializers.CharField(max_length=100,required=True)
    nft_code=serializers.CharField(max_length=100,required=True)
    nft_label=serializers.CharField(max_length=100,required=True)
    batch_id=serializers.CharField(max_length=100,required=True)
    class Meta:
        model = berry_types
        fields = "__all__"

    def create(self, validated_data):
        return berry_types.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.nft_code = validated_data.get('nft_code', instance.nft_code)
        instance.nft_label = validated_data.get('nft_label', instance.nft_label)
        instance.batch_id = validated_data.get('batch_id', instance.batch_id)
       
        instance.save()
        return instance
    
    
class BerryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = berry_types
        fields = ['id', 'type', 'nft_code', 'nft_label', 'batch_id']


class GrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = grower
        fields = ['id', 'name', 'farm_code']


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = certifications
        fields = ['id', 'name']


class UtilityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = utility_tags
        fields = ['id', 'name']

class berry_batch_serializers(serializers.ModelSerializer):
    berry_type = serializers.PrimaryKeyRelatedField(queryset=berry_types.objects.all(), required=False)
    farm_code = serializers.PrimaryKeyRelatedField(queryset=grower.objects.all(), required=False)
    certifications = serializers.PrimaryKeyRelatedField(queryset=certifications.objects.all(), many=True, required=False)
    utility_tags = serializers.PrimaryKeyRelatedField(queryset=utility_tags.objects.all(), many=True, required=False)
    harvest_date=serializers.SerializerMethodField()
    
    class Meta:
        model = berry_batch
        fields = "__all__"
        read_only_fields = ['harvest_date']
    def get_harvest_date(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.harvest_date.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')
    def create(self, validated_data):
        certifications_data = validated_data.pop('certifications', [])
        utility_tags_data = validated_data.pop('utility_tags', [])
        
        batch = berry_batch.objects.create(**validated_data)
        batch.certifications.set(certifications_data)
        batch.utility_tags.set(utility_tags_data)
        return batch

    def update(self, instance, validated_data):
        certifications_data = validated_data.pop('certifications', None)
        utility_tags_data = validated_data.pop('utility_tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if certifications_data is not None:
            instance.certifications.set(certifications_data)
        if utility_tags_data is not None:
            instance.utility_tags.set(utility_tags_data)

        instance.save()
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Replace FK fields with nested representations
        representation['berry_type'] = BerryTypeSerializer(instance.berry_type).data if instance.berry_type else None
        representation['farm_code'] = GrowerSerializer(instance.farm_code).data if instance.farm_code else None
        representation['certifications'] = CertificationSerializer(instance.certifications.all(), many=True).data
        representation['utility_tags'] = UtilityTagSerializer(instance.utility_tags.all(), many=True).data
        return representation 