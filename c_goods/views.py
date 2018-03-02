from django.shortcuts import render
from c_goods.models import GoodInfo,TypeInfo
from c_cart.models import Cart
from django.core.paginator import Paginator
from django.core import serializers
from django.db.models import Q
import json

def index(request):
    request.session['typeinfos']=typeinfos()
    # request.session['typeinfos'] =json.loads(serializers.serialize('json',TypeInfo.objects.filter(level__gt=1).all()))
    # request.session['typeinfos1'] =json.loads(serializers.serialize('json',TypeInfo.objects.filter(level=1).all()))
    context={'guest_cart':1,'title':'首页'}
    #获取最新最火的4个商品
    hot=GoodInfo.objects.all().order_by('-gclick')[0:8]
    context.setdefault('hot',hot)
    #获取所有类别
    typelist=TypeInfo.objects.all()
    for i in range(len(typelist)):  #enumerate()
        typeinfo=typelist[i]
        # goods1=GoodInfo.objects.filter(gtype=typeinfo.id).order_by('-id')
        goods1=typeinfo.goodinfo_set.order_by('-id')[0:4]
        goods2=typeinfo.goodinfo_set.order_by('gclick')[0:4]
        context.setdefault('type'+str(i),goods1)
        context.setdefault('type' + str(i)+'-', goods2)
    return render(request, "index.html", context)

def typelist(request,tid,sid,pindex):
    #pk id是传进的分类拿到
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news=typeinfo.goodinfo_set.order_by('-id')[0:2]
    ordby='-id'  if sid=='1' else '-gprice' if sid=='2' else '-gclick'
    ssnr = request.GET.get('ssnr', '').strip()
    if ssnr:
        typei= TypeInfo.objects.filter(ttitle__contains=ssnr).first()
        typepk=typeinfo.pk if typei else 0
        good_list=GoodInfo.objects.filter(Q(gtitle__contains=ssnr)|Q(gtype=typepk))
    else:
        good_list =typeinfo.goodinfo_set.order_by(ordby)
    good_list=json.loads(serializers.serialize('json',good_list))
    paginator=Paginator(good_list,3)
    page=paginator.page(int(pindex))
    context={'title':'商品列表','guest_cart':1,'page':page,
             'paginator':paginator,'typeinfo':typeinfo,'sort'
             :sid,'news':news,'ssnr':ssnr}
    return render(request,'c_goods/list.html',context)


def typeinfos(tjson=[],ts=None):
    for i in tjson:
        i['sub']=[j for j in ts if j['fields']['pid']==i['pk']]
        if i['sub']:typeinfos(i['sub'],ts)
    if len(tjson)==0:
        ts=json.loads(serializers.serialize('json',TypeInfo.objects.all()))
        tjson=[i for i in ts if i['fields']['pid']==0]
        typeinfos(tjson,ts)
    return tjson

def detail(request,id):
    goods=GoodInfo.objects.get(pk=int(id))
    goods.gclick+=1
    goods.save()
    cart_count=Cart.objects.filter(user_id=request.session.get('uid',0)).count()
    news=goods.gtype.goodinfo_set.order_by('-id')[0:2]
    context={'title':goods.gtype.ttitle,'goods':goods,'cart_count':
             cart_count,'news':news,'guest_cart':1,
             'typeinfo':goods.gtype}
    response=render(request,'c_goods/detailed.html',context)
    goodids=request.COOKIES.get('goodids','')
    if goodids:
        goodids1=goodids.split(',')
        if goodids1.count(id)>=1:goodids1.remove(id)
        goodids1.insert(0,id)
        if len(goodids1)>=6:
            del goodids1[5]
        goodids=','.join(goodids1)
    else:goodids=id
    response.set_cookie('goodids',goodids)
    return response










