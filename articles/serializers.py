from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("Le titre ne peut pas dépasser 50 caractères.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Le contenu ne peut pas être vide.")
        return value
