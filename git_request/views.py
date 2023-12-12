from django.shortcuts import render
import requests
from .forms import VenueForm
import json
#from .forms import Data_git
import os

def index(request):
    # response = request.get('')
    submitted = False
    form = VenueForm
    
    response = []
    if request.method == "POST":
        form = VenueForm(request.POST)
        response = requests.get('https://api.github.com/users/{}/repos'.format(form.data['git_account'])).json()
        list_json = []
        
        file = open('sample.json')
        file_content = json.load(file)
        file.close()

        for i in response:
            dictionary = {'name': i['name'], 'html_url': i['html_url'], 'description':i['description'], 'language':i['language'] } 
            file_content.append(dictionary)

        json_object = json.dumps(file_content,indent=4)
        file = open('sample.json', 'w')
        file.write(json_object)
        file.close()

        return render(request, 'index.html', {'form': form, 'response':response})
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'index.html', {'form': form})

    # return render(request, 'index.html', {'response':response})

