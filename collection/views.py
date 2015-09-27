from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing

# Create your views here.
def index(request):
  number = 6
  thing = "Thing name"
  things = Thing.objects.all()
  # this is your new view
  return render(request, 'index.html', {
    'number': number,
    'thing': thing,
    'things': things,
  })

def thing_detail(request, slug):
  thing = Thing.objects.get(slug=slug)
  return render(request, 'things/thing_detail.html', {
    'thing': thing,
    })

def edit_thing(request, slug):
  thing = Thing.objects.get(slug=slug)
  form_class = ThingForm
  if request.method == 'POST':
    form = form_class(data=request.POST, instance=thing)
    if form.is_valid():
      form.save()
      return redirect('thing_detail', slug=thing.slug)
  else: 
    form = form_class(instance=thing)
  return render(request, 'things/edit_thing.html', {
      'thing': thing,
      'form': form, 
    }) 

def browse_by_name(request, initial=None):
  if initial:
    things = Things.objects.filter(
        name__istartswith=initial).order_by('name')
  else:
    things = Thing.objects.all().order_by('name')
  return render(request, 'search/search.html', {
      'things': things, 
      'initial': initial,
    }) 