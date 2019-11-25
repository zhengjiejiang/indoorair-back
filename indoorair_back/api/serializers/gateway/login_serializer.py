from rest_framework import serializers
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login,logout
from rest_framework.validators import UniqueValidator




class LoginSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


    def create(self, validate_data):
        username = request.POST.get("username")
        password = request.POST.get("password")
        request=self.context.get('request')

         # This is for debugging purposes only.
        print(username, password)
        try:
            user = authenticate(
            username=username,
            password=password,
            )

            if user :
                print("PRE-LOGIN", user.get_full_name())
                login(request,user)
                print("PRE-LOGIN", user.get_full_name())
                # A backend authenticated the credentials
                return user
        except Exception as e:
            print(e)
            raise serializers.ValidationError({
                 "reason": "Cannot log in, username or password is wrong.",
            })
