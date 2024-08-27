from django.shortcuts import render


def take_me_home_cr(request):
    return render(request, 'home_page.html')


def show_me_some_thing(request):
    return render(request, 'disc_folder.html')
