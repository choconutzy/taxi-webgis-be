from django.db import models

class BaseModel(models.Model):

  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class MSError(BaseModel):
  class Meta:
    db_table = 'errors'
    
  code = models.IntegerField(null=False)
  module = models.CharField(max_length=256, null=False)
  message = models.TextField(null=False)
  
  def __str__(self):
    return f"{self.module} at {self.created_at.strftime('%Y/%m/%d')}"
