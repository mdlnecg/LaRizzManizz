from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'rating']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        return strip_tags(rating)
        