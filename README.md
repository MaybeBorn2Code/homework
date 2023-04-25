# homework
class Author(models.Model):
  user = models.OneToOneField(to=User)
  sm_pp = models.SmallIntegerField(validators=[MaxValueValidator(5)])
class Book(models.Model):
  title = models.CharField(max_lenght=200)
  pages = models.PositiveIntegerField()
  authors = models.ManyToManyField(to=Author, related_name='books')
Сгенерировать 1000 моделей и сделать так, чтобы звпрос на все модели был в 2
запроса в базу данных
