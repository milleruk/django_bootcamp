from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from . models import Product

# Create your views here.
def home_view(request, *args, **kwargs):  # /search/
    # print(args, kwargs)
    # return HttpResponse("<h1>Hello World</h1>")
    context = {"name": "Miller"}
    return render(request, "home.html", context)


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # render html page with HTTP statis 404

    #try:
    #    obj = Product.objects.get(id=id)
    #except:
    #    raise Http404

    #return HttpResponse(f"Product id {obj.id}")
    #return render(request, "products/product_detail.html", {"object": obj})
    return render(request, "products/detail.html", {"object": obj})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all() # [obj1, obj2, obj3]
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not Found"})
        #return json with HTTP status code of 404 
    return JsonResponse({"id": obj.id})
    
#class HomeView():
#    pass
