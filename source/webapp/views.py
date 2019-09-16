from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import IssueForm
from webapp.models import Article, Issue, STATUS_CHOICES


def index_view(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html', context={
        'num_visits': num_visits
    })


def issue_list(request):
    issues = Issue.objects.all()
    pk = request.session.get('pk')
    for issue in issues:
       request.session['pk'] = issue.pk
    print(pk)
    context = {
        'issues': issues,
        'pk': pk
    }

    return render(request, 'issue_list.html', context)


def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'article_list.html', context)


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    return render(request, 'view.html', context={
        'article': article
    })


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)
        return redirect('article_view', pk=article.pk)


def issue_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    context = {
        'issue': issue
    }

    return render(request, 'issue_view.html', context)


def issue_create_view(request):
    if request.method == 'GET':
        form = IssueForm()
        context = {
            'status': STATUS_CHOICES,
            'form': form
        }
        return render(request, 'issue_create.html', context)
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                finish_date=form.cleaned_data['finish_date']
            )
            return redirect('issue_view', pk=issue.pk)
        else:
            return render(request, 'issue_create.html', context={'form': form})


def issue_delete_view(request):
    issue__id = request.GET.get('issue_id')
    issue = Issue.objects.get(pk=issue__id)
    issue.delete()
    issues = Issue.objects.all()
    context = {
        'issues': issues
    }
    return render(request, 'issue_list.html', context)


def issue_update_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'GET':
        form = IssueForm(data={
            'description': issue.description,
            'status': issue.status,
            'finish_date': issue.finish_date
        })
        return render(request, 'issue_update.html', context={'form': form, 'issue': issue, 'status': STATUS_CHOICES})
    elif request.method == 'POST':
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.finish_date = form.cleaned_data['finish_date']
            issue.save()
            return redirect('issue_list')
        else:
            return render(request, 'issue_update.html', context={'form': form, 'issue': issue})


def issue_get_delete(request):
    issues = Issue.objects.all()
    data = request.GET.get('issue_pk')
    if request.method == 'GET':
        issues_delete = []
        issues_pk = []
        for issue in issues:
            if str(issue.pk) in data:
                issues_delete.append(issue)
                issues_pk.append(issue.pk)
        return render(request, 'issues_delete.html', context={
            'issues': issues_delete,
            'issues_pk': issues_pk
        })


def issue_post_delete(request):
    issues = Issue.objects.all()
    if request.method == "POST":
        if request.POST.get('cancel') != 'no':
            issue_delete = request.POST.get('del')
            for issue in issues:
                if str(issue.pk) in issue_delete:
                    issue.delete()
        return redirect('issue_list')


