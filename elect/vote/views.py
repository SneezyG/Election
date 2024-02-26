from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.http import require_http_methods
from vote.models import AnnouncedLGAResults, AnnouncedPuResults, LGA, PollingUnit, Ward, NewVote
from django.db.models import Sum
from django.urls import reverse
from vote.forms import VoteForm


# Create your views here.

@require_http_methods(["GET"])
def Index(request):
  
   """
   show total votes.
   """
    
   template = "vote/base.html"
   
   results = AnnouncedLGAResults.objects.values('party_abbreviation').annotate(votes=Sum('party_score')).order_by('-votes')
   
   locations = LGA.objects.values_list("lga_name", flat=True).distinct()

   destination = reverse("vote:post_lga")
   
   context = {
     "results": results,
     "locations": locations,
     "destination": destination,
     "searchText": "Enter local government"
   }
   
   return render(request, template, context)
   
 


class New_vote(View) :
   
   """
   store new votes results 
   """
   post_template = "vote/success.html"
   get_template = "vote/create.html"
   
   
   def get(self, request):
     return render(request, self.get_template)

   def post(self, request):
     form = VoteForm(request.POST)
     if form.is_valid():
        form.save()
        return render(request, self.post_template)
     else:
       error = '<p class="text-center text-danger p-2">Invalid inputs</p>'
       return render(request, self.get_template, {"form_error":error})
   
  
class Lga_vote(View):
  
   """
   show votes for a particular local government 
   """
    
   template = "vote/lga.html"
   
   def get_context(self, name):
     lga = get_object_or_404(LGA, lga_name=name)
     lga_name = lga.lga_name
     lga_id = lga.lga_id
     
     results = AnnouncedLGAResults.objects.filter(lga_name=str(lga_id)).values('party_abbreviation').annotate(votes=Sum('party_score')).order_by('-votes')
     
     wards = Ward.objects.filter(lga_id=lga_id).values_list("ward_name", flat=True).distinct()
     
     destination = reverse("vote:post_ward")
     
     return {
       "results": results,
       "locations": wards,
       "destination": destination,
       "area": lga_name,
       "searchText": "Enter ward name",
       "lgaId": lga_id
     }
   
   def get(self, request, name):
     context = self.get_context(name.strip())
     return render(request, self.template, context)
    
   def post(self, request):
     name = request.POST.get('name').strip()
     context = self.get_context(name)
     return render(request, self.template, context)
   
   
   
   

class Ward_vote(View):
  
   """
   show votes for a particular ward
   """
   
   template = "vote/ward.html"
   
   def get_context(self, name, lga_id):
     ward = get_object_or_404(Ward, ward_name=name, lga_id=lga_id)
     ward_name = ward.ward_name
     ward_id = ward.ward_id
     
     lga_name = LGA.objects.get(lga_id=lga_id).lga_name
     
     units = PollingUnit.objects.filter(ward_id=ward_id)
     unit_ids = units.values_list("uniqueid", flat=True)
     unit_ids = [str(unit) for unit in unit_ids]
     unit_names = units.values_list("polling_unit_name", flat=True).distinct()
     
     results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=unit_ids).values('party_abbreviation').annotate(votes=Sum('party_score')).order_by('-votes')
     
     
     destination = reverse("vote:post_unit")
     
     return {
       "results": results,
       "locations": unit_names,
       "destination": destination,
       "area": ward_name,
       "searchText": "Enter polling unit name",
       "lgaName": lga_name,
       'wardId': ward.uniqueid,
       'lgaId': lga_id
     }
   
   def get(self, request, name, lga_id):
     context = self.get_context(name.strip(), lga_id)
     return render(request, self.template, context)
    
   def post(self, request):
     name = request.POST.get('name').strip()
     lga_id = int(request.POST.get('lga').strip())
     context = self.get_context(name, lga_id)
     return render(request, self.template, context)
   
   
   
 
class Unit_vote(View):
  
   """
   show votes in a particular Polling unit
   """
    
   template = "vote/unit.html"
   
   def get_context(self, name, ward_id, lga_id):
     
     ward = Ward.objects.get(uniqueid=ward_id)
     
     unit = get_object_or_404(PollingUnit, polling_unit_name=name, ward_id=ward.ward_id)
     unit_name = unit.polling_unit_name
     unit_id = str(unit.uniqueid)
     
     lga = LGA.objects.get(lga_id=lga_id)
     
     results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unit_id).values('party_abbreviation').annotate(votes=Sum('party_score')).order_by('-votes')
     
     return {
       "results": results,
       "area": unit_name,
       "lgaName": lga.lga_name,
       "wardName": ward.ward_name,
       "lgaId": lga.lga_id
     }
   
   def get(self, request, name):
     pass
    
   def post(self, request):
     name = request.POST.get('name').strip()
     ward_id = request.POST.get('ward').strip()
     lga_id = int(request.POST.get('lga').strip())
     context = self.get_context(name, ward_id, lga_id)
     return render(request, self.template, context)
