from django import forms  
from first_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }