from django import forms

from .models import Product, Category


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Category.objects.all())
    image_url = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'description', 'date', 'location',
                  'category', 'image_url']
