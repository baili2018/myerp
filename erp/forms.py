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
    summary = forms.CharField(label='摘要', required=True, widget=forms.Textarea(attrs={'class': '111'}))#特殊设置
    C1 = forms.Select()

    class Meta:

        model = cost #绑定数据模型
        # fields = ['c_id', 'create_date', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement', 'S_date']
        fields = ['c_id', 'C1', 'C2', 'C3', 'summary', 'Amount', 'BorL', 'Balance', 'Manager', 'Settlement', 'S_date']
