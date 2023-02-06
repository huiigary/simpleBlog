from django.shortcuts import render
from django.http import HttpResponse
from .models import Post  # import the Post-model in the models folder
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# mock post data for testing
posts = [
    {'author': 'Author 1',
     'title': 'blog post 1',
     'content': 'first post',
     'date_posted': 'Jan.1, 2023'},

    {'author': 'Author 2',
     'title': 'blog post 2',
     'content': 'first post',
     'date_posted': 'Feb.2, 2023'}
]


def home(request):
    context = {
        'posts': Post.objects.all()  # Using the data from the Post-model in the database
    }
    # The 3rd arg in render (context) is like props and passes data to the views template html
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1> Blog home </h1>')


class PostListView(ListView):
    # tell list view what model to query to create the list view (all you need to create listview... however in this case we need to add more code)
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # Listview default calls "object_list"... Instead set the variable to be "posts"
    context_object_name = 'posts'
    # order by "date_posted" attribute of a Post. "-date_posted" makes it newest --> oldests
    ordering = ['-date_posted']
    paginate_by = 5


# Note1: This is different from "PostListView" because we followed the expected Django formatting hence write fewer lines
# Note2:This class-view will find the django expected html naming post_detail.html (<app>/<model>_<viewtype>.html)... hence no need to write the "template_name" line
# Note3: Post_detail.html now uses "object" as expected from django to access Post objects  (did this to avoid adding line: context_object_name...)
class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # creating override form_valid function
        # set the author to current login user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # creating override form_valid function
        # set the author to current login user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):     # test_func --> Ensures current user is same as the post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
