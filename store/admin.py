from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Product, Category, Company, StarRating, Rating, Review, Attribute, AttributesValue, Cart, CartProduct


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(widget = CKEditorUploadingWidget())

    class Meta:
        models = Product
        fields = '__all__'
        
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    form = ProductAdminForm


class AutofieldSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

class AttributeValueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['value']}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, AutofieldSlugAdmin)
admin.site.register(Company, AutofieldSlugAdmin)
admin.site.register(Attribute, AutofieldSlugAdmin)
admin.site.register(AttributesValue, AttributeValueAdmin)
admin.site.register(StarRating)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartProduct)
