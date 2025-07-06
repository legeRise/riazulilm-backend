from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    formatted_date = serializers.SerializerMethodField()
    download_url = serializers.SerializerMethodField()  # <-- Add this line

    class Meta:
        model = Book
        fields = '__all__'  # This will now include download_url and formatted_date

    def get_formatted_date(self, obj):
        return obj.formatted_date

    def get_download_url(self, obj):
        return obj.download_url  # Uses the @property from your model