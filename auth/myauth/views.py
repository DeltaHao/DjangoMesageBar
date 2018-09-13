from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import my_form, my_edit_form, my_login_form
from .models import normal_user_form, Mesage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .sms_send import send_sms
from random import randint
import time
from django.core.paginator import Paginator
@csrf_exempt


# 主页
def home(request):
    # 文件名为'home.html'
    mesages = Mesage.objects.all()
    paginator = Paginator(mesages, 6)
    page_num = request.GET.get('page',1)
    page_of_mesages = paginator.get_page(page_num)

    content = { 'mesages': page_of_mesages.object_list,'page_of_mesages': page_of_mesages}
    return render(request, 'myauth/home.html',content)


# 登录
def log_in(request):
    if request.method == 'POST':
        login_form = my_login_form(data=request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            login(request, user)
            return redirect('myauth:home')
    else:
        if request.user.is_authenticated:
            return redirect('myauth:home')
        else:
            login_form = my_login_form()

    content = {'login_form': login_form}
    return render(request, 'myauth/log_in.html',content)


# 登出
def log_out(request):
    logout(request)
    return redirect('myauth:log_in')


# 注册
def register(request):
    if request.method == 'POST':
        reg_form = my_form(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user = authenticate(username=reg_form.cleaned_data['username'], password=reg_form.cleaned_data['password1'])
            user.email = reg_form.cleaned_data['email']
            normal_user_form(user=user, nickname=reg_form.cleaned_data['nickname'], birthday=reg_form.cleaned_data['birthday'], phonenumber=reg_form.cleaned_data['phonenumber']).save()
            login(request, user)
            return redirect('myauth:home')
    else:
        reg_form = my_form()
        content = {'reg_form': reg_form}
        return render(request, 'myauth/register.html', content)
    content = {'reg_form': reg_form}
    return render(request, 'myauth/register.html', content)


# 个人中心
@login_required(login_url='myauth:log_in')
def user_center(request):
    content = {'user': request.user, 'mesages': Mesage.objects.all()}
    return render(request, 'myauth/user_center.html', content)


# 个人信息编辑
@login_required(login_url='myauth:log_in')
def user_edit(request):
    if request.method == 'POST':
        edit_form = my_edit_form(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            request.user.normal_user_form.nickname = edit_form.cleaned_data['nickname']
            request.user.normal_user_form.birthday = edit_form.cleaned_data['birthday']
            request.user.normal_user_form.phonenumber = edit_form.cleaned_data['phonenumber']
            request.user.normal_user_form.save()
            return redirect('myauth:user_center')
    else:
        edit_form = my_edit_form(instance=request.user)

    content = {'edit_form': edit_form, 'user': request.user,}
    return render(request, 'myauth/user_edit.html', content)


# 修改密码
@login_required(login_url='myauth:log_in')
def password_edit(request):
    error = ''
    if request.method == 'POST':
        password_edit_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_edit_form.is_valid():
            password_edit_form.save()
            return redirect('myauth:log_in')
    else:
        password_edit_form = PasswordChangeForm(user=request.user)

    content = {'password_edit_form': password_edit_form, 'user': request.user, 'error': error}
    return render(request, 'myauth/password_edit.html', content)


# 删除留言
@login_required(login_url='myauth:log_in')
def delete(request, item_id):
    a = Mesage.objects.get(id=item_id)
    a.delete()
    return redirect("myauth:user_center")

#点赞
@login_required(login_url='myauth:log_in')
def approval(request, item_id):
    a = Mesage.objects.get(id=item_id)
    a.approval += 1
    a.save()
    return redirect("myauth:home")


# 发布留言
@login_required(login_url='myauth:log_in')
def publish(request):
    if request.method == "POST":
        if request.POST['content'] == '':
            return render(request, "myauth/publish.html", {'警告': '请输入内容!'})
        else:
            a = Mesage(content=request.POST['content'], created_time=time.time(), author=request.user, approval=0)
            a.save()
            return redirect('myauth:home')
    else:
        return render(request, "myauth/publish.html")

def intro(requset):
    return render(requset, "myauth/intro.html")


