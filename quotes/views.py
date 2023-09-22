from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Quote, Author, Tag


class QuotesListView(ListView):
    paginate_by = 7
    model = Quote
    template_name = "home.html"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        activities = self.get_related_activities()
        context['quote_list'] = activities
        context['page_obj'] = activities
        return context

    def get_related_activities(self):
        queryset = Quote.objects.filter(tags__tag__contains=self.object)
        paginator = Paginator(queryset, 4)  # paginate_by
        page = self.request.GET.get('page')
        activities = paginator.get_page(page)
        return activities


class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = "quote_new.html"
    fields = ["tags", "author", "quote"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tag_new.html"
    fields = [
        "tag",
    ]
    success_url = "/quote/new/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = "author_new.html"
    fields = ["fullname", "born_date", "born_location", "biography"]
    success_url = "/quote/new/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
