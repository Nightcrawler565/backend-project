from django.core.management.base import BaseCommand
from creditsystem.tasks import excel_ingestion_task

class Command(BaseCommand):
    help = 'Ingest data from Excel into Django models'

    def handle(self, *args, **options):
        excel_file_path='C:\Users\User\Downloads\Backend Internship Assignment\customer_data.xlsx'

        # Execute the Celery task asynchronously
        excel_ingestion_task.delay(excel_file_path)


        self.stdout.write(self.style.SUCCESS('Ingestion task scheduled. Check celery logs for progress. '))