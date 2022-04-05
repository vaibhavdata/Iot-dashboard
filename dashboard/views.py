from audioop import reverse
from django.shortcuts import render,redirect,HttpResponse
from .models import All_Type, Device,Device_Type,Service,Service_type
from django.contrib.auth.models import User
from .forms import DeviceForm
# Create your views here.
def home(request):
    device = Device.objects.all().filter(is_available=True).order_by('created_date')
    device_count = device.count()
    context ={
        'device': device,
        'device_count': device_count,
        
    }
    return render(request,"home/index.html",context)


def device_detail(request,slug):
    single_device = Device.objects.filter(slug=slug)
    service = Service.objects.all().order_by('service')
    context ={
        'single_device': single_device,
        'service':service,
    }
    return render(request,"home/tables.html",context)
def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip =""
    return ip
def device_add(request):
    if request.method =="POST":
        form = DeviceForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            data =Device()
            data.name = form.cleaned_data['name']
            data.slug = form.cleaned_data['slug']
            data.notes = form.cleaned_data['notes']
            data.image = form.cleaned_data['image']
            data.status = form.cleaned_data['status']
            data.device_type = form.cleaned_data['device_type']
            data.current_release = form.cleaned_data['current_release']
            data.target_release = form.cleaned_data['target_release']
            data.all_type = form.cleaned_data['all_type']
            data.release_police = form.cleaned_data['release_police']
            data.ip_address = get_ip(request)
            data.host_version =request.META.get('HTTP_REFERER')
            user = User.objects.get(username= request.user)
            data.last_login = user.last_login.strftime('%y-%m-%d %a %H:%M:%S')
            data.save()
            print(data)
            return redirect("home")
    else:
        form = DeviceForm()
    context ={
           'form':form,
       }
            
    return render(request,"home/billing.html",context)

def delete_device(request,slug):
    device = Device.objects.get(slug=slug)
    device.delete()
    return redirect('home')
            
