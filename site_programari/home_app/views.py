from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import Serviciu
from django.utils import timezone


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')  # Redă template-ul about.html


def cursuri(request):
    return render(request, 'cursuri.html')  # Redă template-ul programari.html


def dashboard(request):
    return render(request, 'dashboard.html')  # Redă template-ul dashboard.html


def disponibilitate(request):
    return render(request, 'disponibilitate.html')  # Redă template-ul dashboard.html


def AlegeServiciu(request):
    return render(request, 'AlegeServiciu.html')  # Redă template-ul dashboard.html


from django.shortcuts import render


def AlegeServiciu(request):
    servicii = Serviciu.objects.all()  # Preia toate serviciile din baza de date
    return render(request, 'AlegeServiciu.html', {'servicii': servicii})


from .forms import ClientaForm


def formular_clienta(request):
    if request.method == 'POST':
        form = ClientaForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează datele în baza de date
            return redirect('AlegeServiciu')  # Redirecționează la pagina de alegere a serviciului
    else:
        form = ClientaForm()
    return render(request, 'formular_clienta.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Serviciu, Clienta


def confirma_serviciul(request):
    if request.method == 'POST':
        serviciu_id = request.POST.get('serviciu_id')
        serviciu = get_object_or_404(Serviciu, id=serviciu_id)

        # Salvarea serviciului selectat în sesiune (sau direct într-o bază de date)
        request.session['serviciu_selectat'] = serviciu.nume

        # Poți salva și în baza de date dacă ai deja datele cliente salvate
        # clienta = Clienta.objects.last()  # Ex. ultima clientă înregistrată
        # clienta.serviciu_selectat = serviciu
        # clienta.save()

        return redirect('finalizare_programare')  # Redirecționează către pagina următoare
    return redirect('alegerea_serviciului')


def finalizare_programare(request):
    serviciu_selectat = request.session.get('serviciu_selectat', None)
    if not serviciu_selectat:
        return redirect('alegerea_serviciului')  # Dacă nu există serviciu selectat, redirecționează înapoi

    return render(request, 'finalizare_programare.html', {'serviciu_selectat': serviciu_selectat})


from datetime import time
from .models import Programare, Serviciu, Clienta
from .forms import DataProgramareForm


def finalizare_programare(request):
    serviciu_selectat = request.session.get('serviciu_selectat', None)
    if not serviciu_selectat:
        return redirect('alegerea_serviciului')  # Redirecționează dacă nu există serviciu selectat

    ore_disponibile = [
        time(hour, 0) for hour in range(9, 18)
    ]  # Interval: 9:00 - 18:00 (poți ajusta intervalul)
    ore_finale = ore_disponibile

    if request.method == 'POST':
        form = DataProgramareForm(request.POST)
        if form.is_valid():
            data_selectata = form.cleaned_data['data']
            programari_existente = Programare.objects.filter(data=data_selectata)

            # Găsește orele deja rezervate
            ore_rezervate = [programare.ora for programare in programari_existente]

            # Elimină orele rezervate din lista de ore disponibile
            ore_finale = [ora for ora in ore_disponibile if ora not in ore_rezervate]

            # Salvează data în sesiune (opțional)
            request.session['data_selectata'] = str(data_selectata)

    else:
        form = DataProgramareForm()

    return render(request, 'finalizare_programare.html', {
        'form': form,
        'serviciu_selectat': serviciu_selectat,
        'ore_disponibile': ore_finale
    })


from datetime import datetime


def confirma_programare(request):
    if request.method == 'POST':
        ora_selectata = request.POST.get('ora_selectata')
        data_selectata_str = request.session.get('data_selectata')
        serviciu_selectat = request.session.get('serviciu_selectat')

        if data_selectata_str and ora_selectata and serviciu_selectat:
            try:
                # Conversia orei în format valid
                ora_validata = datetime.strptime(ora_selectata, "%H:%M").time()

                # Conversia datelor din șir de caractere în obiect datetime.date
                data_selectata = datetime.strptime(data_selectata_str, "%Y-%m-%d").date()

                # Verificăm dacă data aleasă este în viitor
                if data_selectata < timezone.localdate():  # Verificăm dacă data aleasă este în trecut
                    messages.error(request, 'Nu puteți selecta o dată din trecut.')
                    return redirect('finalizare_programare')  # Redirecționează înapoi la pagina finalizare_programare

                # Salvează programarea
                clienta = Clienta.objects.last()  # Înlocuiește cu logica potrivită pentru a obține clienta corectă
                serviciu = Serviciu.objects.get(nume=serviciu_selectat)
                Programare.objects.create(
                    clienta=clienta,
                    serviciu=serviciu,
                    data=data_selectata,
                    ora=ora_validata
                )

                return render(request, 'confirmare_programare.html', {
                    'serviciu': serviciu,
                    'data': data_selectata,
                    'ora': ora_validata
                })
            except ValueError:
                # Gestionarea erorilor de conversie
                return redirect('finalizare_programare')

    return redirect('finalizare_programare')


from .models import Appointment

def dashboard(request):
    appointments = Appointment.objects.all()
    # Calculăm statisticile
    total_hours = 0
    total_income = 0
    for appointment in appointments:
        # Calculăm orele lucrate și venitul total
        total_hours += int(appointment.duration.split()[0])  # presupunem că durata este în format "Xh" sau "Xh Ym"
        total_income += appointment.price

    context = {
        'appointments': appointments,
        'total_hours': total_hours,
        'total_income': total_income,
        'client_count': appointments.count(),
    }
    return render(request, 'dashboard.html', context)