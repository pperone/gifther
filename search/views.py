from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.mail import EmailMessage
from django.http import JsonResponse

from rest_framework import viewsets

from .models import Product
from .forms import SearchForm
from .serializers import ProductSerializer


def get_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            woman = form.cleaned_data['woman']
            occasion = form.cleaned_data['occasion']
            results = Product.objects.filter(Q(woman__icontains=woman) & Q(occasion__icontains=occasion))
            if form.cleaned_data['price']:
                if form.cleaned_data['price'] == '10':
                    priced = results.filter(price__lte=10)
                elif form.cleaned_data['price'] == '50':
                    priced = results.filter(price__lte=50)
                elif form.cleaned_data['price'] == '100':
                    priced = results.filter(price__lte=100)
                else:
                    priced = results
            else:
                priced=results

            ordered = priced.order_by('-votes')

            return render(request, "search.html", {'results': ordered, 'woman': woman, 'occasion': occasion})

    else:
        form = SearchForm()

    return render(request, 'search-form.html', {'form': form})


def do_vote(request):
    vote = request.GET.get('vote')
    pk = request.GET.get('pk')
    product = Product.objects.get(pk=pk)

    if vote == 'up':
        product.votes += 1
        product.save()
    elif vote == 'down':
        product.votes -= 1
        product.save()

    data = {
        'votes': product.votes
    }

    return JsonResponse(data)


class ProductView(viewsets.ModelViewSet):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
