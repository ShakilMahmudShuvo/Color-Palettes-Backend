# from rest_framework import serializers
# from .models import Palette

# class PaletteSerializer(serializers.ModelSerializer):
#     # A serializer for the Palette model
#     class Meta:
#         model = Palette
#         fields = "__all__" # Including all fields of the model in the serialized data


from rest_framework import serializers
from .models import Palette

class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if not user.is_staff:  # Regular user
            self.fields.pop('user')  # Remove 'user' field from serializer when its a regular user, 
                                # the new color palette will be automatically associate to his id
                                # but for admin,he can choose the user manually for a post
                                


