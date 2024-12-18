from django.shortcuts import render


# Create your views here.
def gameguides_home_view(request):
    return render(request, 'GameGuides/game_guides_home.html')


def hsr_banner_history_view(request):
    return render(request, 'GameGuides/hsr_banner_history.html')


def survivorio_clans_view(request):
    return render(request, 'GameGuides/survivorio_clans.html')


def survivorio_gear_view(request):
    return render(request, 'GameGuides/survivorio_gear.html')


def survivorio_map_types_bosses_view(request):
    return render(request, 'GameGuides/survivorio_map_types_bosses.html')


def survivorio_pets_view(request):
    return render(request, 'GameGuides/survivorio_pets.html')


def survivorio_survivors_view(request):
    return render(request, 'GameGuides/survivorio_survivors.html')


def survivorio_merging_view(request):
    return render(request, 'GameGuides/survivorio_merging.html')
