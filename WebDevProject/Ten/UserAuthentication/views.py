from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from UserAuthentication.forms import UserInfoForm, UserInfoCustomFieldsForm
from UserAuthentication.models import UserInfo


# Create your views here.
def registration_view(request):
    registered = False
    if request.method == "POST":
        user_info_form = UserInfoForm(data=request.POST)
        user_info_custom_fields_form = UserInfoCustomFieldsForm(data=request.POST)

        if user_info_form.is_valid() and user_info_custom_fields_form.is_valid():
            user = user_info_form.save()
            user.set_password(user.password)
            user.save()

            custom_fields = user_info_custom_fields_form.save(commit=False)
            custom_fields.user = user

            if 'profile_pic' in request.FILES:
                custom_fields.profile_pic = request.FILES['profile_pic']

            custom_fields.save()
            registered = True
        else:
            print(f'{user_info_form.errors}\n{user_info_custom_fields_form.errors}')
    else:
        user_info_form = UserInfoForm()
        user_info_custom_fields_form = UserInfoCustomFieldsForm()

    context_dict = {'registered': registered,
                    'user_info_form': user_info_form,
                    'user_info_custom_fields_form': user_info_custom_fields_form}
    return render(request, 'UserAuthentication/user_registration.html', context=context_dict)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account deactivated.')
        else:
            return HttpResponse('Invalid username/password combination.')
    return render(request, 'UserAuthentication/login_logout.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required()
def user_roster_view(request):
    users_list = UserInfo.objects.all()
    print(users_list)
    return render(request, 'UserAuthentication/user_roster.html', context={'users_list': users_list})
    # return HttpResponse('Only logged in users can see this page!')
