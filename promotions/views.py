from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from promotions.models import Promo


def index(request):
    promotions_list = Promo.objects.order_by('-posting_date')[:5]
    template = loader.get_template('promotions/index.html')
    context = {'promotions_list': promotions_list}
    return render(request, 'promotions/index.html', context)
    

def detail(request, promo_id):
    promo = get_object_or_404(Promo, pk=promo_id)
    return render(request, 'promotions/detail.html', {'promo': promo})

