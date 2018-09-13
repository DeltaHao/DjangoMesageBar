from django.urls import path, include
from . import views

app_name = 'myauth'
urlpatterns = [
    # 主页及其函数命名为'home'
    path('', views.home, name='home'),

    # 登陆及其函数命名为'log_in'
    path('log_in/', views.log_in, name='log_in'),

    # 登出及其函数命名为'log_out'
    path('log_out/', views.log_out, name='log_out'),

    # 注册及其函数命名为'register'
    path('register/', views.register, name='register'),

    # 个人中心及其函数命名为'user_center'
    path('user_center/', views.user_center, name='user_center'),

    # 个人信息编辑及其函数命名为'user_edit'
    path('user_center/user_edit/', views.user_edit, name='user_edit'),

    # 修改密码及其函数命名为'password_edit'
    path('user_center/password_edit', views.password_edit, name='password_edit'),

    # 留言删除函数命名为delete
    path('user_center/delete/<item_id>', views.delete, name="delete"),

    # 留言发布函数命名为publish
    path('publish/', views.publish, name='publish'),

    # 点赞 approval
    path('user_center/approval/<item_id>', views.approval, name="approval"),

    path('intro/', views.intro, name='intro'),
]
