from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  

class RegisterView(generics.CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Allow admin/superuser to log in without approval
            if user.is_superuser or user.is_staff or user.is_approved:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Account not approved'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out'})

class DashboardView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Admin endpoint to approve users
class ApproveUserView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [permissions.IsAdminUser]
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.is_approved = True
            user.save()
            return Response({'message': 'User approved'})
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def unapproved_users(request):
    is_approved = request.GET.get('is_approved')
    if is_approved == 'false':
        users = User.objects.filter(is_approved=False, is_superuser=False)
    else:
        users = User.objects.filter(is_superuser=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
