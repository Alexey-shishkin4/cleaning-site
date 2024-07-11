from django import forms
from .models import Bb
from orders.models import Orders
from phonenumber_field.formfields import PhoneNumberField
import datetime


class OrderForm(forms.ModelForm):

    service = forms.ModelMultipleChoiceField(
        label="Услуги",
        queryset=Bb.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    time = forms.DateTimeField(
        widget=forms.DateTimeInput(),
        initial=datetime.datetime.now()
    )

    name = forms.CharField(label="Your name", max_length=100)

    email_address = forms.EmailField()

    phone_number = PhoneNumberField(region="RU")

    address = forms.CharField(max_length=200)

    comment = forms.Textarea()

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Orders
        fields = ['service',
                  'time',
                  'name',
                  'email_address',
                  'phone_number',
                  'address',
                  'comment']