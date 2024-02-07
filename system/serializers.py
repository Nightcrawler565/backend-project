from rest_framework import serializers
from .models import Customers,LoanData

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields='__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoanData
        fields=('id','loan_id','loan_amount')

# class CustomerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customers
#         fields = ['customer_id', 'first_name', 'last_name', 'phone_number', 'age']