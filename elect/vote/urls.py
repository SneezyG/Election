from django.urls import path
from vote.views import Index, Lga_vote, Ward_vote, Unit_vote, New_vote



urlpatterns = [
  path('', Index, name='index'),
  path('vote/lga/<str:name>/', Lga_vote.as_view(), name='get_lga'),
  path('vote/lga/', Lga_vote.as_view(), name='post_lga'),
  path('vote/ward/<str:name>/<int:lga_id>/', Ward_vote.as_view(), name='get_ward'),
  path('vote/ward/', Ward_vote.as_view(), name='post_ward'),
  path('vote/unit/', Unit_vote.as_view(), name='post_unit'),
  path('vote/new/', New_vote.as_view(), name='new_vote'),
]