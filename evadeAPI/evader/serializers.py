from rest_framework import serializers
from evader.models import Evader_user


class User_registration_serializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Evader_user
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Evader_user(email=self.validated_data['email'],
                            username=self.validated_data['username'],
                            first_name=self.validated_data['first_name'],
                            last_name=self.validated_data['last_name'],)
        password = self.validated_data['password']
        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user.set_password(password)
        user.save()
        return user
