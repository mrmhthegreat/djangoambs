# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    added_by = models.CharField(max_length=191, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    slug = models.CharField(max_length=120, blank=True, null=True)
    product_type = models.CharField(max_length=20)
    category_ids = models.CharField(max_length=80, blank=True, null=True)
    category_id = models.CharField(max_length=191, blank=True, null=True)
    sub_category_id = models.CharField(max_length=191, blank=True, null=True)
    sub_sub_category_id = models.CharField(max_length=191, blank=True, null=True)
    brand_id = models.BigIntegerField(blank=True, null=True)
    unit = models.CharField(max_length=191, blank=True, null=True)
    min_qty = models.IntegerField()
    refundable = models.IntegerField()
    digital_product_type = models.CharField(max_length=30, blank=True, null=True)
    digital_file_ready = models.CharField(max_length=191, blank=True, null=True)
    digital_file_ready_storage_type = models.CharField(max_length=10, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    color_image = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_storage_type = models.CharField(max_length=10, blank=True, null=True)
    featured = models.CharField(max_length=255, blank=True, null=True)
    flash_deal = models.CharField(max_length=255, blank=True, null=True)
    video_provider = models.CharField(max_length=30, blank=True, null=True)
    video_url = models.CharField(max_length=150, blank=True, null=True)
    colors = models.CharField(max_length=150, blank=True, null=True)
    variant_product = models.IntegerField()
    attributes = models.CharField(max_length=255, blank=True, null=True)
    choice_options = models.TextField(blank=True, null=True)
    variation = models.TextField(blank=True, null=True)
    digital_product_file_types = models.TextField(blank=True, null=True)
    digital_product_extensions = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    unit_price = models.FloatField()
    purchase_price = models.FloatField()
    tax = models.CharField(max_length=191)
    tax_type = models.CharField(max_length=80, blank=True, null=True)
    tax_model = models.CharField(max_length=20)
    discount = models.CharField(max_length=191)
    discount_type = models.CharField(max_length=80, blank=True, null=True)
    current_stock = models.IntegerField(blank=True, null=True)
    minimum_order_qty = models.IntegerField()
    details = models.TextField(blank=True, null=True)
    free_shipping = models.IntegerField()
    attachment = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    featured_status = models.IntegerField()
    meta_title = models.CharField(max_length=191, blank=True, null=True)
    meta_description = models.CharField(max_length=191, blank=True, null=True)
    meta_image = models.CharField(max_length=191, blank=True, null=True)
    request_status = models.IntegerField()
    denied_note = models.TextField(blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    multiply_qty = models.IntegerField(blank=True, null=True)
    temp_shipping_cost = models.FloatField(blank=True, null=True)
    is_shipping_cost_updated = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
