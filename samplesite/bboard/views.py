from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import Bb


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


def by_author(request, author_name):
    x = request.user.id
    author = author_name
    posts = Bb.objects.filter(author=request.user)
    rubrics = Rubric.objects.all()
    context = {'author': author, 'posts': posts, 'rubrics': rubrics, 'x': x}
    return render(request, 'bboard/by_author.html', context)
