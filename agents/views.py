import random

from django.core.mail import send_mail
from django.urls import reverse
from django.views import generic

from agents.forms import AgentModelForm
from leads.models import Agent

from .mixins import OrganizerAndLoginRequiredMixin


class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject="You are invinted to be an agent",
            message="You added as an agent on DJCRM, please come login to start working.",
            from_email=self.request.user.email,
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentUpdateView(generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
