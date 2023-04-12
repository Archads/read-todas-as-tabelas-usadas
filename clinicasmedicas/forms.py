from django.forms import ModelForm
from clinicasmedicas.models import Clinica, ClinicaMedico, Medico, Especialidade

# Create the form class.
class ClinicaForm(ModelForm):
     class Meta:
         model = Clinica
         fields = ["CodCli", "NomeCli", "Endereco", "Telefone", "Email"]

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ['CodEspec', 'NomeEspec', 'Descricao']

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['CodMed', 'NomeMed', 'Genero', 'Telefone', 'Email', 'CodEspec']

class ClinicaMedicoForm(ModelForm):
    class Meta:
        model = ClinicaMedico
        fields = ['CodCli', 'CodMed', 'DataIngresso', 'CargaHorariaSemanal']