from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

from .models import ContactInfo, Service, Message, NetworkBoard, Unit
from .forms import MessageForm, ServiceForm, ServiceUpdateForm, StatusUpdateForm, FavoriteForm


@login_required
def home_view(request):
    user = request.user
    units = Unit.objects.filter(users=user)
    return render(request, 'home.html', {'user': user,
                                         'units': units})


@login_required
def netdash_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    favorites = unit.favorites.all()
    return render(request, 'netdash.html', {'unit': unit,
                                            'favorites': favorites})


@login_required
def detail_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    favorites = unit.favorites.all()
    return render(request, 'unit_detail.html', {'unit': unit,
                                                'favorites': favorites})


@login_required
def add_message_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    next = request.POST.get('next', '/')
    if request.method == 'POST':
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.unit = unit
            new_message.save()
            return HttpResponseRedirect(next)
    else:
        message_form = MessageForm()
    return render(request, 'add_message.html', {'form': message_form})


@login_required
def add_service_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    next = request.POST.get('next', '/')
    if request.method == 'POST':
        service_form = ServiceForm(data=request.POST)
        if service_form.is_valid():
            new_service = service_form.save(commit=False)
            new_service.network_board = unit.network_board
            new_service.save()
            return HttpResponseRedirect(next)
    else:
        service_form = ServiceForm()
    return render(request, 'add_service.html', {'form': service_form})


@login_required
def add_favorite_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    next = request.POST.get('next', '/')
    if request.method == 'POST':
        favorite_form = FavoriteForm(data=request.POST)
        if favorite_form.is_valid():
            cd = favorite_form.cleaned_data
            new_favorites = cd['favorites']
            for favorite in new_favorites:
                unit.favorites.add(favorite)
            unit.save()
            return HttpResponseRedirect(next)
    else:
        favorite_form = FavoriteForm()
    return render(request, 'add_favorite.html', {'form': favorite_form})


@login_required
def edit_service_view(request, slug, pk):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    service = get_object_or_404(Service, pk=pk)
    next = request.POST.get('next', '/')
    form = ServiceUpdateForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(next)
    return render(request, 'edit_service.html', {'form': form})


@login_required
def edit_status_view(request, slug):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    network_board = get_object_or_404(NetworkBoard, unit=unit)
    next = request.POST.get('next', '/')
    form = StatusUpdateForm(request.POST or None, instance=network_board)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(next)
    return render(request, 'edit_status.html', {'form': form})


@login_required
def delete_message_view(request, slug, pk):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    message = get_object_or_404(Message, pk=pk)
    next = request.POST.get('next', '/')
    if request.method == "POST":
        message.delete()
        return HttpResponseRedirect(next)
    return render(request, 'delete_message.html', {'message': message})


@login_required
def delete_favorite_view(request, slug, pk):
    unit = get_object_or_404(Unit, slug=slug, users=request.user)
    favorite = unit.favorites.get(pk=pk)
    next = request.POST.get('next', '/')
    if request.method == 'POST':
        unit.favorites.remove(favorite)
        return HttpResponseRedirect(next)
    return render(request, 'delete_favorite.html', {'favorite': favorite})
