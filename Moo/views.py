from django.shortcuts import render
from django.http import HttpResponseRedirect
from Moo.forms import Cow_talk_input
from Moo.models import Cow_talk

import subprocess

def index (request):
    if request.method == 'POST':
        form = Cow_talk_input(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_text = Cow_talk.objects.create(
                text = form.get('text')
            )
            the_cow = subprocess.run(['cowsay', new_text.text], capture_output=True)
            output = the_cow.stdout.decode()
            form = Cow_talk_input()
    else:
        form = Cow_talk_input()
        output = None
    return render(request, 'index.html', {'form':form, 'the_cow': output})


def recent_inputs_view(request):
    recent_inputs = Cow_talk.objects.order_by('-id')[0:10]
    return render(request, 'recents_view.html', {'inputs':recent_inputs})