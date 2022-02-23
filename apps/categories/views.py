from django.shortcuts import render, redirect
from apps.categories.models import Category, Topic
from django.views.generic.list import ListView
from apps.categories.forms import AddTopicForm
from django.views.generic.edit import CreateView


class CategoryListView(ListView):
    model = Category
    ordering = ('title',)
    # context_object_name = 'foobar_list'
    template_name = 'category_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active=True)


def category_list(request, **kwargs):
    data = Category.objects.filter(is_active=True).order_by('title')
    context = {'obj_list': data}
    return render(request, 'category_list.html', context=context)


class TopicListView(ListView):
    model = Topic
    ordering = ('-created_at',)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__url_assign=self.kwargs['assign'])


def add_topic(request, **kwargs):
    if request.method == 'POST':
        form = AddTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return redirect(topic.category.get_absolute_url())

    form = AddTopicForm(
        initial={
            'category': Category.objects.get(url_assign=kwargs['assign']).id
        }
    )
    context = {
        'form': form,
    }
    return render(request, 'categories/add_topic.html', context=context)


class TopicCreateView(CreateView):
    initial = {'status': 'enabled'}
    form_class = AddTopicForm
    template_name = 'categories/add_topic.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['category'] = Category.objects.get(url_assign=self.kwargs['assign']).id
        return initial

    def get_success_url(self):
        return self.object.category.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
