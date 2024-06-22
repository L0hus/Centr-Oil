from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from Main.models import Product
from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .models import Feedback

def index_view(request):
    form = FeedBackForm()
    return render(request, 'index.html', {'form': form})

def catalog_view(request):
    form = FeedBackForm()
    return render(request, 'catalog.html', {'form': form})

def product_detail(request, type, id):
    form = FeedBackForm()
    product = get_object_or_404(Product, type=type, id=id)
    return render(request, 'product.html', {'product': product, 'form': form},)

def production_view(request):
    form = FeedBackForm()
    return render(request, 'production.html', {'form': form})

def directory_view(request):
    form = FeedBackForm()
    return render(request, 'directory.html', {'form': form})

def auto_view(request):
    form = FeedBackForm()
    return render(request, 'auto-dir.html', {'form': form})

def aviation_view(request):
    form = FeedBackForm()
    return render(request, 'aviation-dir.html', {'form': form})

def cable_view(request):
    form = FeedBackForm()
    return render(request, 'cable-dir.html', {'form': form})

def conservation_view(request):
    form = FeedBackForm()
    return render(request, 'conservation-dir.html', {'form': form})

def multi_view(request):
    form = FeedBackForm()
    return render(request, 'multi-dir.html', {'form': form})

def lowtemp_view(request):
    form = FeedBackForm()
    return render(request, 'lowtemp-dir.html', {'form': form})

def instrumentation_view(request):
    form = FeedBackForm()
    return render(request, 'instrumentation-dir.html', {'form': form})

def gearbox_view(request):
    form = FeedBackForm()
    return render(request, 'gearbox-dir.html', {'form': form})

def reinforcing_view(request):
    form = FeedBackForm()
    return render(request, 'reinforcing-dir.html', {'form': form})

def conductive_view(request):
    form = FeedBackForm()
    return render(request, 'conductive-dir.html', {'form': form})

def lithium_view(request):
    form = FeedBackForm()
    return render(request, 'lithium-dir.html', {'form': form})

def map_view(request):
    form = FeedBackForm()
    return render(request, 'map.html', {'form': form})

def privacy_view(request):
    form = FeedBackForm()
    return render(request, 'privacy.html', {'form': form})

class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        try:
            form = FeedBackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.ip_address = request.META.get('REMOTE_ADDR')
                feedback.save()
                name = form.cleaned_data['name']
                from_email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']
                try:
                    send_mail(f'От {name} | {phone}', message, from_email, [''])
                except BadHeaderError:
                    pass  # Просто игнорируем ошибку
            return redirect('home')
        except Exception:
            return redirect('home')
        
def custom_404(request, exception):
    return render(request, '404.html', status=404)
        