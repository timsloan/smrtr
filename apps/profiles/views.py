from django.db import models
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Smrtr
from profiles.forms import *
# External
from wall.forms import WallItemForm

def profile(request, user_id):

    puser = get_object_or_404(User, pk=user_id)
    profile = puser.get_profile()

    try:
        wall = profile.wall
        wallitems = profile.wall.wallitem_set.select_related()
    except:
        wall = None
        wallitems = None

    context = {
        'puser': puser, 
        'profile': profile,
        "wall": wall,
        "wallitems": wallitems,
        "wallform": WallItemForm()
    }

    return render_to_response('profile.html', context, context_instance=RequestContext(request))
    
    
def edit_profile(request):

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
            return HttpResponseRedirect( reverse('user-profile',kwargs={'user_id':user.id} ) )
    else:
        uform = UserForm(instance=user)
        pform = ProfileForm(instance=profile)
        
    context = {
        'profile': profile,
        'uform': uform,
        'pform': pform,
    }

    return render_to_response('profile_edit.html', context, context_instance=RequestContext(request))

