from django.db import models
from brand.models import Brand


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="车型名称", unique=True, help_text="车型名称")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    year_count = models.IntegerField(verbose_name="年销量", help_text="年销量")
    B_id = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="品牌ID", help_text="品牌ID")

    class Meta:
        db_table = "tb_type"
        verbose_name = "汽车型号"
        verbose_name_plural = verbose_name
