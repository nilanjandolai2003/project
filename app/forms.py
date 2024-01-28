from django import forms
from .models import student
from datetime import datetime
from django.utils.text import slugify


class student_form(forms.ModelForm):
    join_date=forms.DateTimeField(widget=forms.HiddenInput(),initial=datetime.now(),required=False)

    class Meta:
        model=student
        fields=['first_name','last_name','department','role','phone']
    def save(self,commit=True):
        instance= super().save(commit=False)
        instance.join_date=datetime.now()
        unique_id = f"{slugify(instance.department.name)}{self.generate_unique_number(instance.department)}"
        instance.id = unique_id

         
        if commit:
            instance.save()
        return instance     
    def generate_unique_number(self, department):
        count = student.objects.filter(department=department).count() + 1
        return str(count).zfill(3)