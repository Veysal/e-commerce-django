from django import forms

# Создаем список для выбора количества товара от 1 до 20.
# Это более явный способ сделать то же самое, что и генератор списка.
PRODUCT_QUANTITY_CHOICES = []
for i in range(1, 21):
    PRODUCT_QUANTITY_CHOICES.append((i, str(i)))


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Количество'
    )
    # Поле, которое говорит, нужно ли перезаписать количество или добавить к существующему
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
