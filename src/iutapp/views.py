from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView

from iutapp.models import Contact, Personnel


class Home(TemplateView):
    model = Contact
    template_name = 'iutapp/contact_list.html'

# Create your views here.
class ContactCreate(CreateView):
    model = Contact
    template_name = 'iutapp/contact_create.html'
    fields = ('lastname','surname','date_of_birthday','email','content')

class About(TemplateView):
    model = Contact
    template_name = 'iutapp/about.html'

class Filieres(TemplateView):
    model = Contact
    template_name = 'iutapp/filieres.html'

class DetailsFilieres(TemplateView):
    model = Contact
    template_name = 'iutapp/detailsfilieres.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filieres'] = [
            {
                'title': 'Gestion des Banques',
                'diplome': 'Licence Professionnelle en Gestion des Banques',
                'admission': 'BAC séries C, D, G2',
                'debouche': 'Gestionnaires des Banques',
                'image': '/img/gb1.jpeg'
            },
            {
                'title': 'Gestion des Ressources Humaines',
                'diplome': 'Licence Professionnelle en Gestion des Ressources Humaines',
                'admission': 'BAC séries C, D, G2',
                'debouche': 'Consultant en RH',
                'image': '/img/fil.webp'
            },
            {
                'title': 'Gestion des Entreprises',
                'diplome': 'Licence Professionnelle en Gestion des Entreprises',
                'admission': 'BAC séries C, D, G2',
                'debouche': 'Gestionnaires des entreprises',
                'image': '/img/iutgirl.jpg'
            },
            {
                'title': 'Gestion Commerciale',
                'diplome': 'Licence Professionnelle en Gestion Commerciale',
                'admission': 'BAC séries C, D, G2, G3',
                'debouche': 'Cadres commerciaux',
                'image': '/img/ig.jpg'
            },
            {
                'title': 'Informatique de Gestion',
                'diplome': 'Licence Professionnelle en Informatique de Gestion',
                'admission': 'BAC séries C, D',
                'debouche': 'Postes d’analystes programmeur',
                'image': '/img/ig2.jpg'
            },
            {
                'title': 'Gestion des Transports et Logistique',
                'diplome': 'Licence Professionnelle en Gestion des Transports et Logistique',
                'admission': 'BAC séries C, D, G2',
                'debouche': 'Gestionnaires de transport et de logistique',
                'image': '/img/gtl.jpeg'
            }
        ]
        return context

class PersonnelListView(ListView):
    model = Personnel
    template_name = 'personnel/list.html'
    context_object_name = 'personnel'
