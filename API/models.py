from django.db import models

class Question(models.Model):
    question_text = models.TextField()
    options = models.TextField()
    correct_option = models.IntegerField()
    module = models.ForeignKey('Module', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    explanation = models.TextField()

    def __str__(self):
        return self.question_text

class Module(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Identifier(models.Model):
    user_ID = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class History(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    history = models.TextField()

    def __str__(self):
        return self.history[0:50] + "..."