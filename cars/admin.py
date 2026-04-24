from django.contrib import admin
from .models import Car, Brand

#Configurações para o admin do django, definindo quais campos serão exibidos e quais serão pesquisáveis

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    search_fields = ("model", "brand",)


#Registra o modelo Car no admin do django, utilizando as configurações definidas na classe CarAdmin(obs: é obrigatório registrar o modelo para que ele apareça no admin do django)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)

