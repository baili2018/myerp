from django.shortcuts import render
from django import forms
from django.http import *
from erp.models import *
from erp.forms import *
from erp import trackingmoreclass
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
# Create your views here.


def cost_list(request):
    costlist = cost.objects.all()
    paginator = Paginator(costlist, 25)
    try:
        page = int(request.GET.get('page', 1))
        clist = paginator.page(page)
    except PageNotAnInteger:
        clist = paginator.page(paginator.num_pages)
    return render(request, 'cost.html', locals())

def cost_add(request):
    if request.method == 'POST':
        form_cost = cost_form(request.POST)
        if form_cost.is_valid():
            form_cost.save()
            return HttpResponse('添加成功')
    else:
        form_cost = cost_form()
    return render(request, 'cost_add.html', locals())

# def V_cost_add(request):
#     if request.method == 'POST':
#         form_cost = cost_form(request.POST)
#         if form_cost.is_valid():
#             cost.objects.create(
#                 F_c_id = form_cost.cleaned_data['F_c_id'],
#                 F_create_date = form_cost.cleaned_data['F_create_date'],
#                 # F_c1 = form_cost.CharField(label='一级科目')
#                 # F_c2 = forms.CharField(label='二级科目')
#                 # F_c3 = forms.CharField(label='三级科目')
#                 # F_summary = forms.CharField(label='摘要')
#                 # F_amount = forms.DecimalField(label='发生金额')
#                 # F_borl = forms.CharField(label='借贷方向')
#                 # F_balance = forms.DecimalField(label='当前余额')
#                 # F_account_number = forms.CharField(label='账号')
#                 # F_manager = forms.CharField(label='经办人')
#                 # F_settlement = forms.CharField(label='是否结算')
#                 # F_s_date = forms.DateTimeField(label='结算时间')
#             )
#             form_cost.save()
#             return HttpResponse('添加成功')
#     else:
#         form_cost = cost_form()
#     return render(request, 'cost_add.html', locals())


def index(request):
    return render(request, 'index.html',)

def index3(request):
    return render(request, 'index_v3.html',)

def tem(request):
    if request.method == 'POST':
        q = request.POST.get('sku')
    return render(request, 'tem.html', locals())