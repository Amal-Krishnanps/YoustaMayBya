from rest_framework import serializers

from yousta.models import User,Cloths,ClothVarients,Carts,Orders,Reviews

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]
        #overided, otherwise password will not be saved as encrypted 
    def create(sef,validated_data):
        return User.objects.create_user(**validated_data)
        

##### string realted field
##### slug related field

        
class ClothVarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=ClothVarients
        exclude=("cloth",)
        
        
class ClothSerializer(serializers.ModelSerializer):
    #for showing actual cat name insted of id wit the help of foreignkey relation sip, only works if str method present
    # category=serializers.StringRelatedField(read_only=True) 
    #if str mtd not present then
    category=serializers.SlugRelatedField(read_only=True,slug_field="name")
    # for retriveing all details of varients
    varients=ClothVarientSerializer(many=True,read_only=True)
    class Meta:
        model=Cloths
        fields="__all__"

class CartSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    ClothVarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
     
    class Meta:
        model=Carts
        fields=["id","ClothVarient","user","status","date"]
        
class OrderSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    ClothVarient=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    order_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Orders
        fields="__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cloth=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    
    class Meta:
        model=Reviews
        fields="__all__"