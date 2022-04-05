from email.mime import image
from ssl import AlertDescription
from urllib import request
from django import forms
from .models import All_Type, Device, Device_Type
class DeviceForm(forms.ModelForm):
    #status = forms.ModelChoiceField(queryset=Device.objects.all().order_by('name'))
    class Meta:
        model=  Device
        fields = ('name','slug','notes','status','image','device_type','current_release','target_release','all_type','release_police')
        def __init__(self, *args, **kwargs):
            super(DeviceForm, self).__init__(*args, **kwargs)
            self.fields['status'].queryset = Device.objects.all()
            self.fields['release_police'].queryset = Device.objects.all()
            self.fields['device_type'].queryset = Device_Type.objects.all()
            self.fields['all_type'].queryset = All_Type.objects.all()
            for field in self.fields:
                self.fields[field].widget.attrs['class'] ="form-control"
            
    