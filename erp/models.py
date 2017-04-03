from django.db import models
import datetime
import time

# Create your models here.



class cost(models.Model):
    c_id = models.AutoField('序号', auto_created=True, primary_key=True)
    create_date = models.DateTimeField('创建日期', auto_now_add=True)
    C1 = models.CharField('一级科目', max_length=16)
    C2 = models.CharField('二级科目', max_length=16)
    C3 = models.CharField('三级科目', max_length=16)
    summary = models.CharField('摘要', max_length=500)
    Amount = models.DecimalField('发生金额', max_digits=10, decimal_places=2, default=0.00)
    BorL = models.CharField('借贷方向', max_length=2, choices=(('借', '借'), ('贷', '贷')))
    Balance = models.DecimalField('当前余额', max_digits=10, decimal_places=2, default=0.00)
    Account_number = models.CharField('结算账号', max_length=40)
    Manager = models.CharField('经办人', max_length=26)
    Settlement = models.CharField('是否结算', max_length=2, choices=(('是', '是'), ('否', '否')))
    S_date = models.DateTimeField('结算时间', null=True, blank=True)

    def __unicode__(self):
        return self.name


class km_c1(models.Model):
    KC1_id = models.AutoField(primary_key=True, auto_created=True)
    KC1_name = models.CharField('科目名称', max_length=200, unique=True)

class km_c2(models.Model):
    KC2_id = models.AutoField(primary_key=True, auto_created=True)
    KC2_name = models.CharField('科目名称', max_length=200,unique=True)
    id_kc1_kc2 = models.ForeignKey(km_c1)

class km_c3(models.Model):
    KC3_id = models.AutoField(primary_key=True, auto_created=True)
    KC3_name = models.CharField('科目名称', max_length=200, unique=True, blank=True)
    id_kc2_kc3 = models.ForeignKey(km_c2)

class Cate1(models.Model):
    C1_id = models.AutoField("一级分类ID", primary_key=True, null=False, help_text="自动生成，主键，不能为空值")
    C1_name = models.CharField("分类名称", max_length=50, unique=True)
    C1_shorthand = models.CharField("名称简写", max_length=2)
    class Meta:
        verbose_name = "一级分类"
    def __str__(self):
        return self.C1_name

class Cate2(models.Model):
    C2_id = models.AutoField("二级分类ID", primary_key=True, null=False, help_text="自动生成，主键，不能为空值")
    C2_name = models.CharField("分类名称", max_length=50, unique=True)
    C2_shorthand = models.CharField("名称简写", max_length=2)
    FK_C1id = models.ForeignKey(Cate1)

class Cate3(models.Model):
    C3_id = models.AutoField("三级分类ID", primary_key=True, null=False, help_text="自动生成，主键，不能为空值")
    C2_name = models.CharField("分类名称", max_length=50, unique=True)
    C2_shorthand = models.CharField("名称简写", max_length=2,)
    FK_C2id = models.ForeignKey(Cate2)

class UPC(models.Model):
    UPC = models.CharField('UPC', max_length=12, primary_key=True)
    Used = models.CharField('是否使用', max_length=1, choices=(('Y', "是"), ('N', "否")), default='', blank=True)
    U_date = models.DateTimeField('使用时间', null=True, blank=True)
    sku = models.CharField('对应SKU', max_length=200, null=True, default='', blank=True)
    Asin = models.CharField('对应ASIN', max_length=12, null=True, default='', blank=True)
