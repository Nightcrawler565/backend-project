from django.shortcuts import render
# from creditsystem.tasks import process_data
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .models import LoanData
from .serializers import CustomerSerializer
from .serializers import LoanSerializer

# def some_view(request):
#     # Process data asynchronously using Celery
#     data = {"key": "value"}
#     process_data.delay(data)
#     return HttpResponse("Data processing started in the background.")

@api_view(['POST'])
def register(request):
    serializer=CustomerSerializer(data=request.data)
    if serializer.is_valid():
        customer=serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def check_eligibility(request):
    customer_id=request.data.get('customer_id')
    loan_amount=float(request.data.get('loan_amount',0))
    interest_rate=float(request.data.get('interest_rate',0))
    tenure=int(request.data.get('tenure'))
    try:
        customer=Customers.objects.get(id=customer_id)
    except Customers.DoesNotExist:
        return Response({"error":"Customer not found"},status=status.HTTP_404_NOT_FOUND)

    # Implement your credit scoring logic here
    credit_score=calculate_credit_score(customer)

    # Implement your eligibility check logic based on credit_score, loan amount, etc.
    approval, corrected_interest_rate=check_loan_eligibility(credit_score,loan_amount,interest_rate,customer)


    response_data={
        "customer_id":customer.id,
        "approval":approval,
        "interest_rate":interest_rate,
        "corrected_interest_rate":corrected_interest_rate,
        "tenure":tenure,
        "monthly_installment":calculate_monthly_installment(loan_amount,corrected_interest_rate,tenure)
    }

    return Response(response_data,status=status.HTTP_200_OK)

def calculate_credit_score(customer):
    pass

def check_loan_eligibility(credit_score,loan_amount,interest_rate,customer):
    pass
    # return approval,corrected_interest_rate

def calculate_monthly_installment(loan_amount,interest_rate,tenure):
    # return monthly_installment
    pass


@api_view(['POST'])
def create_loan(request):
    customer_id=request.data.get('customer_id')
    loan_amount=float(request.data.get('loan_amount',0))
    interest_rate=float(request.data.get('interest_rate',0))
    tenure=int(request.data.get('tenure',0))

    try:
        customer=Customers.objects.get(id=customer_id)
    except Customers.DoesNotExist:
        return Response({"error":"Customer not found"}, status=status.HTTP_404_NOT_FOUND)

    # Return an initial response to the client
    response_data={
        "loan_id":None,
        "customer_id":customer.id,
        "loan_approved":False,
        "message":"Loan processing initiated. Approval status will be update later.",
        "monthly_installment":None,
    }
    return Response(response_data,status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def view_loan(request,loan_id):
    try:
        loan=LoanData.objects.get(loan_id=loan_id)
    except LoanData.DoesNotExist:
        return Response({"error":"Loan not found"},status=status.HTTP_404_NOT_FOUND)

    # Serialize customer details
    customer_serializer=CustomerSerializer(loan.customer_id)

    # Serialize loan details
    loan_serializer=LoanSerializer(loan)

    # Combine customer and loan details in the response
    # response_data={
    #     "loan_id":loan.id,
    #     "customer_id":CustomerDetailSerializer.data,
    #     "loan_amount":loan.loan_amount,
    #     "interest_rate":loan.emi,
    #     "tenure":loan.tenure,
    # }

    return Response(loan_serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def view_loans(request, customer_id):
    try:
        loans=LoanData.objects.filter(customer_id=customer_id)
    except LoanData.DoesNotExist:
        return Response({"error":"Loans not found"},status=status.HTTP_404_NOT_FOUND)

    # Serialize list of loans
    loan_serializer=LoanSerializer(loans,many=True)

    # Return the list of loans
    return Response(loan_serializer.data,status=status.HTTP_200_OK)
# Create your views here.
