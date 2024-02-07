# tasks.py
from celery import shared_task
import pandas as pd
from django.core.management import call_command
from system.models import Customers,LoanData

@shared_task
def excel_ingestion_task(excel_file_path):
    try:
        df=pd.read_excel(excel_file_path)

        for index, row in df.iterrows():
         # Create or update model instances based on your data
            Customers.objects.update_or_create(
                customer_id=row['Customer ID'],
                first_name=row['First Name'],
                last_name=row['Last Name'],
                age=row['Age'],
                phone_number=row['Phone Number'],
                monthly_salary=row['Monthly Salary'],
                approved_limit=row['Approved Limit']
            )
        print('Successfully ingested data from Excel')
    except Exception as e:
        print(f'Error: {str(e)}')

