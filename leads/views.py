from django.shortcuts import render, redirect

from leads.forms import LeadForm
from .models import Agent, Lead

def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads":leads}
    return render(request, "leads/lead_list.html", context=context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead":lead}
    return render(request, "leads/lead_detail.html", context=context)

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print("the form is valid")
            print(form.cleaned_data)
            cleaned_data = form.cleaned_data
            first_name = cleaned_data["first_name"]
            last_name = cleaned_data["last_name"]
            age = cleaned_data["age"]
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")
    context = {
        "form":form
    }
    return render(request, "leads/lead_create.html", context=context)
    