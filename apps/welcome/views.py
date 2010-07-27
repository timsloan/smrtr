from django.db import models
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
# Smrtr
from welcome.forms import *
    
# Get basic profile information from the user once registered    
def profile(request):

    user = request.user
    profile = user.get_profile()

    if request.method == 'POST': # If the form has been submitted...
        uform = UserForm(request.POST, instance=user) # A form bound to the POST data
        pform = ProfileForm(request.POST, instance=profile) # A form bound to the POST data
        if pform.is_valid() and uform.is_valid(): # All validation rules pass
            user = uform.save()
            user.save()
            profile = pform.save()
            profile.save()
            request.user.message_set.create(
                message=_(u"Welcome to smrtr! Get started by choosing a challenge below and clicking Start..."))
            return HttpResponseRedirect( reverse('home') ) #reverse('welcome-2') )
    else:
        uform = UserForm(instance=user)
        pform = ProfileForm(instance=profile)
        
    context = {
        'profile': profile,
        'uform': uform,
        'pform': pform,
    }

    return render_to_response('welcome_profile.html', context, context_instance=RequestContext(request))


def networks(request):
    return False
