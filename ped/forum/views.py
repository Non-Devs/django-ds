from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Thread


class ForumView(ListView):

    model = Thread
    template_name = 'forum/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['forum'] = Thread.objects.all()
        return context
