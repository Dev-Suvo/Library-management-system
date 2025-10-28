from django.shortcuts import render , redirect
from .models import *
# Create your views here.


def create(request):
    if request.method == "POST":
        data = request.POST
        B_name = data.get('b_name')
        B_des = data.get('b_des')
        B_image = request.FILES.get('b_image')

        Lbook.objects.create(
            b_name = B_name,
            b_des = B_des,
            b_image = B_image,
        )
        return redirect('/')
    return render(request, 'home.html')


def showtable(request):

    queryset = Lbook.objects.all()

    if request.GET.get('si'):
        queryset = queryset.filter(b_name__icontains = request.GET.get('si'))

    context = {'books' : queryset}
    return render(request,'table.html', context)


def update(request, id):
    queryset = Lbook.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        B_name = data.get('b_name')
        B_des = data.get('b_des')
        B_image = request.FILES.get('b_image')

        queryset.b_name = B_name
        queryset.b_des = B_des
        
        if B_image:
            queryset.b_image = B_image

        queryset.save()
        return redirect('/table/')


    context = {'book': queryset}

    return render(request,'update.html', context)

     

def delete(request, id):
    queryset = Lbook.objects.get(id = id)
    queryset.delete()
    return redirect('/table/')

