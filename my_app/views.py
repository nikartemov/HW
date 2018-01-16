from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from .models import Flight
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import LoginForm, SignupForm, AddObject
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.core.files.storage import FileSystemStorage


def login(request):
    redirect_url = '/index'
    if request.method == 'POST':
        redirect_url = '/index'
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error(None, 'invalid login/password')
    else:
        form = LoginForm()
    return render(request, 'auth.html', {'form': form, 'continue': redirect_url})


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = auth.authenticate(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'])
            auth.login(request, user)
            return HttpResponseRedirect('/index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form,
                                           'type': 'Registration'})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")


def index(request):
    flights = Flight.objects.all()
    form = AddObject(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            flight = form.fill_object()
            f = request.FILES.get('image')
            print(f)
            if f is None:
                file_url = r'img/default.jpg'
            else:
                file_url = r'img/%d%s' % (flight.id, '.jpg')
                fs = FileSystemStorage()
                filename = fs.save('my_app/static/' + file_url, File(f))

            flight.image_url = file_url
            flight.save()
            return redirect('flight_url', id=flight.id)
    else:
        return render(request, 'objects_list.html', {'flights': flights,
                                                        'form': form})



@csrf_exempt
def flight(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == 'GET':
        status = flight.participation.filter(id=request.user.id).exists()
        return render(request, "object.html", {'flight': Flight.objects.get(id=id), 'status': status})
    if request.method == 'POST':
        state = request.POST.get('state')
        if state == "True" and not flight.participation.filter(id=request.user.id).exists():
            flight.participation.add(request.user)
        if state == 'False' and flight.participation.filter(id=request.user.id).exists():
            flight.participation.remove(request.user)

        return render_to_response('users_list.html', {'users': flight.participation.all()})


def render_cons(pos):
    ObjOnPage = 3
    flights = Flight.objects.all()[ObjOnPage * pos: ObjOnPage * (pos + 1)]
    return flights

def ajax_list(request,page_id):
    pos = int(page_id)
    return render_to_response('object_container.html', {'flights': render_cons(pos)})

