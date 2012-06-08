from django.shortcuts import render_to_response
from sembrar.models import Project

def home(request):
	projects = Project.objects.all()
	tools_used = request.GET.get("tools_used", "")
	if tools_used:
		projects = projects.filter(tools_used__icontains=tools_used)
	category = request.GET.get("category", "")
	if category:
		projects = projects.filter(category__icontains=category)
	organization = request.GET.get("organization", "")
	if organization:
		projects = projects.filter(organization__icontains=organization)
				
	if projects:
		start = projects[0]
	else:
		start = None	
		
	return render_to_response('home.html', {'qry': tools_used, 'projects': projects, 'start': start, 'category':category, 'organization':organization})
