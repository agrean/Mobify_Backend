from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Payments
from .serializers import PaymentSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView


from rest_framework import permissions

# Create your views here.
class UsersView(APIView):
    def post(self, request, formar=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404)

@csrf_exempt
def users_view(request):
    """
    The view enables creating new users into the system
    """
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=201)

        return JsonResponse(user_serializer.errors, status=400)

# def user_view(request, pk):
# 	"""
# 	This view enable to deal with one specific user
# 	"""
# class Payment(generics.ListCreateAPIView):
# 	queryset = Payments.objects.all()
# 	serializer_class = PaymentSerializer

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)


class Payment(APIView):
    #     """
    #     List all snippets, or create a new snippet.
    #     """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        # payments = Payments.objects.all()
        payments = Payments.objects.filter(owner=self.request.user)
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(serializer.data, safe=False)


    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt  # exempting csrf token
def payments_view(request):
    """
    The view enables listing all the existing payments and creating new ones
    """
    if request.method == 'GET':
        payments = Payments.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return JsonResponse({'payments': serializer.data})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def payment_view(request, pk):
    """
    View to respond to individual payment. Retrieve, update or delete payment
    """
    try:
        payment = Payments.objects.get(pk=pk)
    except Payments.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PaymentSerializer(payment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(payment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        payment.delete()
        return HttpResponse(status=204)
