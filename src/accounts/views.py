from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from accounts.forms import UserLoginForm, UserRegForm, AddInformationAboutStudent
from accounts.models import MyUser

User = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('info:home')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('info:home')


def register_view(request):
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        messages.success(request, 'Пользователь добавлен в систему.')
        return render(request, 'accounts/register_done.html',
                      {'new_user': new_user})
    return render(request, 'accounts/register.html', {'form': form})


def user_info_view(request, pk):
    users = MyUser.objects.filter(id=pk)
    return render(request, 'accounts/user_info.html', {'users': users})


def change_info_view(request, pk):
    if request.method == 'POST':
        form = AddInformationAboutStudent(auto_id=pk,
                                          instance=request.user,
                                          data=request.POST,
                                          files=request.FILES)
        if form.is_valid():
            form.save()
            # obj = User.objects.get(pk=pk)
            return redirect('/1/')
    else:
        form = AddInformationAboutStudent(instance=request.user)
    return render(request, 'accounts/change_info.html', {'form': form})

