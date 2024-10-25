from django.shortcuts import render,redirect
from modelapp.models import caballo
from modelapp.form import formcaballo

def index(request):
    return render(request,'index.html')

def caballos(request):
    form=caballo.objects.all()
    data={'caballos':form}
    return render(request,'caballos.html',data)

def agregarcaballos(request):
    form = formcaballo(request.POST or None)  
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/caballosos')

    data = {'form': form}
    return render(request, 'agregarcaballo.html', data)
    
def eliminar(request,id):
    form=caballo.objects.get(id=id)
    form.delete()
    return caballos(request)

def actualizar(request,id):
    caball=caballo.objects.get(id=id)
    form=formcaballo(instance=caball)
    if request.method=='POST':
        form=formcaballo(request.POST,instance=caball)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render (request,'agregarcaballo.html',data)
# Create your views here.
