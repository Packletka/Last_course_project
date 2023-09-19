from django.shortcuts import render, redirect
from .models import Comments
from .forms import CommentsForm
from django.views.generic import DetailView, DeleteView, UpdateView, ListView


def all_comments(request):
    comments = Comments.objects.order_by('-id')
    return render(request, 'comments/all_comments.html', {'comments': comments})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_comments')

    form = CommentsForm()

    sensation = {
        'form': form,
        'error': error
    }
    return render(request, 'comments/create.html', sensation)


def delete(request):
    return render(request, 'comments/comment_delete.html', {'delete': delete})


def detail_comment(request):
    return render(request, 'comments/detail_comment.html', {'detail_comment': detail_comment})


class CommentsDetailView(DetailView):
    model = Comments
    template_name = 'comments/detail_comment.html'
    context_object_name = 'comment'


class CommentsDeleteView(DeleteView):
    model = Comments
    template_name = 'comments/comment_delete.html'
    success_url = '/comments/'
    context_object_name = 'comment'


class CommentsUpdateView(UpdateView):
    model = Comments
    template_name = 'comments/create.html'
    form_class = CommentsForm


class CommentsListView(ListView):
    model = Comments
    template_name = 'comments/list_view.html'
    context_object_name = 'comment'
    queryset = Comments.objects.all()
