from django.shortcuts import render
from django.db.models import Prefetch
from apps.comments.models import Comment
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.comments.forms import AddCommentForm
from apps.categories.models import Topic
from apps.votes.models import Vote


class CommentViewMixin:

    def get_success_url(self):
        return self.object.topic.get_absolute_url()


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        return (
            qs
            .filter(topic__slug=self.kwargs['slug'])
            .prefetch_related(
                Prefetch(
                    'vote_set',
                    queryset=Vote.objects.filter(user=self.request.user),
                    to_attr='user_vote'
                )
            )
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['category_assign'] = self.kwargs['assign']
        context['topic_slug'] = self.kwargs['slug']
        return context


def comment_list(request, **kwargs):
    data = Comment.objects.filter(topic__slug=kwargs['slug'])
    context = {'comment_list': data}
    return render(request, 'comment_list.html', context=context)


class CommentCreateView(CommentViewMixin, CreateView):
    model = Comment
    form_class = AddCommentForm

    def get_initial(self):
        initial = super().get_initial()
        topic = Topic.objects.get(slug=self.kwargs['slug'])
        initial['topic'] = topic.id
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentUpdateView(CommentViewMixin, UpdateView):
    model = Comment
    form_class = AddCommentForm


class CommentDeleteView(CommentViewMixin, DeleteView):
    model = Comment
