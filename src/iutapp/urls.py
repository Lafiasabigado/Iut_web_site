from django.urls import path

from iutapp.views import Home, ContactCreate, About, Filieres, DetailsFilieres, PersonnelListView

app_name = 'iutapp'


urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('create/', ContactCreate.as_view(),name='create'),
    path('about/', About.as_view(), name='about'),
    path('filieres/', Filieres.as_view(), name='filieres'),
    path('details/', DetailsFilieres.as_view(), name='details'),
    path('personnel/', PersonnelListView.as_view(), name='personnel'),
]