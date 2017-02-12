from django.shortcuts import render, get_object_or_404

from myapp.forms import MyForm
from myapp.models import MyJSONModel


def index(request):
    form = MyForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form=form.save()
        return(json_detail(request,pk=new_form.id))
    return render(request, "myapp/index.html", locals())

def results(request):
    jsons = MyJSONModel.objects.all()
    return render(request, 'myapp/results.html', {'jsons':jsons})

def json_detail(request, pk):
    json = get_object_or_404(MyJSONModel, pk=pk)
    return render(request, 'myapp/json_detail.html', {'json': json})