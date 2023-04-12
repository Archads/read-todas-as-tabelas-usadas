from django.shortcuts import render, redirect
from clinicasmedicas.forms import ClinicaForm, EspecialidadeForm, MedicoForm, ClinicaMedicoForm
from clinicasmedicas.models import Clinica, Especialidade, Medico, ClinicaMedico
# Create your views here.
#Antes: data['db'] = Clinica.objects.all
def home(request):
    data = {}
    data['clinica'] = Clinica.objects.all()
    data['especialidade'] = Especialidade.objects.all()
    data['medico'] = Medico.objects.all()
    data['clinicas_medico'] = ClinicaMedico.objects.all()
    return render(request, 'home.html', data)
#Alterado: data['forms'] = ClinicaForm()
def form(request):
    data = {}
    data['clinica_form'] = ClinicaForm()
    data['especialidade_form'] = EspecialidadeForm()
    data['medico_form'] = MedicoForm()
    data['clinica_medico_form'] = ClinicaMedicoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    