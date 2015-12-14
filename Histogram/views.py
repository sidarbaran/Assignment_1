from django.shortcuts import HttpResponse
import os

def count(request,filename):
    file=open("%s/templates/%s"%(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),filename))
    #i placed the file in templates.Moreover, i take BASE_DIR from settings thanks to importing os for adrresing to go.
    for_count=dict()
    #create dictinory to help counting
    for word in file.read().split(" "):
        if word not in for_count:
            for_count[word] =1
        else:
            for_count[word] +=1
    #for loop is for how many different words and how many times it exist in filename
    str = "Name: %s <br> Words: <br>" % filename
    for s,b in for_count.items():
        str += "%s: %d <br>"%(s,b)
    #i use <br> for make single line break
    #i export key and value as s,b to show words, and how many times they occur
    file.close()
    return HttpResponse(str)







