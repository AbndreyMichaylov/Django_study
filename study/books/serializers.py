from rest_framework import serializers
from .models import Author

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name','last_name','email')