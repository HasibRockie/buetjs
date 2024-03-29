from django.contrib import admin
from django.urls import path
from home import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('campus/',views.campus, name="campus"),
    path('hall/',views.hall, name="hall"),
    path('club/',views.club, name="club"),
    path('sports/',views.sports, name="sports"),
    path('alumni/',views.alumni, name="alumni"),
    path('gellery/',views.gellery,name="gellery"),
    path('blog/',views.blog, name="blog"),
    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name="about"),
    path('posts/<str:id>/',views.post, name="post"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.accountSettings, name="edit"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/edit/images/<str:id>/',views.editImage, name="editImage"),
    path('dashboard/edit/members/<str:id>/',views.editMember, name="editMember"),
    path('dashboard/edit/posts/<str:id>/',views.editPost, name="editPost"),
    path('dashboard/edit/images/<str:id>/delete',views.deleteImage, name="deleteImage"),
    path('dashboard/edit/members/<str:id>/delete',views.deleteMembers, name="deleteMember"),
    path('dashboard/edit/posts/<str:id>/delete',views.deletePost, name="deletePost"),
    path('dashboard/edit/about/',views.editAbout, name="editAbout"),
    path('dashboard/add/image/',views.addImage, name="addImage"),
    path('dashboard/add/member/',views.addMember, name="addMember"),
    path('dashboard/add/post/',views.addPost, name="addPost"),
]