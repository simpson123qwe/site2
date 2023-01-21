from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import ReviewForm 
def home(request):
    print(request.method)
    if request.method=="GET":
        lname1=request.GET.get("lname")
        fname=request.GET.get("fname")
        pol=request.GET.get("pol")
        vozrast=request.GET.get("vozrast")
        pochta=request.GET.get("pochta")

        print(lname1)
        # return HttpResponse("Приветствую", status=404)
        form=ReviewForm()
        return render(request, "home.html",{"name":lname1,"name2":fname,"pol":pol,"vozrast":vozrast,"pochta":pochta,"form":form})
    # elif request.method=="POST":
    #     form=ReviewForm(request.POST)
    #     if form.is_valid():


def base(request):
    return render(request, "base.html")













