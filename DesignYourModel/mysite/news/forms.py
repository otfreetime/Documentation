from django import forms
from news.models import Category, Codedata

# class CreateCodeForm(forms.ModelForm):
#     class Meta:
#         model =Codedata
#         fields = (Category)

#         category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)


class NameForm(forms.Form):
    class Meta:
        model =  Codedata
        fields = ['Issure',]

    issure = forms.ModelChoiceField(queryset=Codedata.objects.all(),empty_label=None)
    # code = forms.ModelChoiceField(queryset=Codedata.objects.only('Code'),empty_label=None)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)



    