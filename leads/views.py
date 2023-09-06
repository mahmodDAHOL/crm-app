from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from leads.forms import LeadForm, LeadModelForm

from .models import Agent, Lead


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"
    
def landing_page(request):
    return render(request, "landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/lead_list.html", context=context)


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, "leads/lead_detail.html", context=context)


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
        
    def form_valid(self, form):
        send_mail(
            subject="a lead has been created",
            message="Go to the site to see the new lead",
            from_email="mahmod@aldahool.com",
            recipient_list=["ali@ali.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {"form": form}
    return render(request, "leads/lead_create.html", context=context)

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
    

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead,
    }

    return render(request, "leads/lead_update.html", context)


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    def get_success_url(self) -> str:
        return reverse("leads:lead-list")
    

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
