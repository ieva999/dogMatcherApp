from django import forms
from app.models import UserProfile
class UserProfileForm(forms.ModelForm):
    #profile information gathered from the survey
    CHOICES_GROOMING=(('Almost none', 1), ('Occasional grooming', 2), ('Regular grooming', 3))
    grooming=forms.ChoiceField()
    family=forms.ChoiceField()
    homesize=forms.ChoiceField()
    dogsize=forms.ChoiceField()
    beingalone=forms.ChoiceField()
    exercise=forms.ChoiceField()

    class Meta:
        model = UserProfile
        fields = ('grooming', 'family', 'homesize', 'dogsize', 'beingalone', 'exercise')
