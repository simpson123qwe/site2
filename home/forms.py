from django import forms 
class ReviewForm(forms.Form):
    lname=forms.CharField(max_length=15)
    fname=forms.CharField(max_length=15)
    pol=forms.ChoiceField(
        choices=(("M","M"),("W","W"))
    )
    vozrast=forms.DateTimeField()
    pochta=forms.EmailField(min_length=10)
