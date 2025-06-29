from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
        # Optionally, you can add 'formatted_date' explicitly:
        # fields = ['id', 'title', ..., 'formatted_date']

    def get_formatted_date(self, obj):
        # You can use the property or format it here
        return obj.formatted_date