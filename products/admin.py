from django.contrib import admin
from .models import UserProfile, Direction, RankingUser, Category, Product, Card, Rent



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','cellphone') 

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)

class RentInLine(admin.TabularInline):
    list_display = ('user','product','score','begin_day','end_day') 
# class UserDirectionAdmin(admin.ModelAdmin):
#     list_display = ('street','int_number','ext_number','neighborhood','country','state')
# admin.site.register(UserProfile, UserDirectionAdmin)

# Register your models here.
admin.site.register(Direction)
admin.site.register(RankingUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Card)
admin.site.register(Rent)