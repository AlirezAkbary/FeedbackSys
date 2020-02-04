from django.shortcuts import render
from .models import Professor
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def professor_view(request, id):
    obj = Professor.objects.get(ProfID=id)
    context = {
        "object" : obj
    }
    return render(request, "professor/New_HomeProfPage.html", context)


# Create your views here.

# Create your views here.
