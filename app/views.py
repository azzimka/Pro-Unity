from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Registration
from .forms import RegistrationForm
from .models import Course, Category


def index(request):
    course = Course.objects.all()
    category = Category.objects.all()

    return render(request,'index.html' ,{'course':course,'category':category})

def category_detail(request,slug):
    categories = Category.objects.get(slug__iexact=slug)
    return render(request,'category_detail.html',{'categories':categories})




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@staff_member_required
def view_data(request):
    ism_query = request.GET.get('ism')
    it_query = request.GET.get('it')

    registrations = Registration.objects.all()
    
    if ism_query:
        registrations = registrations.filter(ism__icontains=ism_query)
    if it_query:
        registrations = registrations.filter(it__icontains=it_query)
        
    return render(request, 'view_data.html', {'registrations': registrations})


def card(request):
    return render(request, 'card.html')

def python(request):
    return render(request, 'python.html')

def front(request):
    return render(request, 'front.html')

def base(request):
    return render(request, 'base.html')