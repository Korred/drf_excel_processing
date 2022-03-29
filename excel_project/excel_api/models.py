from django.db import models


class ExcelDocument(models.Model):
    file = models.FileField(upload_to="excel")
    filename = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Excel Document"
        verbose_name_plural = "Excel Documents"
