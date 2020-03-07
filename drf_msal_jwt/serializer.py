from rest_framework import serializers


class CodeSerializer(serializers.Serializer):
    """
    Serializer class for serialize code from the user
    """
    code = serializers.CharField(max_length=2000)
    state = serializers.CharField(max_length=36, allow_blank=True, allow_null=True)
