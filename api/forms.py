from django import forms
from record.models import Customer, Order

        
# add customer form
class AddCustomerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}), label='')
    phone_number = forms.CharField(
    required=False,
    widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
    label=''
    )
    
    class Meta:
        model = Customer
        fields = ['name','phone_number']
        
class AddOrderForm(forms.ModelForm):
    item = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Item', 'class': 'form-control'}), label='')
    amount = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(attrs={'placeholder': 'Amount', 'class': 'form-control'}), label='')
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        widget=forms.widgets.Select(attrs={'class': 'form-control'}),
        label='Select Customer'
    )
    
    class Meta:
        model = Order
        fields = ['customer','item', 'amount']