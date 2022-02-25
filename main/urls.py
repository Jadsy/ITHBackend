from django.contrib import admin
from django.urls import path, include
from main import views
urlpatterns = [
    path('my-profile/', views.ProfileList.as_view()),
    path('my-projects/', views.ProjectList.as_view()),
    path('my-issues/', views.IssueList.as_view()),
    path('my-assignees/', views.AssigneesList.as_view()),

    path('my-status/', views.StatusList.as_view()),
    path('my-severities/', views.SeverityList.as_view()),
    path('my-types/', views.TypeList.as_view()),
]
