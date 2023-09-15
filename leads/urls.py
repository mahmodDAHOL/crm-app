from django.urls import path

from leads.views import (AssignAgentView, CategoryCreateView,
                         CategoryDeleteView, CategoryDetailView,
                         CategoryListView, CategoryUpdateView,
                         FollowUpCreateView, FollowUpDeleteView,
                         FollowUpUpdateView, LeadCategoryUpdateView,
                         LeadCreateView, LeadDeleteView, LeadDetailView,
                         LeadListView, LeadUpdateView)

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>", LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update", LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete", LeadDeleteView.as_view(), name="lead-delete"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
    path("<int:pk>/assign-agent/", AssignAgentView.as_view(), name="assign-agent"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path("<int:pk>/lead-category-update/",LeadCategoryUpdateView.as_view(), name="lead-category-update"),
    path('<int:pk>/followups/create/', FollowUpCreateView.as_view(), name='lead-followup-create'),
    path('followups/<int:pk>/', FollowUpUpdateView.as_view(), name='lead-followup-update'),
    path('followups/<int:pk>/delete/', FollowUpDeleteView.as_view(), name='lead-followup-delete'),
    ]
