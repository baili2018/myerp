from django import forms
from django.db import models
from erp.models import *

# class cost_form(forms.ModelForm):
#     class Meta:
#         model = cost #绑定数据模型
#         # fields = ['c_id', 'create_date', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement', 'S_date']
#         fields = ['c_id', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement']

# class cost_form(forms.Form):
#     F_c_id = forms.IntegerField(label='序号')
#     F_create_date = forms.DateTimeField(label='创建时间')
#     F_c1 = forms.CharField(label='一级科目')
#     F_c2 = forms.CharField(label='二级科目')
#     F_c3 = forms.CharField(label='三级科目')
#     F_summary = forms.CharField(label='摘要', widget=forms.Textarea(attrs={'class': '111'}))
#     F_amount = forms.DecimalField(label='发生金额', max_digits=10, decimal_places=2)
#     F_borl = forms.ChoiceField(label='借贷方向', choices=(('借', '借'), ('贷', '贷')))
#     F_balance = forms.DecimalField(label='当前余额', max_digits=10, decimal_places=2)
#     F_account_number = forms.CharField(label='账号', widget=forms.TextInput(attrs={'class': 'input-group'}))
#     F_manager = forms.CharField(label='经办人')
#     F_settlement = forms.ChoiceField(label='是否结算', choices=(('是', '是'), ('否', '否')))
#     F_s_date = forms.DateTimeField(label='结算时间')

class cost_form(forms.ModelForm):
    create_date = forms.CharField(label='创建时间', widget=forms.DateTimeInput())
    summary = forms.CharField(required=True, widget=forms.Textarea(attrs=\
            {'class': 'form-control', 'rows': '3', 'style': 'width:680px', 'placeholder': '摘要'}))#特殊设置
    C1 = forms.CharField(label='一级科目', widget=forms.Select())
    C2 = forms.CharField(label='二级科目', widget=forms.Select())
    C3 = forms.CharField(label='三级科目', widget=forms.Select())
    def __init__(self,*args,**kwargs):    #执行父类的构造方法
        super(cost_form, self).__init__(*args, **kwargs)
        self.fields['C1'].widget.choices = km_c1.objects.all().values_list('KC1_name', 'KC1_name')
        self.fields['C2'].widget.choices = km_c2.objects.all().values_list('KC2_name', 'KC2_name')
        self.fields['C3'].widget.choices = km_c3.objects.all().values_list('KC3_name', 'KC3_name')
        #每次都会去数据库中获取这个列表
    Amount = forms.FloatField(label='发生金额', widget=forms.TextInput(attrs=\
            {'class': 'form-control', 'id': 'exampleInputAmount', 'placeholder': '发生金额', 'style': 'width:144px'}))
    BorL = forms.CharField(label='借货方向', widget=forms.Select(choices=(('借', '借'), ('贷', '贷'))))
    Account_number = forms.CharField(label='结算账号', max_length=50)
    Manage = forms.CharField(label='经办人', max_length=50)
    Settlement = forms.CharField(label='是否结算', widget=forms.Select(choices=(('是', '是'), ('否', '否'))))
    S_date = forms.CharField(label='结算时间')
    class Meta:
        model = cost #绑定数据模型
        # fields = ['c_id', 'create_date', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement', 'S_date']
        fields = ['c_id', 'create_date', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement', 'S_date']
