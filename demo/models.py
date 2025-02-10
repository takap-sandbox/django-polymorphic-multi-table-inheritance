from django.db import models
from polymorphic.models import PolymorphicModel


class Plan(PolymorphicModel):
    name = models.CharField(max_length=100)
    monthly_base_fee = models.IntegerField(default=0)

    def price(self):
        raise NotImplementedError

class HobbyPlan(Plan):
    def price(self):
        return self.monthly_base_fee

class ProPlan(Plan):
    pro_rate = models.IntegerField(default=100)
    def price(self):
        return self.monthly_base_fee * self.pro_rate
