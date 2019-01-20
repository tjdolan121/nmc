from django import forms
from .models import Message, Service, NetworkBoard, Unit


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'priority', 'body')


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'status', 'more_info')


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('title', 'location')


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('favorites',)


class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'status', 'more_info')


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = NetworkBoard
        fields = ('overall_status',)
