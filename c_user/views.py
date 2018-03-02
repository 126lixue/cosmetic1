from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from hashlib import sha1
from c_user.models import User,Address
from c_goods.models import GoodInfo
from c_user import user_decorator


def login(request):
    uname=request.COOKIES.get('uname','')
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,'pwd':pwd,'error':0}
    try:
        url=request.META['HTTP_REFERER']
        if '/user/register' in url:raise Exception()
    except:url='/'
    response=render(request,'c_user/login.html',context)
    response.set_cookie('url',url)
    return response
def register(request):
    return render(request,'c_user/register.html')


def login_handle(request):
    post=request.POST#接受表单请求
    uname=post.get('user_name')
    pwd=post.get('pwd','')
    print(uname)
    remember=post.get('remember','0')
    s=sha1()
    s.update(pwd.encode('utf-8')) #先编码
    upwd=s.hexdigest()
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()

    if user:
        url=request.COOKIES.get('url','/')
        red=HttpResponseRedirect(url)
        if remember=='1':
            red.set_cookie('uname',uname.encode('utf-8')) #存在浏览器里
            red.set_cookie('upwd',pwd)
        else:
            red.set_cookie('uname','',max_age=-1)  #没有帮忙保存，瞬间消失
            red.set_cookie('upwd','',max_age=-1)
        request.session['username']=uname #默认有个期限，有效期限半个小时
        request.session['uid']=user.id   #存在应用里
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request,'c_user/login.html',context)
def register_handle(request):
    post = request.POST  # 接收用户输入
    uname = post.get('username','')
    pwd = post.get('pwd','')
    cpwd = post.get('cpwd','')
    uemail = post.get('email','')
    uphone = post.get('uphone', '')
    # allow = post.get('allow')
    # 判断密码是否相等
    if pwd != cpwd:
        return redirect('/user/register')
    s1 = sha1()    # 密码加密
    # 使用sha1加密
    # sha1加密前，要先编码为比特
    s1.update(pwd.encode('utf-8'))
    pwd = s1.hexdigest()
    user = User()# 存入数据库
    user.uname = uname
    user.upwd = pwd
    user.uemil = uemail
    user.uphone=uphone
    user.save()
    # print(user.uname)
    return redirect('/user/login')
def logout(request):
    request.session.flush()#清空所有session中信息
    return redirect('/')
def register_exist(request):
    uname=request.GET.get('un')

    count=User.objects.filter(uname=uname). count()
    return JsonResponse({'count':count})

@user_decorator.login
def user_center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list = []

    if goodids!='':
        goodidl=goodids.split(',')
        for i in goodidl:
            goods_list.append(GoodInfo.objects.filter(pk=i).first())

    myurl=request.path.split('/')[-1]
    print(myurl)
    res='c_account.html' if myurl=='c_account' else 'c_index.html'
    return render(request,'c_user/'+res,locals())




@user_decorator.login
def shdz(request):
    adds = Address.objects.filter(uid=request.session.get('uid',''),scbz=0)
    return render(request,'c_user/c_address.html',locals())

@user_decorator.login
def userupdate(request):
    post = request.POST  # 接收用户输入
    uid = request.session.get('uid', '')
    user = User.objects.filter(id=uid).first()
    user.uname=post.get('un','')
    user.uemil=post.get('uemil','')
    user.usex = post.get('usex', '')
    uname = post.get('un', '')
    uphone= post.get('uphone', '')
    uemil = post.get('uemil', '')
    user.save()
    request.session['username'] = user.uname
    return redirect('/')

@user_decorator.login
def add_save(request):
    post = request.POST  # 接收用户输入
    aid=post.get('aid')
    print(aid)
    if aid:
        Address.objects.filter(id=aid).update(reciver=post.get('reciver'),
            sheng = post.get('sheng'),shi = post.get('shi'),qu= post.get('qu'),
                    detialaddr=post.get('detialaddr'),rphone = post.get('rphone') ,yzbm = post.get('yzbm'))
    else:
        Address.objects.create(reciver=post.get('reciver'),uid = request.session['uid'],
                 sheng=post.get('sheng'), shi=post.get('shi'), qu=post.get('qu'),
                  detialaddr=post.get('detialaddr'), rphone=post.get('rphone'),
                    yzbm=post.get('yzbm'))
    return redirect('/user/c_address')
@user_decorator.login
def mrdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(mrdz=1).update(mrdz=0)
    # Address.objects.all().update(mrdz=0)
    Address.objects.filter(id=dzid).update(mrdz=1)
    return redirect('/user/c_address')

@user_decorator.login
def scdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(id=dzid).update(scbz=1)
    return redirect('/user/c_address')


@user_decorator.login
def bjdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid)
    adds = Address.objects.filter(uid=request.session.get('uid', ''), scbz=0)
    return render(request, 'c_user/c_address.html', locals())






