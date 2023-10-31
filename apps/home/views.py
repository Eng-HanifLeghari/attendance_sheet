# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import ZoomParticipant


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def zoom_meeting_list(request):
    if request.method == "GET":
        meetings = ZoomParticipant.objects.all()
        context = {
            "meetings": meetings,
        }

        return render(request, "home/zoom.html", context)

    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_records")  # Get a list of selected student IDs
        for student_id in selected_ids:
            attendance_status = request.POST.get(f"attendance_status_{student_id}")
            comment = request.POST.get(f"comment_{student_id}")

            # Update the model for each student
            ZoomParticipant.objects.filter(id=student_id).update(
                attendance_status=attendance_status,
                comment=comment
            )

        # Fetch Zoom meeting data from the database
        meetings = ZoomParticipant.objects.all()

        context = {
            "meetings": meetings,
        }

        return render(request, "home/zoom.html", context)