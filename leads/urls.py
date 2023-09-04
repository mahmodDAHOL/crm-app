from django.urls import path

from leads.views import lead_create, lead_detail, lead_list

app_name = "leads"

urlpatterns = [
    path("", lead_list),
    path("<int:pk>", lead_detail),
    path("create/", lead_create),
    ]
