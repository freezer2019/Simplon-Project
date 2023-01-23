from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from simplon_app.models import CustomUser, Staffs, AdminHOD, Participants

@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def admin_home(request):
    context={
        'all_participant_count': Participants.objects.all().count(),
    }
    return render(request, "hod_template/home_content.html", context)


def add_participant(request):
    return render(request, "hod_template/add_participant_template.html")


def add_participant_save(request):
    if request.method != "POST":
        messages.error(request, "Méthode invalide !")
        return redirect('add_participant')
    else:
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numero_de_telephone = request.POST.get('numero_de_telephone')
        email = request.POST.get('email')
        try:
            participant_model = Participants(nom=nom, prenom=prenom, numero_de_telephone=numero_de_telephone, email=email)
            participant_model.save()
            messages.success(request, "Participant ajouté avec succès !")
            return redirect('add_participant')
        except:
            messages.error(request, "Erreur d'ajout du participant !")
            return redirect('add_participant')


def manage_participant(request):
    participants = Participants.objects.all()
    context = {
        "participants": participants
    }
    return render(request, "hod_template/manage_participant_template.html", context)


def edit_participant(request, participant_id):
    participant = Participants.objects.get(id=participant_id)
    context = {
        "participant": participant,
        "id": participant_id
    }
    return render(request, "hod_template/edit_participant_template.html", context)


def edit_participant_save(request):
    if request.method != "POST":
        HttpResponse("Méthode invalide !")
    else:
        participant_id = request.POST.get('participant_id')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numero_de_telephone = request.POST.get('numero_de_telephone')
        email = request.POST.get('email')

        try:
            participant = Participants.objects.get(id=participant_id)
            participant.nom = nom
            participant.prenom = prenom
            participant.numero_de_telephone = numero_de_telephone
            participant.email = email
            participant.save()

            messages.success(request, "Participant modifié avec succès !")
            return redirect('/edit_participant/'+participant_id)

        except:
            messages.error(request, "Erreur de modification du participant !")
            return redirect('/edit_participant/'+participant_id)



def delete_participant(request, participant_id):
    participant = Participants.objects.get(id=participant_id)
    try:
        participant.delete()
        messages.success(request, "Données participant effacées avec succès !")
        return redirect('manage_participant')
    except:
        messages.error(request, "Erreur de suppression des données du participant !")
        return redirect('manage_participant')


def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Méthode invalide !")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile mis à jour avec succès !")
            return redirect('admin_profile')
        except:
            messages.error(request, "Erreur de mise à jour du profile !")
            return redirect('admin_profile')