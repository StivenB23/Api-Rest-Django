from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Company
import json

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if(len(companies) > 0):
                company=companies[0]
                datos = {"message": "Success", 'companies': company}
                return JsonResponse(datos)
            else:
                datos = {"message": "companies not found..."}
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos = {"message": "Success", 'companies': companies}
            else:
                datos = {"message": "companies not found..."}
            return JsonResponse(datos)


    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        print(jd) #mostrar data en estilo de lista
        Company.objects.create(name=jd['name'],website=jd['website'], foundation=jd['foundation'])
        datos = {"message": "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if(len(companies) > 0):
            companies = list(Company.objects.get(id=id))
            Company.name = jd['name']
            Company.website = jd['website']
            Company.foundation = jd['foundation']
            Company.save()
        else:
            datos = {"message": "companies not found..."}
        return JsonResponse(datos)

    def delete(self, request):
        companies = list(Company.objects.filter(id=id).values())
        if (len(companies) > 0):
            Company.objects.filter(id=id).delete()
            datos = {"message": "Success"}
        else:
            datos = {"message": "companies not found..."}
        return JsonResponse(datos)