from rest_framework.response import Response
from rest_framework.views import APIView

from drf_msal_jwt.serializer import CodeSerializer
from drf_msal_jwt.utils import build_auth_url, get_user_jwt_token


class MSALLoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return Response({
            'login_url': build_auth_url()
        })


class MSALLoginWithCodeView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        code_serialized = CodeSerializer(request.data)
        user_token = get_user_jwt_token(code_serialized.data['code'])
        return Response({
            'token': user_token
        })


