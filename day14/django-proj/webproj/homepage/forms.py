from django import forms # form import
from .models import Coffee # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm
    class Meta: #form을 만들기 위해서 어떤 form을 써야하는지
        model = Coffee
        fields = ('name', 'price', 'is_ice')