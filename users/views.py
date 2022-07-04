from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header

# me modul
from .models import MyUser
from .serializers import UserSerializer
from .authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token


class RegisterAPIView(APIView): # registrasa uchun 
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class LoginAPIView(APIView): # login uchun
    def post(self, request):
        # data dan kelgan userni email ini olib tekshirib koradi
        user = MyUser.objects.filter(email=request.data['email']).first()
    
        if not user: # Agar user yoq bolsa
            raise APIException("Invalid Email") 
        print(user.password)
        if user.password != request.data['password']: #agar parol togri kelmasa
            raise APIException("Invalid Password")

        access_token = create_access_token(user.id) 
        refresh_token = create_refresh_token(user.id) 

        resp = Response()
        # cookie ga refresh tokenni joylemiz 
        resp.set_cookie(key='refreshToken', value=refresh_token , httponly=True) 

        resp.data = {
            'token': access_token
        }

        return resp

    
class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split() 
        # print(auth)
        # print(len(auth))

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            user = MyUser.objects.filter(pk=id).first()
            return Response(UserSerializer(user).data)

        raise AuthenticationFailed("Unauthenticated")



class RefreshTokenAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
        print(refresh_token)
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response({
            'token':access_token
        })


