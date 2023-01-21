from django.db import models

# Create your models here.
class ReviewModel(models.Model):
    lname=models.CharField(max_length=15,verbose_name="Имя")
    fname=models.CharField(max_length=15,verbose_name="Фамилия")
    pol=models.CharField(
        max_length=1,
        choices=(("M","M"),("W","W")),
        verbose_name="Пол"
    )
    vozrast=models.DateTimeField(verbose_name="Возраст")
    pochta=models.EmailField(max_length=255,verbose_name="Почта")


    def __str__(self) -> str:
        return self.lname

#параметры для таблицы
    class Meta:
        verbose_name="Отзыв"    
        verbose_name_plural="Отзывы"  
          









