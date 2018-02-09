from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Doctor, Branch, Arrange
from django.views import generic

#from .forms import ScheduleForm

class DetailView(generic.DetailView):
    model = Arrange
    template_name = 'schedule/detail.html'

class IndexView(generic.ListView):
    model = Branch
    template_name = 'schedule/index.html'
    

#def index(request):
#    return HttpResponse("Hello. You're at schedule index.")

def bybranch(request, b_id):
    arrangeList = get_list_or_404(Arrange, branch_id=b_id)
    branchRow = get_object_or_404(Branch, id=b_id)
    context = {
        'arrangeList': arrangeList,
        'branchRow': branchRow,
    }
    return render(request, 'schedule/bybranch.html', context)


class ScheduleUpdate(generic.edit.UpdateView):
    model = Arrange
    fields = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    template_name_suffix = '_update_form'






