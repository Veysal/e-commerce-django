from django import forms

PRODUCT_QUANTITY_CHOICES = []
for i in range(1,8):
    PRODUCT_QUANTITY_CHOICES.append((i, str(i)))


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices = PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label = 'Количество'
    )

    update = forms.BooleanField(
        required = False,
        initial = False,
        widget=forms.HiddenInput
    )