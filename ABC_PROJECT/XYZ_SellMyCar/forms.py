from django import forms
# from django.forms import ModelForm

from XYZ_SellMyCar.models import Car

class RegisterCarForm(forms.ModelForm):
    # verify_email = forms.EmailField(label="Re-type Email:")
    #
    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     ver_email = all_clean_data['verify_email']
    #
    #     if email != ver_email:
    #         raise forms.ValidationError("Email must match!")

    class Meta:
        model = Car
        fields = '__all__'
