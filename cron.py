from django.core.management import setup_environ
import settings
setup_environ(settings)
# Spenglr
from questions.utils import *
from education.utils import *
from challenge.utils import *
from profiles.utils import *
from network.utils import *

def cron():
    print "Running smrtr cron.py..."
    batch_question_update_sq()
    
    batch_module_update_sq()
    batch_concept_update_sq()    

    batch_usermodule_update_sq()
    batch_userconcept_update_sq()
    batch_userconcept_update_focus()

    batch_user_update_sq()
    batch_network_update_sq()

    batch_generate_user_challenges()
    print "Done."
cron()
