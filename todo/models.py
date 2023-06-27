from django.db import models

# Create your models here.


class Todo(models.Model):
    
    PRIOIRITY = (
        (1,'High'), # kullanıcı 1 i seçerse high
        (2,'Medium'),
        (3,'Low'),
    )
    
    task = models.CharField(max_length =50)
    description = models.TextField(blank = True)
    prioirity = models.SmallIntegerField(choices=PRIOIRITY, default=3)
    is_done =models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True) #eğer bir değişiklk yapıldıysa pc nın yerel saatini al
    created_date = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.task
    
    