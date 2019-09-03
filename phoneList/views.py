from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound


from .models import phoneNumber
 
# получение данных из бд
def index(request):
    Pnumber = phoneNumber.objects.all()
    return render(request, "index.html", {"Pnumber": Pnumber})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        newNumber = phoneNumber()
        newNumber.phoneNumber_name = request.POST.get("name")
        newNumber.phoneNumber_number = request.POST.get("numberPhone")
        newNumber.save()
    return HttpResponseRedirect("/")

# изменение данных в бд
def edit(request, id):
    try:
        newNumber = phoneNumber.objects.get(id=id)
 
        if request.method == "POST":
            newNumber.phoneNumber_name = request.POST.get("name")
            newNumber.phoneNumber_number = request.POST.get("numberPhone")
            newNumber.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"newNumber":  newNumber})
    except phoneNumber.DoesNotExist:
            return HttpResponseNotFound("<h2>Контакта не существует</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        newNumber = phoneNumber.objects.get(id=id)
        newNumber.delete()
        return HttpResponseRedirect("/")
    except phoneNumber.DoesNotExist:
        return HttpResponseNotFound("<h2>Контакта не существует</h2>")