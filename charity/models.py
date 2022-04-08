from django.db import models


class Charity(models.Model):
    type = models.CharField(max_length=15)
    poster = models.ImageField(upload_to="posters/%Y/%m/%d/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    trustfund = models.ForeignKey("trustfund.TrustFund", on_delete=models.CASCADE, related_name="charities")
