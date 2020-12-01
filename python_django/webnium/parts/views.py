from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from parts.models import Parts
from .forms import PartsForm
import datetime


# Create your views here.
def list(request):
    parts_list = Parts.objects.all()
    parts_paginator = Paginator(parts_list, 10)

    page = request.GET.get('page', 1)

    try:
        parts = parts_paginator.page(page)
    except PageNotAnInteger:
        parts = parts_paginator.page(1)
    except EmptyPage:
        parts = parts_paginator.page(1)

    params = {
        'parts': parts
    }
    return render(request, 'parts/list.html', params)


def new_parts(request):
    javascript_list = {
        "parts/parts.js"
    }
    css_list = {
        "parts/parts.css"
    }
    initial_dict = dict(
        parts_name="",
        description="",
    )
    parts_form = PartsForm(request.GET or None, initial=initial_dict)

    params = {
        'message': "edit",
        'javascript_list':  javascript_list,
        'parts_form': parts_form,
        'css_list':css_list
    }
    return render(request, 'parts/new_parts.html', params)


def confirm(request, *args, **kwargs):
    parts_name = request.POST['parts_name']
    description = request.POST['description']
    parts_id = request.POST['parts_id']
    if parts_id is None or parts_id == "":
        parts_object = Parts(
            parts_name=parts_name,
            description=description,
            pub_date=datetime.datetime.now()
        )
        parts_object.save()
        result = "created"
    else:
        parts_object = Parts.objects.all().filter(id=parts_id).first()
        parts_object.parts_name = parts_name
        parts_object.description = description
        parts_object.save()
        result = "updated"

    context = {
        'parts_name': parts_name,
        'description': description,
        'result': result
    }
    return render(request, 'parts/confirm.html', context)
