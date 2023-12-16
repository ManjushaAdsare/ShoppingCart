import os
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Product, CartItem
from rest_framework import status
import traceback
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.views import APIView


class List_Products(ListAPIView):

    def get(self, request, *args, **kwargs):
        try:
            queryset = Product.objects.all()

            # output = {
            #     "products": list(queryset.values())
            # }

            # return Response(output, status.HTTP_200_OK)
            return Response({'products': list(queryset.values())}, template_name='index.html')
            # return (request, 'index.html', {'products': list(queryset.values())})
        except Exception as e:
            print(e)
            print(traceback.format_exc())


class AddProductData(APIView):
    def post(self, request):
        try:
            data = request.data
            record = []
            for item in data["products"]:
                each_record = Product(
                    name=item.get("name"),
                    description=item.get("description"),
                    price=item.get("price"),
                )
                record.append(each_record)
            Product.objects.bulk_create(record)
            return Response(
                {"success": "Data inserted successfully"},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return Response(
                {"data": [], "Details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ViewCart(APIView):
    def get(self, request, *args, **kwargs):
        try:
            print("request.user ********************************", request.user)
            cart_items = CartItem.objects.all()
            # cart_items = CartItem.objects.filter(user=request.user)
            total_price = sum(item.product.price * item.quantity for item in cart_items)
            # return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
            return Response({'cart_items': cart_items, 'total_price': total_price}, template_name='cart.html')
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return Response("Error......")


class AddtoCart(APIView):
    def post(self, request, product_id):
        try:

            # product_id = str(product["id"])
            # if product_id not in self.cart:
            #     self.cart[product_id] = {
            #         "quantity": 0
            #     }
            # if overide_quantity:
            #     self.cart[product_id]["quantity"] = quantity
            # else:
            #     self.cart[product_id]["quantity"] += quantity
            # self.save()


            # product_id = self.kwargs.get('product_id', None)

            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(product=product)
            print("************************************",cart_item, created)
            cart_item.quantity += 1
            cart_item.save()
            # return redirect('ViewCart')
        except Exception as e:
            print(e)
            print(traceback.format_exc())


class Home(ListAPIView):

    def get(self, request, *args, **kwargs):
        # return HttpResponse('Hello, World!')

        return Response("Hello world")
