from django.http import HttpResponse
from django.template import loader
from .models import Member

# GET request to all_members.html
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

# GET request to targeted id member detail.html  
# It will automatically catch the id on the Url route
def details(request, id):
  # retrieve the data boject
  mymember = Member.objects.get(id=id)
  # retrieve the targeted html
  template = loader.get_template('details.html')
  # define the model context that will be passed to the html
  context = {
    'mymember': mymember,
  }
  # send the template to client with data
  return HttpResponse(template.render(context, request))

#GET request to main index page
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())