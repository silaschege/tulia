from django import forms
from django.forms import ModelForm
from .models import ProductCategory,ProductSubCategory,Product

class AddProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields={'product_category_name' }
        labels={
            'product_category_name':'Product Category Name'

        }
        widgets={
             'product_category_name':forms.TextInput(attrs={'class':'form-control'}),
        }

class AddProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields={'product_sub_category_name','product_category'}
        labels={
                'product_sub_category_name': 'Product Sub Category Name',
                'product_category':'Product Category',
        }
        widgets={
            'product_sub_category_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_category':forms.Select(attrs={'class':'form-select'}),
        }

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields={'product_name','product_description','product_price','product_quantity', 'product_image','product_category','product_sub_category'}

        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_description':forms.TextInput(attrs={'class':'form-control'}),
            'product_price':forms.NumberInput(),
            'product_quantity':forms.NumberInput(),
            'product_category':forms.Select(attrs={'class':'form-select'}),
            'product_sub_category':forms.Select(attrs={'class':'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_sub_category'].queryset =  ProductSubCategory.objects.none()

        if 'product_category' in self.data:
            try:
                category_id = int(self.data.get('product_category'))
                self.fields['product_sub_category'].queryset = ProductSubCategory.objects.filter(product_category = category_id).order_by('product_sub_category_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['product_sub_category_name'].queryset = self.instance.product_category.product_sub_category_set.order_by('product_sub_category_name')
