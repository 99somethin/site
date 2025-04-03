from django import forms

class CommentArticleForm(forms.Form):
    content = forms.CharField(
        label="Комментарий",
        max_length=200,
        widget=forms.Textarea(attrs={
            "placeholder": "Введите ваш комментарий...",  
            "class": "form-control", 
            "rows": 4
        })
    )