from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from products.models import Product

# Create your views here.
class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


class ProductListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"
