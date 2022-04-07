from django.shortcuts import render, HttpResponseRedirect
from . forms import StudentRegistration
from . models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        var = StudentRegistration(request.POST)
        if var.is_valid():
            name_db = var.cleaned_data['name']
            email_db = var.cleaned_data['email']
            password_db = var.cleaned_data['password']
            save_inDB = User(
                name = name_db,
                email = email_db,
                password = password_db
            )
        #    var.save() 
        save_inDB.save()
        # return HttpResponse('DATA SUCCESSFULLY SAVED')
        var = StudentRegistration() # make blank form again
    else:
        var = StudentRegistration()
    stud_all = User.objects.all()

    return render (request, 'CREATEAPP/addanddisplay.html', {'form': var, 'students':stud_all})

def delete_entry(request, id):
    if request.method == 'POST':
        stud_Del = User.objects.get(pk=id)  
        stud_Del.delete()
        return HttpResponseRedirect('/')


def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        mi = StudentRegistration(request.POST, instance=pi)
        if mi.is_valid():
            mi.save() 
        #    this can be cleaned data aswell
        else:
            pi = User.objects.get(pk=id)
            mi = StudentRegistration(instance=pi)
    return render(request, 'CREATEAPP/update.html',{'form':mi})