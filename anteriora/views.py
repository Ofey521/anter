from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# strona główna wyświetl
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'anteriora/home.html', context)  # do szablonu html about


"""wyswietlanie postow na stronie glownej """


class PostListView(ListView):
    model = Post
    template_name = 'anteriora/home.html'  # < app > / < model > _ < viewtype >.html konwencjonalna nazwa!!!
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


"""wyświetlanie postów usera"""


class UserPostListView(ListView):
    model = Post
    template_name = 'anteriora/user_posts.html'  # < app > / < model > _ < viewtype >.html konwencjonalna nazwa!!!
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


"""LoginRequiredMixin, żeby dodawać posty tylko jako zalogowany użytkownik, a nie random z randomia"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # metoda do określenia, kto pisze posta
        form.instance.author = self.request.user  # ustaw na self.request.user - aktualnie zalogowanego
        return super().form_valid(form)


"""UserPassesTestMixin - żeby nie updateować postów stworzonych przez innych userów"""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # metoda do określenia, kto pisze posta
        form.instance.author = self.request.user  # ustaw na self.request.user - aktualnie zalogowanego
        return super().form_valid(form)

    """Metoda sprawdzająca czy user edytujący posta zgadza się z autorem"""

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # po zatwierdzeniu usunięcia oznaczamy, gdzie strona ma wrócić

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'anteriora/about.html', {'title': 'About'})  # do szablonu html about


def ranking(request):
    return render(request, 'anteriora/ranking.html', {'title': 'Ranking'})


def help(request):
    return render(request, 'anteriora/help.html', {'title': 'Help'})
