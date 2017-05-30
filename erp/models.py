from django.db import models
import django.utils.timezone
import datetime
import time
from PIL import Image

# Create your models here.



class cost(models.Model):
    c_id = models.AutoField('序号', auto_created=True, primary_key=True)
    create_date = models.DateTimeField('创建日期')
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
    KC1_name = models.CharField('一级科目', max_length=200, unique=True)

class km_c2(models.Model):
    KC2_id = models.AutoField(primary_key=True, auto_created=True)
    KC2_name = models.CharField('二级科目', max_length=200,unique=True)
    id_kc1_kc2 = models.ForeignKey(km_c1)

class km_c3(models.Model):
    KC3_id = models.AutoField(primary_key=True, auto_created=True)
    KC3_name = models.CharField('三级科目', max_length=200, unique=True, blank=True)
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

class IMG(models.Model):
    img_path = models.ImageField('图片路径', upload_to='Pimgage')
    img_name = models.CharField('图片名称', max_length=50)

class Photo(models.Model):
    now = str(time.time())
    filepath = 'pimage/' + now + '/'
    photo_org = models.FileField('Photo', upload_to=filepath)
    photo_small = models.CharField('Small', max_length=255)

    def save(self):
        super(Photo, self).save()
        photopath = str(self.photo_org.path)
        im = Image.open(photopath)
        width, height = im.size

        small_srcoll_num = 0.4
        small_width = width * small_srcoll_num
        small_height = height * small_srcoll_num
        extension = photopath.rsplit('.', 1)[1]
        filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]
        fullpath = photopath.rsplit('/', 1)[0]

        im.thumbnail((small_width, small_height), Image.ANTIALIAS)
        small_name = filename + '_small.' + extension
        now_path = fullpath + '/' + small_name

        if im.mode != 'RGB':
            im.mode = 'RGB'

        im.save(now_path)
        self.photo_small = self.filepath + small_name

        super(Photo, self).save()


#定义产品库表
class Product(models.Model):
    pid = models.CharField('产品ID', max_length=4, primary_key=True)
    name = models.CharField('产品名称', max_length=255)
    p_c1 = models.CharField('一级分类', max_length=255)
    p_c2 = models.CharField('二级分类', max_length=255)
    p_c3 = models.CharField('三级分类', max_length=255)
    p_img = models.ImageField('产品图片', upload_to='/media/', null=True)
    P_size = models.CharField('尺码', max_length=255, )
    P_color = models.CharField('颜色', max_length=255, )
    p_price = models.DecimalField('成本价', max_digits=10, decimal_places=2)
    p_discount = models.DecimalField('折扣', max_digits=10, decimal_places=2)


#定义尺码表
class Size(models.Model):
    Size_name = models.CharField('尺码', max_length=255, primary_key=True)
    Ext_name_1 = models.CharField('尺码别名', max_length=255, null=True)

#定义颜色表
class Color(models.Model):
    color_name = models.CharField('颜色', max_length=30, primary_key=True)
    color_name_cn = models.CharField('中文', max_length=100)

#产品图片
class P_image(models.Model):
    img_id = models.ForeignKey(Product)
    path = 'product_image/'+ str(time.time())+ '/'
    image_org = models.ImageField('原图', upload_to=path)
    image_big = models.ImageField('大图', max_length=255)
    image_128_128 = models.ImageField('中图', max_length=255)
    image_64_64 = models.ImageField('小图', max_length=255)

#定义产品扩展表
class Product_ext(models.Model):
    ex_pid = models.ForeignKey(Product)
    supplier = models.CharField('供应商', max_length=255)
    Item_number = models.CharField('货号', max_length=255)
    Product_source = models.URLField('采购链接', max_length=255)
    supplier_code = models.CharField('供应商条码', max_length=255)
    ext_size_us = models.CharField('US码', max_length=255)

#定义产品库存表


#定义产品出入库表





# class Tem(models.Model):
#     item_sku = models.CharField('SKU', max_length=255, primary_key=True)
#     item_name =
#     item_sku
#     item_name
#     external_product_id
#     external_product_id_type
#     brand_name
#     product_description
#     item_type
#     model
#     update_delete
#     standard_price
#     list_price
#     product_tax_code
#     fulfillment_latency
#     product_site_launch_date
#     merchant_release_date
#     restock_date
#     quantity
#     sale_price
#     sale_from_date
#     sale_end_date
#     max_aggregate_ship_quantity
#     item_package_quantity
#     number_of_items
#     offering_can_be_gift_messaged
#     offering_can_be_giftwrapped
#     is_discontinued_by_manufacturer	missing_keyset_reason	merchant_shipping_group_name	website_shipping_weight	website_shipping_weight_unit_of_measure	item_weight_unit_of_measure	item_weight	item_length_unit_of_measure	item_length	item_width	item_height	bullet_point1	bullet_point2	bullet_point3	bullet_point4	bullet_point5	generic_keywords1	generic_keywords2	generic_keywords3	generic_keywords4	generic_keywords5	main_image_url	other_image_url1	other_image_url2	other_image_url3	other_image_url4	other_image_url5	swatch_image_url	fulfillment_center_id	package_height	package_width	package_length	package_length_unit_of_measure	package_weight	package_weight_unit_of_measure	parent_child	parent_sku	relationship_type	variation_theme	cpsia_cautionary_statement	cpsia_cautionary_description	fabric_type	import_designation	closure_type	belt_style	bottom_style	subject_character	chest_size	chest_size_unit_of_measure	band_size_num	band_size_num_unit_of_measure	collar_style	color_name	color_map	control_type	cup_size	department_name	fabric_wash	fit_type	front_style	inseam_length	inseam_length_unit_of_measure	rise_height	rise_height_unit_of_measure	leg_diameter	leg_diameter_unit_of_measure	leg_style	country_as_labeled	fur_description	opacity	neck_size	neck_size_unit_of_measure	neck_style	pattern_type	pocket_description	rise_style	shoe_width	size_name	size_map	special_size_type	sleeve_length	sleeve_length_unit_of_measure	sleeve_type	special_features	strap_type	style_name	theme	toe_style	top_style	underwire_type	waist_size	waist_size_unit_of_measure	water_resistance_level	sport_type	wheel_type

















