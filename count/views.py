from django.shortcuts import render
from django.http import HttpResponse
import operator

def index(request):
    return render(request,'index.html')

def output(request):
    data = request.GET['textarea']
    data_list = data.split()
    w_len =len(data_list)

    word_list={}

    for word in data_list:
        if word in word_list:
                word_list[word] +=1
        else:
            word_list[word]=1
            
    sorted_list = sorted(word_list.items(), key = operator.itemgetter(1),reverse=True)
    return render(request,'output.html',{'a':data, 'b':w_len, 'sorted_list':sorted_list})

# Create your views here.
