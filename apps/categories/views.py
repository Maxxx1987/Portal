from django.shortcuts import render
from apps.categories.models import Category, Topic
from django.views.generic.list import ListView


class CategoryListView(ListView):
    model = Category
    ordering = ('title',)
    context_object_name = 'obj_list'
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
        return qs.filter(category__slug=self.kwargs['slug'])
