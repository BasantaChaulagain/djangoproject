from django.db import models

class Subject(models.Model):
    subName = models.CharField(max_length=100)

    def __str__(self):
        return self.subName

class Practical(models.Model):
    title = models.CharField(max_length=500)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    practical = models.ForeignKey(Practical, blank=False, on_delete=models.CASCADE)
    index = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.practical.title + ' - ' + str(self.index)