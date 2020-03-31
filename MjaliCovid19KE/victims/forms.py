from django import forms

from dashboard.models import Victims

class AddNewVictims(forms.ModelForm):

    class Meta:
        model=Victims
        fields=('gender',
                'age',
                'relationship',
                'citizen')
    
        labels={
            'gender':'Enter Gender',
            'age':'Enter Age',
            'relationship':'Enter Relationship',
            'citizen':'Enter Citizenship'
        }
            
            
    def __init__(self, *args, **kwargs):
        super(AddNewVictims,self).__init__(*args, **kwargs)
        #self.fields['status'].empty_label="Select"
        
        