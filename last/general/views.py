from django.shortcuts import render, redirect
from .models import Comments
from .forms import CommentsForm


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


def No_game_No_Life(request):
    return render(request, 'general/No_game_No_Life.html')


def all_comments(request):
    comments = Comments.objects.order_by('-id')  # Сортировка по новизне
    return render(request, 'general/all_comments.html', {'comments': comments})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_comments')
        else:
            error = 'Коммент был плохим'

    form = CommentsForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'general/create.html', context)
