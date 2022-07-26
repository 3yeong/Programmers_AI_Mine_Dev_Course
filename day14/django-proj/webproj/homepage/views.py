from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.

def index(request):
    # return HttpResponse("<h1>Hello World!</h1>")
    nums = [1,2,3,4,5]
    return render(request, 'index.html', {"my_list" : nums})

def coffee_view(request):
    coffee_all = Coffee.objects.all() #.get(), .filter(), ...
    # 만약 request가 POST라면:
        # POST 바탕으로 Form을 완성하고
        #Form이 유효하면 -> 저장!
    if request.method == "POST":
        form = CoffeeForm(request.POST) #파일 상에서 post로 보내준 내용을 바탕으로 form을 완성
        if form.is_valid(): #채워진 form이 유효한지 체크
            form.save() #이 Form 내용을 Model에 저장

    form = CoffeeForm() # Form의 객체를 만들어 준다.
    return render(request, 'coffee.html',{"coffee_list":coffee_all, "coffee_form":form})