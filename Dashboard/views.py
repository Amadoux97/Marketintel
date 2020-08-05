from django.shortcuts import render
from .models import Entreprise



def Senegal(request):
    A = Entreprise.objects.filter(pays__contains='Senegal')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Senegal.html', {'A': A, 'B':B})

def Algerie(request):
    A = Entreprise.objects.filter(pays__contains='algerie')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Algerie.html', {'A': A, 'B':B})

def Burkina(request):
    A = Entreprise.objects.filter(pays__contains='Burkina')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Burkina.html', {'A': A, 'B':B})

def congoBrazza(request):
    A = Entreprise.objects.filter(pays__contains='Congo Brazzaville')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/congoBrazza.html', {'A': A, 'B':B})

def congoKinshasa(request):
    A = Entreprise.objects.filter(pays__contains='Congo Kinshasa')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/congoKinshasa.html', {'A': A, 'B':B})

def Egypte(request):
    A = Entreprise.objects.filter(pays__contains='Egypte')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Egypte.html', {'A': A, 'B':B})

def Ivorycoast(request):
    A = Entreprise.objects.filter(pays__contains='Ivory Coast')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Ivorycoast.html', {'A': A, 'B':B})

def Mali(request):
    A = Entreprise.objects.filter(pays__contains='Mali')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Mali.html', {'A': A, 'B':B})

def Maroc(request):
    A = Entreprise.objects.filter(pays__contains='Maroc')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Maroc.html', {'A': A, 'B':B})

def Nigeria(request):
    A = Entreprise.objects.filter(pays__contains='Nigeria')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Nigeria.html', {'A': A, 'B':B})

def Togo(request):
    A = Entreprise.objects.filter(pays__contains='Togo')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Togo.html', {'A': A, 'B':B})

def Tunisie(request):
    A = Entreprise.objects.filter(pays__contains='Tunisie')
    B = A.values('nom', 'secteur')

    return render(request, 'Dashboard/Tunisie.html', {'A': A, 'B':B})



    return render(request, 'Dashboard/test.html', {'A': A, 'B':B})

def sect(request):
    A = Entreprise.objects.filter(pays__contains='Tunisie')
    tables = A.values('' 'secteur')
    result = Entreprise.objects.filter(secteur__contains='Agences')
    result1 = Entreprise.objects.filter(secteur__contains='Ingénierie')
    result2 = Entreprise.objects.filter(secteur__contains='Internet')
    Entreprise.objects.annotate(num_results1=Count)
    data = []
    labels = []

def dashboard(request):
    entreprises=Entreprise.objects.all()
    return render(request, 'Dashboard/test.html', {'entreprises': entreprises})

    


# Create your views here.
