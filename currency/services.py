import requests
import datetime
from currency.viewModels import rateResponseViewModel 
from currency.models import CurrencyRate

def get_rate(fromCurrency,toCurrency,date):
   
    validation_response = validate_request(fromCurrency,toCurrency,date)
    if validation_response is not None:
       return validation_response
    if fromCurrency == toCurrency :
        return rateResponseViewModel(True,fromCurrency,toCurrency,date,1,"").json()
    
    if date == '':
        url = 'https://api.frankfurter.app/latest?from=' + fromCurrency + '&to=' + toCurrency
    else:
        q = CurrencyRate.objects.filter(from_currency=fromCurrency,to_currency=toCurrency,date=date)
        if q.count() > 0:
            return rateResponseViewModel(True,fromCurrency,toCurrency,date,q.first().rate,"").json()
        else:
            url = 'https://api.frankfurter.app/'+date+'..'+date+'?from=' + fromCurrency + '&to=' + toCurrency

    r=requests.get(url)
    if r.status_code == 200 :
        response = r.json()
        if date == '':
            rate = response["rates"][toCurrency]
            date = response["date"]
        else:
            rate = response["rates"][date][toCurrency]
        responseVM = rateResponseViewModel(True,fromCurrency,toCurrency,date,rate,"")
        cr = CurrencyRate(from_currency=fromCurrency,to_currency=toCurrency,date=date,rate=rate)
        cr.save()
        return responseVM.json()
    if r.status_code == 404:
        return rateResponseViewModel(False,fromCurrency,toCurrency,date,0,"Please make sure From, To currency are correct").json()
    
    responseVM = rateResponseViewModel(False,fromCurrency,toCurrency,date,0,"Something went wrong please try again later")
    return responseVM.json()

def validate_request(fromCurrency,toCurrency,date):
    if fromCurrency == '':
       return rateResponseViewModel(False,fromCurrency,toCurrency,date,0,"Invalid from currency").json()
    if toCurrency == '':
       return rateResponseViewModel(False,fromCurrency,toCurrency,date,0,"Invalid to currency").json()
    if date != '':
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return rateResponseViewModel(False,fromCurrency,toCurrency,date,0,"Incorrect data format, should be YYYY-MM-DD").json()
    return None