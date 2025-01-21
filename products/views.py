from django.views import generic
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from .forms import ProductForm

class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    