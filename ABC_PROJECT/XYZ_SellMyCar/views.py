from django.shortcuts import render
from XYZ_SellMyCar import forms

# Create your views here.
def home_page(request):
    contex_dict = {'text':'Welcome to sell my car!','number':7}
    return render(request, "XYZ_SellMyCar/home.html", contex_dict)

def car_register_page(request):

    register_car_form = forms.RegisterCarForm()

    if request.method == 'POST':

        register_car_form = forms.RegisterCarForm(request.POST)

        if register_car_form.is_valid():
            new_reg_car_form = register_car_form.save(commit=True)
            return home_page(request)
        else:
            print("Error form invalid!")

    return render(request, "XYZ_SellMyCar/car-register.html", {'register_car_form':register_car_form})

def gallery_page(request):
    return render(request, "XYZ_SellMyCar/gallery.html")

def about_page(request):
    return render(request, "XYZ_SellMyCar/about.html")
