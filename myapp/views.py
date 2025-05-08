from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class test(APIView):
    def get(self,request):
        return Response({"msg":"Done"})



class service_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = service.objects.get(id=id)
                serializer = service_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except service.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = service.objects.all().order_by("-id")
            serializer = service_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = service_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = service.objects.get(id=id)
        except service.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = service_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = service.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except service.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})



class service_item_view(APIView):
    def get(self, request, id=None , service_id=None):
        if id:
            try:
                uid = service_item.objects.get(id=id)
                serializer = service_item_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except service_item.DoesNotExist:
                return Response({'status': "Invalid"})
        elif service_id:
            try:
                uid = service_item.objects.filter(service_data__id=service_id)
                print(uid)
                serializer = service_item_serializers(uid,many=True)
                return Response({'status': 'success', 'data': serializer.data})
            except service_item.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = service_item.objects.all().order_by("-id")
            serializer = service_item_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = service_item_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = service_item.objects.get(id=id)
        except service_item.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = service_item_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = service_item.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except service_item.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

#=============
class blog_categories_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = blog_categories.objects.get(id=id)
                serializer = blog_categories_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except blog_categories.DoesNotExist:
                return Response({'status': "Invalid"})
        
        else:
            uid = blog_categories.objects.all().order_by("-id")
            serializer = blog_categories_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
       
    def post(self, request):
        serializer = blog_categories_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = blog_categories.objects.get(id=id)
        except blog_categories.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = blog_categories_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = blog_categories.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except blog_categories.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
#------------------



class blog_view(APIView):
    def get(self, request, id=None,blog_id=None):
        if id:
            try:
                uid = blog.objects.get(id=id)
                serializer = blog_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except blog.DoesNotExist:
                return Response({'status': "Invalid"})
        elif blog_id:
                    try:
                        uid = blog.objects.filter(blog_category_data__id=blog_id)
                        print(uid)
                        serializer = blog_serializers(uid,many=True)
                        return Response({'status': 'success', 'data': serializer.data})
                    except blog.DoesNotExist:
                        return Response({'status': "Invalid"})
        else:
            uid = blog.objects.all().order_by("-id")
            serializer = blog_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = blog_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = blog.objects.get(id=id)
        except blog.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = blog_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = blog.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except blog.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

class nft_barriers_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = nft_barriers.objects.get(id=id)
                serializer = nft_barriers_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except nft_barriers.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = nft_barriers.objects.all().order_by("-id")
            serializer = nft_barriers_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = nft_barriers_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = nft_barriers.objects.get(id=id)
        except nft_barriers.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = nft_barriers_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = nft_barriers.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except nft_barriers.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


class contact_us_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = contact_us.objects.get(id=id)
                serializer = contact_us_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except contact_us.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = contact_us.objects.all().order_by("-id")
            serializer = contact_us_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = contact_us_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = contact_us.objects.get(id=id)
        except contact_us.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = contact_us_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = contact_us.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except contact_us.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


class berries_structure_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = berries_structure.objects.get(id=id)
                serializer = berries_structure_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except berries_structure.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = berries_structure.objects.all().order_by("-id")
            serializer = berries_structure_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = berries_structure_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = berries_structure.objects.get(id=id)
        except berries_structure.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = berries_structure_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = berries_structure.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except berries_structure.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

class admin_login_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = admin_login.objects.get(id=id)
                serializer = admin_login_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except admin_login.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = admin_login.objects.all().order_by("-id")
            serializer = admin_login_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
    def post(self,request):
            serializer=admin_login_serializers(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                uid=admin_login.objects.filter(email=email).exists()
                if uid:
                    uid=admin_login.objects.get(email=email)
                    if uid.password == password:
                        serializer=admin_login_serializers(uid)

                        return Response({'status':'success','data':serializer.data})
                    else:
                        return Response({'status':'invalid password'})
                else:
                    return Response({'status':'invalid email'})

            else:
                return Response({'status':"invalid data"})





class ad_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = ad.objects.get(id=id)
                serializer = ad_serializers(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = ad.objects.order_by("-id")
            serializer = ad_serializers(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        # pid=ad.objects.all()
        # pid.delete()
        serializer = ad_serializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})



    def patch(self,request,id=None):

        if id:
            uid = ad.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = ad_serializers(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})


    def delete(self,request,id=None):
        if id:
            try:
                uid = ad.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})



class user_view(APIView):
    def get(self,request,id=None):
        if id:

            try:
                uid=user.objects.get(user_id=id)
                serializer=user_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})
        else:
            uid=user.objects.all().order_by("-id")
            for i in uid:
                print(i.date_time)
            serializer=user_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})

    def post(self,request):
        serializer=user_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data","error":serializer.errors})


    def patch(self,request,id=None):
        try:
            uid=user.objects.get(user_id=id)
        except:
            return Response({'status':"invalid data"})
        serializer=user_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid data","error":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid=user.objects.get(user_id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        else:
            return Response({'status':"invalid data"})




class token_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = token.objects.get(id=id)
                serializer = token_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except token.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = token.objects.all().order_by("-id")
            serializer = token_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = token_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = token.objects.get(id=id)
        except token.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = token_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = token.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except token.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        

class grower_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = grower.objects.get(id=id)
                serializer = grower_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except grower.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = grower.objects.all().order_by("-id")
            serializer = grower_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = grower_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = grower.objects.get(id=id)
        except grower.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = grower_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = grower.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except grower.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
#====================
class certifications_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = certifications.objects.get(id=id)
                serializer = certifications_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except certifications.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = certifications.objects.all().order_by("-id")
            serializer = certifications_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = certifications_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = certifications.objects.get(id=id)
        except certifications.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = certifications_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = certifications.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except certifications.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
        
#========================
class utility_tags_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = utility_tags.objects.get(id=id)
                serializer = utility_tags_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except utility_tags.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = utility_tags.objects.all().order_by("-id")
            serializer = utility_tags_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = utility_tags_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = utility_tags.objects.get(id=id)
        except utility_tags.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = utility_tags_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = utility_tags.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except utility_tags.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
class berry_types_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = berry_types.objects.get(id=id)
                serializer = berry_types_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except berry_types.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = berry_types.objects.all().order_by("-id")
            serializer = berry_types_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = berry_types_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = berry_types.objects.get(id=id)
        except berry_types.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = berry_types_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = berry_types.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except berry_types.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
#==================
class berry_batch_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = berry_batch.objects.get(id=id)
                serializer = berry_batch_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except berry_batch.DoesNotExist:
                return Response({'status': "Invalid"})
        
        else:
            uid = berry_batch.objects.all().order_by("-id")
            serializer = berry_batch_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})
       
    def post(self, request):
        serializer = berry_batch_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = berry_batch.objects.get(id=id)
        except berry_batch.DoesNotExist:
            return Response({'status': "invalid data"})

        serializer = berry_batch_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = berry_batch.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except berry_batch.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})