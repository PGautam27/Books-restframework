from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    author_name = serializers.CharField(max_length=100)
    completed_reading = serializers.BooleanField()
    reading_platform = serializers.CharField(max_length=100)

    def create(self, data):
        return Book.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.author_name = data.get('author_name', instance.author_name)
        instance.completed_reading = data.get('completed_reading', instance.completed_reading)
        instance.reading_platform = data.get('reading_platform', instance.reading_platform)


        instance.save()
        return instance

# from dataclasses import field
# from rest_framework import serializers
# from book_api.models import Book
#
#
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         field = "__all__"
