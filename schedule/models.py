from django.db import models
from django.urls import reverse

class Doctor(models.Model):
    name = models.CharField(max_length=16)
    department = models.CharField(max_length=50) #儿科，妇科 like so...
    def __str__(self):
        return self.name

class Branch(models.Model): #分院名字
    b_name = models.CharField(max_length=50)
    def __str__(self):
        return self.b_name

class Arrange(models.Model): #医生出诊排班
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
#   arrange = models.CharField(max_length=14)

    MORNING = "上午"
    AFTERNOON ="下午"
    WHOLEDAY = "全天"
    DAYOFF = "休息"
    
    PLAN_CHOICE = (
                    (MORNING,"上午"), 
                    (AFTERNOON,"下午"), 
                    (WHOLEDAY,"全天"),
                    (DAYOFF, "休息"),
                  )
    mon = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    tue = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    wed = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    thu = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    fri = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    sat = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)
    sun = models.CharField(max_length=10, choices=PLAN_CHOICE, default=DAYOFF)

    class Meta:
        unique_together = ("doctor","branch")

    def __str__(self):
        message = self.doctor.name + " : "  + self.branch.b_name
        return message

    def get_absolute_url(self):
        return reverse('schedule:bybranch', kwargs={'b_id': self.branch.id})

    

