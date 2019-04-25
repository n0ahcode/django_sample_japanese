from django.db import models




class Post(models.Model):
    text = models.CharField(max_length=100,verbose_name='タスク')
    time = models.DateTimeField(auto_now_add=True,verbose_name='登録時間')

    def __str__(self):
        return self.text
