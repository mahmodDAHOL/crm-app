from django.urls import path

from leads.views import (CategoryDetailView, CategoryListView, LeadCreateView, LeadDeleteView, LeadDetailView,
                         LeadListView, LeadUpadataCategoryView, LeadUpdateView, AssignAgentView)

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
    path("<int:pk>/lead-category-update/",LeadUpadataCategoryView.as_view(), name="lead-category-update"),
    ]
