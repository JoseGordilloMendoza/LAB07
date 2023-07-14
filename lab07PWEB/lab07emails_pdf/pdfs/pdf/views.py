from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from .utils import render_to_pdf
