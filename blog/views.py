from django.shortcuts import render

from blog.forms import PostCreateForm
from blog.models import Post, Category

def main_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'posts': posts
    }
    return render(request, 'blog/index.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            post_author = request.user
            post.save
    form = PostCreateForm()
    context = {
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required
def my_posts(request):
    posts = Poobjects.filter(author=request.user)
    return render(request, 'blog/user_posts.html',
                  context={'posts': posts})

def search(request):
    query = request.GET.get('q')
    posts = POSTS.objects.filter(title__icontains=query)
    return render(request, 'blog/search.html',
                  context={'post': post})