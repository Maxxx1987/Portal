from django.shortcuts import render
from apps.comments.models import Comment
from django.views.generic.list import ListView


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(topic__slug=self.kwargs['slug'])


def comment_list(request, **kwargs):
    data = Comment.objects.filter(topic__slug=kwargs['slug'])
    context = {'comment_list': data}
    return render(request, 'comment_list.html', context=context)
