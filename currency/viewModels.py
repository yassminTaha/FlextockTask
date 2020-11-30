class rateResponseViewModel:
    status = True
    fromcurrency = ""
    tocurrency = ""
    date = ""
    rate = 1
    error = ""

    def __init__(self, status, fromcurrency,tocurrency,date,rate,error):
        self.status = status
        self.fromcurrency = fromcurrency
        self.tocurrency = tocurrency
        self.date = date
        self.rate = rate
        self.error = error
    
    def json(self):
        return {
            'status': self.status,
            'fromcurrency': self.fromcurrency,
            'tocurrency': self.tocurrency,
            'date' : self.date,
            'rate':self.rate,
            'error':self.error
        }