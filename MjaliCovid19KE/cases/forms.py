from django import forms

from dashboard.models import Case

class AddNewCaseForm(forms.ModelForm):

    class Meta:
        model=Case
        fields=('confirmed_date',
                'symptopmatic_at',
                'recovered',
                'details',
                'recovered_at',
                'displayed_symptoms',
                'victim_fk',
                'status',
                'infection_source')
    
        labels={
            'confirmed_date':'Confirmed Date',
            'symptopmatic_at':'Symptopmatic At',
            'recovered':'Recovered',
            'details':'More Details',
            'recovered_at':'Recovered At',
            'displayed_symptoms':'Displayed Symptoms',
            'victim_fk':'Victim',
            'status':'Status',
            'infection_source':'Infection Source',
        }
        attrs = {'confirmed_date': ""}
            
            
    def __init__(self, *args, **kwargs):
        super(AddNewCaseForm,self).__init__(*args, **kwargs)
        self.fields['status'].empty_label="Select"
        self.fields['infection_source'].empty_label="Select"
        self.fields['victim_fk'].empty_label="Select"
        self.fields['details'].required=True
        self.fields['confirmed_date'].widget = forms.DateInput(attrs={
                'type':'date',
                'required': True,
                'class': 'date-time-picker',
                'data-options': '{"format":"Y-m-d H:i", "timepicker":"true"}'
            })
        self.fields['symptopmatic_at'].widget = forms.DateInput(attrs={
                'type':'date',
                'class': 'date-time-picker',
                'data-options': '{"format":"Y-m-d H:i", "timepicker":"true"}'
            })
        self.fields['recovered_at'].widget = forms.DateInput(attrs={
                'type':'date',
                'class': 'date-time-picker',
                'data-options': '{"format":"Y-m-d H:i", "timepicker":"true"}'
            })