from django.db import models
import uuid


class BaseModel(models.Model):  # base class
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True, editable=False)
    CreatedOn = models.DateField(auto_now_add=True, db_index=True, verbose_name="Oluşturma Tarihi")
    ModifiedOn = models.DateField(db_index=True,auto_now=True, verbose_name="Güncelleme Tarihi")
    IsDone = models.BooleanField(default=True, verbose_name="Durumu")

    class Meta:
        abstract = True  # Set this model as Abstract