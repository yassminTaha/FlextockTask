from django.shortcuts import render
from django.http import HttpResponse
import json
from currency.services import get_rate


def index(request):
    fromCurrency = request.GET.get('from', '')
    toCurrency = request.GET.get('to', '')
    date = request.GET.get('date', '')
    rateResponseVM = get_rate(fromCurrency,toCurrency,date)
    return HttpResponse(json.dumps(rateResponseVM), content_type = "application/json")
