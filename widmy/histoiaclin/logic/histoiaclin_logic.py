from ..models import HistoiaClin

def get_histoiaclins():
    histoiaclins = HistoiaClin.objects.all()
    return histoiaclins

