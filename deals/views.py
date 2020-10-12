import csv

from rest_framework.response import Response
from rest_framework.views import APIView

from deals.models import Deals
from deals.serializers import DealFileSerializer, DealVeiwSerializer


class DealUpload(APIView):
    serializer_class = DealFileSerializer

    def post(self, request):
        try:
            serializer = DealFileSerializer(data=request.data)
            if serializer.is_valid():
                self.delete_everything()
                serializer.save()
                self.open_csv(serializer['deal'].value)
                return Response("OK - файл был обработан без ошибок;")
            else:
                return Response(serializer.errors)

        except Exception as e:
            error = (f'Error, Desc: {str(e)} - в процессе обработки файла '
                     f'произошла ошибка.')
            return Response(error)

    def delete_everything(self):
        Deals.objects.all().delete()

    def open_csv(self, file):
        with open('TextTask/files' + file, "rt", encoding='utf8') as f:
            reader = csv.reader(f)
            deals = []
            for row in list(reader)[1:]:
                deals.append(
                    Deals(
                        username=row[0],
                        item=row[1],
                        total=row[2],
                        quantity=row[3],
                        date=row[4],
                    )
                )
            Deals.objects.bulk_create(deals)

    def get(self, request):
        queryset = Deals.objects.all()
        queryset = queryset[:5]

        serializer = DealVeiwSerializer(queryset, many=True)
        serializer_data = sorted(
            serializer.data, key=lambda k: k['spent_money'], reverse=True)
        return Response(serializer_data)
