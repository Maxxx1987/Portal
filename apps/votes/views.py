from apps.votes.models import Vote
from django.views.generic.edit import CreateView, DeleteView
from apps.votes.forms import AddVoteForm


class VoteCreateView(CreateView):
    model = Vote
    form_class = AddVoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.comment.topic.get_absolute_url()


class VoteDeleteView(DeleteView):
    model = Vote
    pk_url_kwarg = 'vote_id'

    def get_success_url(self):
        return self.object.comment.topic.get_absolute_url()
