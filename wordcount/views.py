from django.http import HttpResponse
from django.shortcuts import render
import operator

sorted_list = []
data = ""

def homepage(request):
    return render(request , 'home.html' , {'name':'tushar here'})
#    return HttpResponse("<h1>this is homepage</h1>")

def contact(request):
    return HttpResponse("<h1>CONTACT US</h1><br>this is our conatct page.")

def count(request):
    global data
    data = request.GET['fulltextarea']
    #print(data)

    word_list = data.split()
    #print(word_list)
    list_len = len(word_list)

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # increase value by 1
            word_dictionary[word] += 1
        else:
            #add to the word_dictionary and set value by 1
            word_dictionary[word] = 1

        global sorted_list
        sorted_list = sorted(word_dictionary.items() , key=operator.itemgetter(1), reverse=True)

    return render(request , 'count.html' , {'fulltext':data , 'words':list_len, 'word_dictionary':sorted_list})

def about(request):
    return render(request , 'about.html' )
