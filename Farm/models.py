from django.db import models

# Create your models here.
class UploadLog(models.Model):
    bugID = models.CharField(max_length=20, verbose_name="bug号")
    caseName = models.CharField(max_length=200, verbose_name="case名")
    FwVersion = models.CharField(max_length=20, verbose_name="FW版本")
    IP = models.CharField(max_length=20, verbose_name="机器ip")
    nodeName = models.CharField(max_length=200, verbose_name="机器的node name")
    configID = models.CharField(max_length=20, verbose_name="case的config ID")





































