from django import forms
from order.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_first_name', 'order_last_name', 'order_email',
            'order_address', 'order_postal_code', 'order_city',
        ]





