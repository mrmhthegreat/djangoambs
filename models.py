# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AddFundBonusCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bonus_type = models.CharField(max_length=50)
    bonus_amount = models.FloatField()
    min_add_money_amount = models.FloatField()
    max_bonus_amount = models.FloatField()
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_fund_bonus_categories'


class AddonSettings(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    key_name = models.CharField(max_length=191, blank=True, null=True)
    live_values = models.TextField(blank=True, null=True)
    test_values = models.TextField(blank=True, null=True)
    settings_type = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=20)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    additional_data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addon_settings'


class AdminRoles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    module_access = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_roles'


class AdminWalletHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField()
    order_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    payment = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_wallet_histories'


class AdminWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    inhouse_earning = models.FloatField()
    withdrawn = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    commission_earned = models.FloatField()
    delivery_charge_earned = models.FloatField()
    pending_amount = models.FloatField()
    total_tax_collected = models.FloatField()

    class Meta:
        managed = False
        db_table = 'admin_wallets'


class Admins(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    admin_role_id = models.BigIntegerField()
    image = models.CharField(max_length=30)
    identify_image = models.TextField(blank=True, null=True)
    identify_type = models.CharField(max_length=255, blank=True, null=True)
    identify_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=80)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=80)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admins'


class Attributes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attributes'


class Banners(models.Model):
    id = models.BigAutoField(primary_key=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    banner_type = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    published = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    resource_type = models.CharField(max_length=191, blank=True, null=True)
    resource_id = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    sub_title = models.CharField(max_length=191, blank=True, null=True)
    button_text = models.CharField(max_length=191, blank=True, null=True)
    background_color = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banners'


class BillingAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    contact_person_name = models.CharField(max_length=191, blank=True, null=True)
    address_type = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    zip = models.CharField(max_length=191, blank=True, null=True)
    phone = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing_addresses'


class Brands(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=50)
    image_storage_type = models.CharField(max_length=10, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class BusinessSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=50)
    value = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_settings'


class CartShippings(models.Model):
    id = models.BigAutoField(primary_key=True)
    cart_group_id = models.CharField(max_length=191, blank=True, null=True)
    shipping_method_id = models.BigIntegerField(blank=True, null=True)
    shipping_cost = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_shippings'


class Carts(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    cart_group_id = models.CharField(max_length=191, blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=20)
    digital_product_type = models.CharField(max_length=30, blank=True, null=True)
    color = models.CharField(max_length=191, blank=True, null=True)
    choices = models.TextField(blank=True, null=True)
    variations = models.TextField(blank=True, null=True)
    variant = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()
    tax_model = models.CharField(max_length=20)
    is_checked = models.IntegerField()
    slug = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    thumbnail = models.CharField(max_length=191, blank=True, null=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    seller_is = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    shop_info = models.CharField(max_length=191, blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    shipping_type = models.CharField(max_length=191, blank=True, null=True)
    is_guest = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carts'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    icon = models.CharField(max_length=250, blank=True, null=True)
    icon_storage_type = models.CharField(max_length=10, blank=True, null=True)
    parent_id = models.IntegerField()
    position = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    home_status = models.IntegerField()
    priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryShippingCosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.PositiveBigIntegerField(blank=True, null=True)
    category_id = models.PositiveIntegerField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    multiply_qty = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_shipping_costs'


class Chattings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    delivery_man_id = models.BigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    attachment = models.JSONField(blank=True, null=True)
    sent_by_customer = models.IntegerField()
    sent_by_seller = models.IntegerField()
    sent_by_admin = models.IntegerField(blank=True, null=True)
    sent_by_delivery_man = models.IntegerField(blank=True, null=True)
    seen_by_customer = models.IntegerField()
    seen_by_seller = models.IntegerField()
    seen_by_admin = models.IntegerField(blank=True, null=True)
    seen_by_delivery_man = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    notification_receiver = models.CharField(max_length=20, blank=True, null=True, db_comment='admin, seller, customer, deliveryman')
    seen_notification = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    shop_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chattings'


class Colors(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'colors'


class Contacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    mobile_number = models.CharField(max_length=191)
    subject = models.CharField(max_length=191)
    message = models.TextField()
    seen = models.IntegerField()
    feedback = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Coupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    added_by = models.CharField(max_length=191)
    coupon_type = models.CharField(max_length=50, blank=True, null=True)
    coupon_bearer = models.CharField(max_length=191)
    seller_id = models.BigIntegerField(blank=True, null=True, db_comment='NULL=in-house, 0=all seller')
    customer_id = models.BigIntegerField(blank=True, null=True, db_comment='0 = all customer')
    title = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    min_purchase = models.DecimalField(max_digits=8, decimal_places=2)
    max_discount = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    discount_type = models.CharField(max_length=15)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons'


class Currencies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    symbol = models.CharField(max_length=191)
    code = models.CharField(max_length=191)
    exchange_rate = models.CharField(max_length=191)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerWalletHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_type = models.CharField(max_length=20, blank=True, null=True)
    transaction_method = models.CharField(max_length=30, blank=True, null=True)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_wallet_histories'


class CustomerWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    royality_points = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_wallets'


class DealOfTheDays(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    discount_type = models.CharField(max_length=12)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deal_of_the_days'


class DeliveryCountryCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    country_code = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_country_codes'


class DeliveryHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    deliveryman_id = models.BigIntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    location = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_histories'


class DeliveryManTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    delivery_man_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    user_type = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=36)
    debit = models.DecimalField(max_digits=50, decimal_places=2)
    credit = models.DecimalField(max_digits=50, decimal_places=2)
    transaction_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_man_transactions'


class DeliveryMen(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    f_name = models.CharField(max_length=100, blank=True, null=True)
    l_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True, null=True)
    identity_number = models.CharField(max_length=30, blank=True, null=True)
    identity_type = models.CharField(max_length=50, blank=True, null=True)
    identity_image = models.CharField(max_length=191, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch = models.CharField(max_length=191, blank=True, null=True)
    account_no = models.CharField(max_length=191, blank=True, null=True)
    holder_name = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    is_online = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    auth_token = models.CharField(max_length=191)
    fcm_token = models.CharField(max_length=191, blank=True, null=True)
    app_language = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'delivery_men'


class DeliveryZipCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    zipcode = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_zip_codes'


class DeliverymanNotifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    delivery_man_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    description = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliveryman_notifications'


class DeliverymanWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    delivery_man_id = models.BigIntegerField()
    current_balance = models.DecimalField(max_digits=50, decimal_places=2)
    cash_in_hand = models.DecimalField(max_digits=50, decimal_places=2)
    pending_withdraw = models.DecimalField(max_digits=50, decimal_places=2)
    total_withdraw = models.DecimalField(max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliveryman_wallets'


class DigitalProductOtpVerifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_details_id = models.CharField(max_length=255, blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    otp_hit_count = models.IntegerField()
    is_temp_blocked = models.IntegerField()
    temp_block_time = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digital_product_otp_verifications'


class DigitalProductVariations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    variant_key = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=8, blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digital_product_variations'


class EmailTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    template_name = models.CharField(max_length=191)
    user_type = models.CharField(max_length=191)
    template_design_name = models.CharField(max_length=191)
    title = models.CharField(max_length=191, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    banner_image = models.CharField(max_length=191, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    logo = models.CharField(max_length=191, blank=True, null=True)
    button_name = models.CharField(max_length=191, blank=True, null=True)
    button_url = models.CharField(max_length=191, blank=True, null=True)
    footer_text = models.CharField(max_length=191, blank=True, null=True)
    copyright_text = models.CharField(max_length=191, blank=True, null=True)
    pages = models.JSONField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)
    hide_field = models.JSONField(blank=True, null=True)
    button_content_status = models.IntegerField()
    product_information_status = models.IntegerField()
    order_information_status = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates'


class EmergencyContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=191)
    country_code = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=25)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_contacts'


class ErrorLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_code = models.IntegerField()
    url = models.CharField(max_length=255)
    hit_counts = models.IntegerField()
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    redirect_status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_logs'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class FeatureDeals(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=191, blank=True, null=True)
    photo = models.CharField(max_length=191, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature_deals'


class FlashDealProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    flash_deal_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    discount_type = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flash_deal_products'


class FlashDeals(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.IntegerField()
    featured = models.IntegerField()
    background_color = models.CharField(max_length=255, blank=True, null=True)
    text_color = models.CharField(max_length=255, blank=True, null=True)
    banner = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    deal_type = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flash_deals'


class GuestUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guest_users'


class HelpTopics(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=191)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    ranking = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'help_topics'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=191)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LoyaltyPointTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=36)
    credit = models.DecimalField(max_digits=24, decimal_places=3)
    debit = models.DecimalField(max_digits=24, decimal_places=3)
    balance = models.DecimalField(max_digits=24, decimal_places=3)
    reference = models.CharField(max_length=191, blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loyalty_point_transactions'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MostDemandeds(models.Model):
    id = models.BigAutoField(primary_key=True)
    banner = models.CharField(max_length=255)
    product_id = models.PositiveBigIntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'most_demandeds'


class NotificationMessages(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_type = models.CharField(max_length=191, blank=True, null=True)
    key = models.CharField(max_length=191, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_messages'


class NotificationSeens(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    notification_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_seens'


class Notifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    sent_by = models.CharField(max_length=255)
    sent_to = models.CharField(max_length=255)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    notification_count = models.IntegerField()
    image = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.PositiveIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField()
    client_id = models.PositiveIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class OfflinePaymentMethods(models.Model):
    id = models.BigAutoField(primary_key=True)
    method_name = models.CharField(max_length=255)
    method_fields = models.TextField()
    method_informations = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offline_payment_methods'


class OfflinePayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.IntegerField()
    payment_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offline_payments'


class OrderDeliveryVerifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    image = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_delivery_verifications'


class OrderDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    digital_file_after_sell = models.CharField(max_length=191, blank=True, null=True)
    product_details = models.TextField(blank=True, null=True)
    qty = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField()
    tax_model = models.CharField(max_length=20)
    delivery_status = models.CharField(max_length=15)
    payment_status = models.CharField(max_length=15)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    shipping_method_id = models.BigIntegerField(blank=True, null=True)
    variant = models.CharField(max_length=255, blank=True, null=True)
    variation = models.CharField(max_length=255, blank=True, null=True)
    discount_type = models.CharField(max_length=30, blank=True, null=True)
    is_stock_decreased = models.IntegerField()
    refund_request = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_details'


class OrderExpectedDeliveryHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    user_type = models.CharField(max_length=191)
    expected_delivery_date = models.DateField()
    cause = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_expected_delivery_histories'


class OrderStatusHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    user_type = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    cause = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status_histories'


class OrderTransactions(models.Model):
    seller_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_amount = models.DecimalField(max_digits=50, decimal_places=2)
    seller_amount = models.DecimalField(max_digits=50, decimal_places=2)
    admin_commission = models.DecimalField(max_digits=50, decimal_places=2)
    received_by = models.CharField(max_length=191)
    status = models.CharField(max_length=191, blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=50, decimal_places=2)
    tax = models.DecimalField(max_digits=50, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    seller_is = models.CharField(max_length=191, blank=True, null=True)
    delivered_by = models.CharField(max_length=191)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.CharField(max_length=191, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'order_transactions'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.CharField(max_length=15, blank=True, null=True)
    is_guest = models.IntegerField()
    customer_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=15)
    order_status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    transaction_ref = models.CharField(max_length=30, blank=True, null=True)
    payment_by = models.CharField(max_length=191, blank=True, null=True)
    payment_note = models.TextField(blank=True, null=True)
    order_amount = models.FloatField()
    admin_commission = models.DecimalField(max_digits=8, decimal_places=2)
    is_pause = models.CharField(max_length=20)
    cause = models.CharField(max_length=191, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discount_amount = models.FloatField()
    discount_type = models.CharField(max_length=30, blank=True, null=True)
    coupon_code = models.CharField(max_length=191, blank=True, null=True)
    coupon_discount_bearer = models.CharField(max_length=191)
    shipping_responsibility = models.CharField(max_length=255, blank=True, null=True)
    shipping_method_id = models.BigIntegerField()
    shipping_cost = models.FloatField()
    is_shipping_free = models.IntegerField()
    order_group_id = models.CharField(max_length=191)
    verification_code = models.CharField(max_length=191)
    verification_status = models.IntegerField()
    seller_id = models.BigIntegerField(blank=True, null=True)
    seller_is = models.CharField(max_length=191, blank=True, null=True)
    shipping_address_data = models.TextField(blank=True, null=True)
    delivery_man_id = models.BigIntegerField(blank=True, null=True)
    deliveryman_charge = models.FloatField()
    expected_delivery_date = models.DateField(blank=True, null=True)
    order_note = models.TextField(blank=True, null=True)
    billing_address = models.PositiveBigIntegerField(blank=True, null=True)
    billing_address_data = models.TextField(blank=True, null=True)
    order_type = models.CharField(max_length=191)
    extra_discount = models.FloatField()
    extra_discount_type = models.CharField(max_length=191, blank=True, null=True)
    free_delivery_bearer = models.CharField(max_length=255, blank=True, null=True)
    checked = models.IntegerField()
    shipping_type = models.CharField(max_length=191, blank=True, null=True)
    delivery_type = models.CharField(max_length=191, blank=True, null=True)
    delivery_service_name = models.CharField(max_length=191, blank=True, null=True)
    third_party_delivery_tracking_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class PasswordResets(models.Model):
    identity = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    otp_hit_count = models.IntegerField()
    is_temp_blocked = models.IntegerField()
    temp_block_time = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=191)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PaymentRequests(models.Model):
    id = models.CharField(max_length=36)
    payer_id = models.CharField(max_length=64, blank=True, null=True)
    receiver_id = models.CharField(max_length=64, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=24, decimal_places=2)
    gateway_callback_url = models.CharField(max_length=191, blank=True, null=True)
    success_hook = models.CharField(max_length=100, blank=True, null=True)
    failure_hook = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    currency_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    additional_data = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    is_paid = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payer_information = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    external_redirect_link = models.CharField(max_length=255, blank=True, null=True)
    receiver_information = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    attribute_id = models.CharField(max_length=64, blank=True, null=True)
    attribute = models.CharField(max_length=255, blank=True, null=True)
    payment_platform = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_requests'


class PaytabsInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField()
    result = models.TextField()
    response_code = models.PositiveIntegerField()
    pt_invoice_id = models.PositiveIntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.PositiveIntegerField(blank=True, null=True)
    card_brand = models.CharField(max_length=191, blank=True, null=True)
    card_first_six_digits = models.PositiveIntegerField(blank=True, null=True)
    card_last_four_digits = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paytabs_invoices'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=191)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=191)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class PhoneOrEmailVerifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_or_email = models.CharField(max_length=191, blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)
    otp_hit_count = models.IntegerField()
    is_temp_blocked = models.IntegerField()
    temp_block_time = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_or_email_verifications'


class ProductCompares(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(db_comment='customer_id')
    product_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_compares'


class ProductSeos(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=255, blank=True, null=True)
    no_follow = models.CharField(max_length=255, blank=True, null=True)
    no_image_index = models.CharField(max_length=255, blank=True, null=True)
    no_archive = models.CharField(max_length=255, blank=True, null=True)
    no_snippet = models.CharField(max_length=255, blank=True, null=True)
    max_snippet = models.CharField(max_length=255, blank=True, null=True)
    max_snippet_value = models.CharField(max_length=255, blank=True, null=True)
    max_video_preview = models.CharField(max_length=255, blank=True, null=True)
    max_video_preview_value = models.CharField(max_length=255, blank=True, null=True)
    max_image_preview = models.CharField(max_length=255, blank=True, null=True)
    max_image_preview_value = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_seos'


class ProductStocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    variant = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stocks'


class ProductTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField()
    tag_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tag'


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


class RefundRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_details_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=191)
    approved_count = models.IntegerField()
    denied_count = models.IntegerField()
    amount = models.FloatField()
    product_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    refund_reason = models.TextField()
    images = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    approved_note = models.TextField(blank=True, null=True)
    rejected_note = models.TextField(blank=True, null=True)
    payment_info = models.TextField(blank=True, null=True)
    change_by = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_requests'


class RefundStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    refund_request_id = models.PositiveBigIntegerField(blank=True, null=True)
    change_by = models.CharField(max_length=191, blank=True, null=True)
    change_by_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=191, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_statuses'


class RefundTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_for = models.CharField(max_length=191, blank=True, null=True)
    payer_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_receiver_id = models.PositiveBigIntegerField(blank=True, null=True)
    paid_by = models.CharField(max_length=191, blank=True, null=True)
    paid_to = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    payment_status = models.CharField(max_length=191, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    order_details_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    refund_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refund_transactions'


class ReviewReplies(models.Model):
    id = models.BigAutoField(primary_key=True)
    review_id = models.IntegerField()
    added_by_id = models.IntegerField(blank=True, null=True)
    added_by = models.CharField(max_length=255, db_comment='customer, seller, admin, deliveryman')
    reply_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_replies'


class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.BigIntegerField()
    customer_id = models.BigIntegerField()
    delivery_man_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    attachment = models.JSONField(blank=True, null=True)
    rating = models.IntegerField()
    status = models.IntegerField()
    is_saved = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class RobotsMetaContents(models.Model):
    id = models.BigAutoField(primary_key=True)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    page_name = models.CharField(max_length=255, blank=True, null=True)
    page_url = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_image = models.CharField(max_length=255, blank=True, null=True)
    canonicals_url = models.CharField(max_length=255, blank=True, null=True)
    index = models.CharField(max_length=255, blank=True, null=True)
    no_follow = models.CharField(max_length=255, blank=True, null=True)
    no_image_index = models.CharField(max_length=255, blank=True, null=True)
    no_archive = models.CharField(max_length=255, blank=True, null=True)
    no_snippet = models.CharField(max_length=255, blank=True, null=True)
    max_snippet = models.CharField(max_length=255, blank=True, null=True)
    max_snippet_value = models.CharField(max_length=255, blank=True, null=True)
    max_video_preview = models.CharField(max_length=255, blank=True, null=True)
    max_video_preview_value = models.CharField(max_length=255, blank=True, null=True)
    max_image_preview = models.CharField(max_length=255, blank=True, null=True)
    max_image_preview_value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'robots_meta_contents'


class SearchFunctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    visible_for = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_functions'


class SellerWalletHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    amount = models.FloatField()
    order_id = models.BigIntegerField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)
    payment = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seller_wallet_histories'


class SellerWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    total_earning = models.FloatField()
    withdrawn = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    commission_given = models.FloatField()
    pending_withdraw = models.FloatField()
    delivery_charge_earned = models.FloatField()
    collected_cash = models.FloatField()
    total_tax_collected = models.FloatField()

    class Meta:
        managed = False
        db_table = 'seller_wallets'


class Sellers(models.Model):
    id = models.BigAutoField(primary_key=True)
    f_name = models.CharField(max_length=30, blank=True, null=True)
    l_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    image = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=80)
    password = models.CharField(max_length=80, blank=True, null=True)
    status = models.CharField(max_length=15)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=191, blank=True, null=True)
    branch = models.CharField(max_length=191, blank=True, null=True)
    account_no = models.CharField(max_length=191, blank=True, null=True)
    holder_name = models.CharField(max_length=191, blank=True, null=True)
    auth_token = models.TextField(blank=True, null=True)
    sales_commission_percentage = models.FloatField(blank=True, null=True)
    gst = models.CharField(max_length=191, blank=True, null=True)
    cm_firebase_token = models.CharField(max_length=191, blank=True, null=True)
    pos_status = models.IntegerField()
    minimum_order_amount = models.FloatField()
    free_delivery_status = models.IntegerField()
    free_delivery_over_amount = models.FloatField()
    app_language = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'sellers'


class ShippingAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.CharField(max_length=15, blank=True, null=True)
    is_guest = models.IntegerField()
    contact_person_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.CharField(max_length=191, blank=True, null=True)
    longitude = models.CharField(max_length=191, blank=True, null=True)
    is_billing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_addresses'


class ShippingMethods(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.BigIntegerField(blank=True, null=True)
    creator_type = models.CharField(max_length=191)
    title = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_methods'


class ShippingTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.PositiveBigIntegerField(blank=True, null=True)
    shipping_type = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_types'


class ShopFollowers(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.IntegerField()
    user_id = models.IntegerField(db_comment='Customer ID')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_followers'


class Shops(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.BigIntegerField()
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=191)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=25)
    image = models.CharField(max_length=30)
    image_storage_type = models.CharField(max_length=10, blank=True, null=True)
    bottom_banner = models.CharField(max_length=191, blank=True, null=True)
    bottom_banner_storage_type = models.CharField(max_length=10, blank=True, null=True)
    offer_banner = models.CharField(max_length=255, blank=True, null=True)
    offer_banner_storage_type = models.CharField(max_length=10, blank=True, null=True)
    vacation_start_date = models.DateField(blank=True, null=True)
    vacation_end_date = models.DateField(blank=True, null=True)
    vacation_note = models.CharField(max_length=255, blank=True, null=True)
    vacation_status = models.IntegerField()
    temporary_close = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    banner = models.CharField(max_length=191)
    banner_storage_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class SocialMedias(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)
    active_status = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_medias'


class SoftCredentials(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=191, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soft_credentials'


class Storages(models.Model):
    id = models.BigAutoField(primary_key=True)
    data_type = models.CharField(max_length=255)
    data_id = models.CharField(max_length=100)
    key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storages'


class Subscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class SupportTicketConvs(models.Model):
    id = models.BigAutoField(primary_key=True)
    support_ticket_id = models.BigIntegerField(blank=True, null=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    customer_message = models.CharField(max_length=191, blank=True, null=True)
    attachment = models.JSONField(blank=True, null=True)
    admin_message = models.CharField(max_length=191, blank=True, null=True)
    position = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_ticket_convs'


class SupportTickets(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=150, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=15)
    description = models.CharField(max_length=255, blank=True, null=True)
    attachment = models.JSONField(blank=True, null=True)
    reply = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=15)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'support_tickets'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=191)
    visit_count = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class Transactions(models.Model):
    id = models.AutoField(unique=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    payment_for = models.CharField(max_length=100, blank=True, null=True)
    payer_id = models.BigIntegerField(blank=True, null=True)
    payment_receiver_id = models.BigIntegerField(blank=True, null=True)
    paid_by = models.CharField(max_length=15, blank=True, null=True)
    paid_to = models.CharField(max_length=15, blank=True, null=True)
    payment_method = models.CharField(max_length=15, blank=True, null=True)
    payment_status = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    order_details_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Translations(models.Model):
    translationable_type = models.CharField(max_length=191)
    translationable_id = models.PositiveBigIntegerField()
    locale = models.CharField(max_length=191)
    key = models.CharField(max_length=191, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'translations'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    f_name = models.CharField(max_length=255, blank=True, null=True)
    l_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=25)
    image = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=80)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=80)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    street_address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    house_no = models.CharField(max_length=50, blank=True, null=True)
    apartment_no = models.CharField(max_length=50, blank=True, null=True)
    cm_firebase_token = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    payment_card_last_four = models.CharField(max_length=191, blank=True, null=True)
    payment_card_brand = models.CharField(max_length=191, blank=True, null=True)
    payment_card_fawry_token = models.TextField(blank=True, null=True)
    login_medium = models.CharField(max_length=191, blank=True, null=True)
    social_id = models.CharField(max_length=191, blank=True, null=True)
    is_phone_verified = models.IntegerField()
    temporary_token = models.CharField(max_length=191, blank=True, null=True)
    is_email_verified = models.IntegerField()
    wallet_balance = models.FloatField(blank=True, null=True)
    loyalty_point = models.FloatField(blank=True, null=True)
    login_hit_count = models.IntegerField()
    is_temp_blocked = models.IntegerField()
    temp_block_time = models.DateTimeField(blank=True, null=True)
    referral_code = models.CharField(max_length=255, blank=True, null=True)
    referred_by = models.IntegerField(blank=True, null=True)
    app_language = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'users'


class VendorRegistrationReasons(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_registration_reasons'


class WalletTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=36)
    credit = models.DecimalField(max_digits=24, decimal_places=3)
    debit = models.DecimalField(max_digits=24, decimal_places=3)
    admin_bonus = models.DecimalField(max_digits=24, decimal_places=3)
    balance = models.DecimalField(max_digits=24, decimal_places=3)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_transactions'


class Wishlists(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.BigIntegerField()
    product_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlists'


class WithdrawRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    seller_id = models.BigIntegerField(blank=True, null=True)
    delivery_man_id = models.BigIntegerField(blank=True, null=True)
    admin_id = models.BigIntegerField(blank=True, null=True)
    amount = models.CharField(max_length=191)
    withdrawal_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    withdrawal_method_fields = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    transaction_note = models.TextField(blank=True, null=True)
    approved = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'withdraw_requests'


class WithdrawalMethods(models.Model):
    id = models.BigAutoField(primary_key=True)
    method_name = models.CharField(max_length=191)
    method_fields = models.TextField()
    is_default = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'withdrawal_methods'
