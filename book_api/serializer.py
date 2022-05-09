from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)

# {
#    "title": "Harry Potter",
#    "number_of_pages": 300,
#    "publish_date": "2021-01-09",
#    "quantity": 400
# }
