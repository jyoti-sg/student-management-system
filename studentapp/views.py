from django.shortcuts import render,redirect
from .models import studentmanagement
# Create your views here.
def recordview(request):
    sturecord=studentmanagement.objects.all()
    context={"studentrecord":sturecord}
    return render(request,"home.html",context)
def formview(request):
    return render(request,"form.html")
def adrecord(request):
    rollrecord=request.POST['rollno']
    nrecord=request.POST['name']
    crecord=request.POST['contact']
    frecord=request.POST['fee']
    studentmanagement(rollno=rollrecord, name=nrecord,contact=crecord,fees=frecord).save()
    return redirect('homepage')
def deleterecord(request,deleteid):
    studentmanagement.objects.filter(id=deleteid).delete()
    return redirect('homepage')
def editform(request,editid):

    store=studentmanagement.objects.filter(id=editid)[0]
    context={'editid':editid,'store':store}
    return render(request,"editing.html",context)
def editview(request,editid):
    usfee=request.POST['editfee']
    uscontect=request.POST['editcont']
    store=studentmanagement.objects.filter(id=editid)[0]
    store.fees=usfee
    store.contact=uscontect
    store.save()
    return redirect('homepage')
def backhome(request):
    return redirect('homepage')
def backhomedit(request,editid):
    return redirect('homepage')
def formview2(request,editid):
    return render(request,"form.html")
