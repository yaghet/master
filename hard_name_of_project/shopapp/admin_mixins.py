import csv
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.db.models.options import Options


class ExportAsCSCMixin:
    def export_csv(self, request: HttpRequest, query_set: QuerySet):
        meta: Options = self.moder._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-disposition'] = f'Attachment: filename={meta}-export.csv'

        csv_writer = csv.writer(response)
        csv_writer.writerow(field_names)

        for obj in query_set:
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv.short_description = 'Export as CSV'
