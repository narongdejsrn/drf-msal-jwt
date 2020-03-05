from rest_framework import serializers


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=2000)
