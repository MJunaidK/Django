
from django import forms 
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        widgets = {
            'item_name': forms.TextInput(attrs={'placeholder': 'Enter item name', 'class': 'form-input', 'required': True}),
            'item_desc': forms.Textarea(attrs={'placeholder': 'Enter item description', 'class': 'form-textarea', 'required': True, 'rows': 4}),
            'item_price': forms.NumberInput(attrs={'placeholder': 'Enter item price', 'class': 'form-input', 'required': True, 'step': '0.01'}),
            'item_image': forms.URLInput(attrs={'placeholder': 'Enter item image URL', 'class': 'form-input'}),
        }
    
    def clean_item_price(self):
        price = self.cleaned_data.get('item_price')
        if price is not None and price < 0:
            raise forms.ValidationError("Item price cannot be negative.")
        return price
    
    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('item_name')
        desc = cleaned.get('item_desc') 
        if name and desc and name.lower() in desc.lower():
            raise forms.ValidationError("Item description should not contain the item name.")   
        return cleaned
    