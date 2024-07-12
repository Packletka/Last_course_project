from django.shortcuts import render


def main(request):
    return render(request, 'general/main.html')


def pattern(request):
    return render(request, 'general/pattern.html')


def Akame_ga_Kill(request):
    return render(request, 'general/Akame_ga_Kill.html')


def konoSuba(request):
    return render(request, 'general/konoSuba.html')


def Future_Diary(request):
    return render(request, 'general/Future_Diary.html')


def OnePunchMan(request):
    return render(request, 'general/OnePunchMan.html')


def Noragami(request):
    return render(request, 'general/Noragami.html')


def Sword_Art_Online(request):
    return render(request, 'general/Sword_Art_Online.html')


def No_Game_No_Life(request):
    return render(request, 'general/No_Game_No_Life.html')
