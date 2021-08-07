from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import re
from .models import Ebook,cartitems, searchitem
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def storeview(request):
    ebook={'ebook':Ebook.objects.all()}
    return render(request,'store\index.html',ebook)


def cartview(request):
    cartitem={'cartitem':cartitems.objects.all()}
    return render(request,'store\cart.html',cartitem)

@ csrf_exempt
def add_cart_items(request):
    bookid=request.POST["bookid"] 
    title1=Ebook.objects.get(pk=bookid).title
    price1=Ebook.objects.get(pk=bookid).rating
    des1=Ebook.objects.get(pk=bookid).des
    cartitems.objects.create(title=title1,price=price1,des=des1)
    return HttpResponseRedirect('/store')

@ csrf_exempt
def searching(request):
    searchid=request.POST["search"]
    a=re.compile(f'({searchid})+')
    ebook=Ebook.objects.get_queryset()
    n=Ebook.objects.count()
    i=1
    searchitem.objects.all().delete()
    li1=[]
    for e in ebook:
        li1.append(e.id)

    for i in range(n):
        id2=li1[i]
        e=Ebook.objects.get(id=id2)
        l=a.findall(str(e.title))
        if len(l)!=0:
            title1=Ebook.objects.get(title=e.title)
            id1=title1.id
            price1=Ebook.objects.get(id=id1).rating
            des1=Ebook.objects.get(id=id1).des
            video=Ebook.objects.get(id=id1).video
            searchitem.objects.create(title=title1,rating=price1,des=des1,video=video)
    return HttpResponseRedirect('/store/search-item-view')
    

def searchview(request):
    searchitem1={'searchitem1':searchitem.objects.all()}
    return render(request,'store\search.html',searchitem1)