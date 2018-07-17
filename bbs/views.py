from django.shortcuts import render, redirect
from django.contrib import auth
from bbs.models import Article, UserInfo


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)

        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj)
        if user_obj:
            print("ok")
            auth.login(request, user_obj)
            return redirect("/homepage/")

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/homepage/")


def homepage(request):
    article_list = Article.objects.all()
    return render(request, "homepage.html", {"article_list": article_list})


def register(request):
    return render(request, "register.html")


def not_found(request):
    return render(request, "not_found.html")


def homesite(request, username):
    """
    查询
    :param request:
    :param username:
    :return:
    """

    # 查询当前站点的用户对象
    user = UserInfo.objects.filter(username=username).first()
    if not user:
        return render(request, "not_found.html")
    # 查询当前站点对象
    blog = user.blog

    # 查询当前用户发布的所有文章
    article_list = Article.objects.filter(user__username=username)

    # 查询当前站点每一个分类的名称以及对应的文章数

    # 查询当前站点每一个标签的名称以及对应的文章数

    return render(request, "homesite.html", {"article_list": article_list, "blog": blog})
