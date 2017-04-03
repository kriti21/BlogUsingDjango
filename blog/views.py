from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
#from .models import Category
from .models import Article
from .forms import PostForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/article_list.htm', {'articles': articles}) #,'language': language, 'session_language': session_language})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.htm', {'article': article})

def article_like(request, pk):
    if pk:
        a = Article.objects.get(id=pk)
        count = a.likes
        count+=1
        a.likes = count
        a.save()
    #return HttpResponseRedirect('blog/article/%s' %  pk)
    return render(request, 'blog/article_detail.htm', {'article': a})

def article_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.htm', {'form': form})
