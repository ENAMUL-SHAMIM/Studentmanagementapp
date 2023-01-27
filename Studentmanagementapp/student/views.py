from django.shortcuts import render,redirect
from student.forms import StudentForm
from student.models import Student

# Create your views here.
def create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/all-student")
    else:
        form = StudentForm()
    return render(request,'create.html', {'form': form})

def Show(request):
    Students = Student.objects.all()
    return render(request, 'Show.html', {'Students': Students})

def Delete(request,id):
    Student = Student.objects.get(id=id)
    Student.Delete()
    return redirect("/All-student")

def Edit(request, id):
    Student = Student.objects.get(id = id)
    return render(request, 'Edit.html', {"student": Student})

def Update(request, id):
    Student = Student.objects.get(id = id)
    form = StudentForm(request.Post, instance = Student)

    print(form.is_valid())

    if form.is_valid():
        Student.Save()
        return redirect("/All-student")

    return render(request, 'Edit.html', {"student": Student})