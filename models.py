from tortoise import Model,fields
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator
class User(Model):
    id=fields.IntField(pk=True,index=True)
    username=fields.CharField(max_length=45,null=False)
    email=fields.CharField(max_length=200,null=False,unique=True)
    password=fields.CharField(max_length=255,null=False)
    is_verified=fields.BooleanField(default=False)
    date_joined=fields.DatetimeField(default=datetime.utcnow)


class Business(Model):
    id=fields.IntField(pk=True,index=True)
    businessname=fields.CharField(max_length=45,null=False)
    logo=fields.CharField(max_length=255,default="defaultlogo.png")
    owner=fields.ForeignKeyField("models.User",related_name="business")

class Product(Model):
    id=fields.IntField(pk=True,index=True)
    productname=fields.CharField(max_length=100,null=False)
    category=fields.CharField(max_length=30,index=True)
    image=fields.CharField(max_length=255,default="defaultproduct.png")
    price=fields.DecimalField(max_digits=12,decimal_places=2)
    created_at=fields.DatetimeField(default=datetime.utcnow)
    business=fields.ForeignKeyField("models.Business",related_name="products")



user_pydantic=pydantic_model_creator(User,name="User",exclude=("is_verified",))
user_pydanticIn=pydantic_model_creator(User,name="UserIn",exclude_readonly=True,exclude=("is_verified","date_joined"))
user_pydanticOut=pydantic_model_creator(User,name="UserOut",exclude=("password",))

business_pydantic=pydantic_model_creator(Business,name="Business")
business_pydanticIn=pydantic_model_creator(Business,name="Business",exclude_readonly=True)

product_pydantic=pydantic_model_creator(Product,name="Product")
product_pydanticIn=pydantic_model_creator(Product,name="ProductIn",exclude=("id"))