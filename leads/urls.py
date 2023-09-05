from django.urls import path

from leads.views import LeadCreateView, LeadDeleteView, LeadDetailView, LeadListView, LeadUpdateView, lead_create, lead_delete, lead_detail, lead_list, lead_update

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="lead-list"),
    path("<int:pk>", LeadDetailView.as_view(), name="lead-detail"),
    path("<int:pk>/update", LeadUpdateView.as_view(), name="lead-update"),
    path("<int:pk>/delete", LeadDeleteView.as_view(), name="lead-delete"),
    path("create/", LeadCreateView.as_view(), name="lead-create"),
    ]
